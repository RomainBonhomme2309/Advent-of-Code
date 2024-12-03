import re

def sum_enabled_muls(input_data):
    enabled = True
    total = 0
    for command in re.findall(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", input_data):
        if command == "do()":
            enabled = True
        elif command == "don't()":
            enabled = False
        elif enabled and command.startswith("mul"):
            x, y = map(int, re.findall(r"\d+", command))
            total += x * y
    return total



if __name__ == '__main__':
    with open('3_input.txt', 'r') as f2:
        data = f2.read()
    
    res = sum_enabled_muls(data)

    print(res)
