# Implement 'bisect' functionality of revision control
# Find last working commit, given a good and a bad

FIRST_FAIL = 672

def test(x):
    return True if x < FIRST_FAIL else False

def bisect(good, bad):
    while True:
        half = (good + bad) / 2
        passing = test(half)
        is_target = passing and not test(half + 1)
        if is_target:
            return half
        if passing:
            good = half
        else:
            bad = half

print bisect(17, 7000)
