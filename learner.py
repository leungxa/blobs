from collections import OrderedDict

GLOBAL_SUB_POOL = []
GRADED_SUBS = []
REVIEWS = {}

class Status:
    DO_NOTHING, WORKING_ON_SUBMISSION, WAITING_TO_REVIEW, WORKING_ON_REVIEW, \
    FINISH_REVIEW, WAITING_FOR_GRADE, DONE = range(7)

class Learner:
    def __init__(self, l_id, l_fsst, l_fstg, l_review_bias):
        self.id = l_id
        self.first_sub_start_time = l_fsst
        self.first_sub_true_grade = l_fstg
        self.review_bias = l_review_bias
        self.sub_count = 0
        self.review_count = 0
        self.curr_status = Status.DO_NOTHING
        self.working_on_sub = None
        self.last_sub = None
        self.reviewing_sub = None
        self.review_start_time = None
        self.subs = []

    def update_status(self, status):
        self.curr_status = status
        print "learner", self.id, "new_status:", self.curr_status
        if self.curr_status == Status.DONE and self.has_grade():
            print self.last_sub.score_sum()
        
    def start_submission(self, curr_tick):
        if curr_tick != self.first_sub_start_time:
            return
        true_grade = min(Submission.MAX_SCORE, \
                         max(Submission.MIN_SCORE, \
                             self.first_sub_true_grade + self.sub_count * 15))
        sub = Submission(self, curr_tick, true_grade)
        self.working_on_sub = sub
        self.update_status(Status.WORKING_ON_SUBMISSION)
    
    def workon_or_submit_submission(self, curr_tick):
        # do nothing until time to submit
        if self.working_on_sub and \
                self.working_on_sub.sub_start_time + Submission.WORKING_TIME == curr_tick:
            GLOBAL_SUB_POOL.append(self.working_on_sub)
            self.subs.append(self.working_on_sub)
            self.last_sub = self.working_on_sub
            del self.working_on_sub
            self.sub_count += 1
            self.update_status(Status.WAITING_TO_REVIEW)
    
    def wait_subs_to_review(self, curr_tick):
    # waiting for submissions to review
        self.update_status(Status.WAITING_TO_REVIEW)
        # failing grade, work on next submission
        if self.last_sub.failing():
            self.start_submission(curr_tick)
        # if pool contains submissions they can review, start to review
        sub_to_review = Submission.get_available_sub_to_review(self)
        if sub_to_review:
            return self.start_review(curr_tick, sub_to_review)
        # if ^ dont apply, don't do anything

    def has_grade(self):
        return self.last_sub.has_grade()
        
    def start_review(self, curr_tick, submission):
        # goes through submissions, find one to review
        self.reviewing_sub = submission
        submission.current_reviewer_ids.add(self.id)
        self.review_start_time = curr_tick
        self.update_status(Status.WORKING_ON_REVIEW)
    
    def workon_or_submit_review(self, curr_tick):
        # do nothing until time to submit
        if self.review_start_time + Submission.REVIEW_TIME == curr_tick:
            sub = self.reviewing_sub
            score = min(Submission.MAX_SCORE, \
                        max(Submission.MIN_SCORE, sub.sub_true_grade + self.review_bias))
            review = Review(self, score, curr_tick)
            sub.reviews.append(review)
            sub.current_reviewer_ids.remove(self.id)
            if sub.has_grade():
                GRADED_SUBS.append(sub)
                GLOBAL_SUB_POOL.remove(sub)
            self.review_count += 1
            self.update_status(Status.FINISH_REVIEW)
    
    def after_submitting_review(self, curr_tick):
    # finishes a review
        # failing grade, work on next submission
        if self.last_sub.failing():
            return self.start_submission(curr_tick)
        # user submit fewer reviews than 3x theirsumbmissioncount, wait for subs to review
        if self.review_count < 3 * self.sub_count:
            return self.wait_subs_to_review(curr_tick)
        # if learners submission does not have a grade, wait for a grade
        if not self.has_grade():
            print "should go here"
            return self.wait_for_grade(curr_tick)
        # if ^ dont apply, learner is finished and stops doing anything
        print "why is it going to done", self.has_grade()
        return self.update_status(Status.DONE)
    
    def wait_for_grade(self, curr_tick):
        self.update_status(Status.WAITING_FOR_GRADE)
        if self.has_grade():
            # failing grade, work on next submission
            if self.last_sub.failing():
                return self.start_submission(curr_tick)
            else:
                self.update_status(Status.DONE)
    
    def tick(self, curr_tick):
        if self.curr_status == Status.DONE:
            return

        if self.curr_status == Status.DO_NOTHING:
            return self.start_submission(curr_tick)
                
        if self.curr_status == Status.WORKING_ON_SUBMISSION:
            return self.workon_or_submit_submission(curr_tick)
        
        if self.curr_status == Status.WAITING_TO_REVIEW:
            return self.wait_subs_to_review(curr_tick)

        if self.curr_status == Status.WORKING_ON_REVIEW:
            return self.workon_or_submit_review(curr_tick)
                
        if self.curr_status == Status.FINISH_REVIEW:
            return self.after_submitting_review(curr_tick)
        
        if self.curr_status == Status.WAITING_FOR_GRADE:
            return self.wait_for_grade(curr_tick)
        

