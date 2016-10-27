# Chef has an array of N integers. He wants to play a special game. In this game he needs to make all the integers in the array greater than or equal to 0.

# Chef can use two types of operations. The first type is to increase all the integers of the given array by 1, but it costs X coins. The operation of the second type is to add 1 to only one integer of the given array and to use this operation you need to pay 1 coin. You need to calculate the minimal cost to win this game (to make all integers greater than or equal to 0)


def list_zero(numbers, x_val):
    neg_numbers = [x for x in numbers if x < 0]
    if x_val < 1:
        return sum(neg_numbers) * x_val
    num = sorted(neg_numbers, reverse=True)
    return _helper(num, x_val)

def _helper(numbers, x_val):
    if len(numbers) == 1:
        return min(abs(numbers[0]) * x_val, abs(numbers[0]) * 1)
    num_to_apply = abs(numbers[0]) if numbers[0] < 0 else 0
    max_cost = sum(numbers)
    if num_to_apply > 0:
        numbers = [x + num_to_apply for x in numbers]
        return num_to_apply*x_val + _helper(numbers[1:], x_val)

print list_zero([-1, -2,-3], 2)
print list_zero([12,-1,-22,-3], 2)
