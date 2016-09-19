# Task Scheduler
# List of Tasks / Queue of tasks: 1 1 2 1
# Cooldown / Recovery interval: 2s
# 1 _ _ 1 2 _ 1: 7s

# List of Tasks / Queue of tasks: 1 2 3 1 2 3
# Cooldown / Recovery interval: 3s
#
# 1 2 3 _ 1 2 3
# { 1: 3}
# { 1: 2, 2: 3}

# ...

# { 2: 1}

# ;

# { 1: 4, 2: 5, 3: 6}

def tick(cd_items, ticks):
    for j, cd in cd_items:
        new_cd = cd - ticks
        if new_cd =< 0:
            del cd_items[j]
        else:
            cd_items[j] = new_cd

def tasks(list_tasks, cd_time):
    cd_items = {}
    delays = 0
    for i, val in enumerate(list_tasks):
        delay = 0
        tick(cd_items)
        if val not in cd_items:
            cd_items[val] = cd_time
        else:
            delay = cd_items[val]
        if delay:
            tick(cd_items, delay)
            cd_items[val] = cd_time
            delays += delay
    return len(list_tasks) + delays