class Submission:
    MIN_SCORE = 0
    MAX_SCORE = 100
    WORKING_TIME = 50
    REVIEW_TIME = 20
    PASSING_SCORE = 240
    REQUIRED_REVIEW_NUM = 3
    
    def __init__(self, author, sub_start_time, true_grade):
        self.author = author
        self.sequence_num = author.sub_count + 1
        self.sub_start_time = sub_start_time
        self.sub_true_grade = true_grade
        self.grade_tick = -1
        self.reviews = []
        self.current_reviewer_ids = set()

    @staticmethod
    def get_available_sub_to_review(learner):
        for sub in GLOBAL_SUB_POOL:
            if (sub.author.id != learner.id) and \
                    (learner.id not in [r.author.id for r in sub.reviews]) and \
                    (len(sub.reviews) + len(sub.current_reviewer_ids) < Submission.REQUIRED_REVIEW_NUM):
                return sub
        return None
        
    def score_sum(self):
        count = 0
        for r in self.reviews:
            count += r.score
        return count
    
    def has_grade(self):
        if len(self.reviews) == self.REQUIRED_REVIEW_NUM:
            return True
        return False
    
    def failing(self):
        score = self.score_sum()
        if (len(self.reviews) == 3 and score < self.PASSING_SCORE) or \
                (len(self.reviews) == 2 and score < self.PASSING_SCORE - 100) or \
                (len(self.reviews) == 1 and score < self.PASSING_SCORE - 200):
            return True
        return False

class Review:
    def __init__(self, author, score, curr_tick):
        self.author = author
        self.score = score
        self.review_time = curr_tick
    
def simulate(ticks):
    if ticks <= 0:
        return
    
    # create learners
    learners = [
        Learner(1, 1, 90, 2),
        Learner(2, 2, 98, 3),
        Learner(3, 2, 91, -1),
        Learner(4, 5, 80, -2)
    ]
    
    # tick learners
    for i in range(ticks):
        for l in learners:
            l.tick(i)

            
    print "GLOBAL_SUB~~~~~~~~~~"
    for sub in GLOBAL_SUB_POOL:
        print sub.author.id, sub.has_grade(), [r.author.id for r in sub.reviews], sub.score_sum()
    print "GRADED_SUB~~~~~~~~~~"
    for sub in GRADED_SUBS:
        print sub.author.id, sub.has_grade(), [r.author.id for r in sub.reviews], sub.score_sum()
    
    for l in learners:
        print l.subs

simulate(1500)
