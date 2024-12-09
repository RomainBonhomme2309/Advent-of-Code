from itertools import product

def concatenate(a, b):
    return int(f"{a}{b}")

def evaluate_expression(nums, ops):
    result = nums[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += nums[i + 1]
        elif op == '*':
            result *= nums[i + 1]
        elif op == '||':
            result = concatenate(result, nums[i + 1])
    return result

def is_equation_valid(target, nums):
    num_operators = len(nums) - 1
    for ops in product(['+', '*', '||'], repeat=num_operators):
        if evaluate_expression(nums, ops) == target:
            return True
    return False

def total_calibration_result(input_data):
    total = 0
    for line in input_data:
        target, numbers = line.split(":")
        target = int(target)
        nums = list(map(int, numbers.split()))

        if is_equation_valid(target, nums):
            total += target

    return total


if __name__ == '__main__':
    with open('7_input.txt', 'r') as f2:
        data = f2.read().splitlines()

    res = total_calibration_result(data)

    print(res)
