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


def r_bisect(good, bad):
    half = (good + bad) / 2
    passing = test(half)
    is_target = passing and not test(half + 1)
    if is_target:
        return half
    if passing:
        return bisect(half, bad)
    else:
        return bisect(good, half)


print bisect(17, 700) == r_bisect(17, 700)
