import numpy as np

def is_increasing(lst):
    return all(i < j for i, j in zip(lst, lst[1:]))

def is_decreasing(lst):
    return all(i > j for i, j in zip(lst, lst[1:]))

def close_values(l):
    return all(np.abs(l[i] - l[i+1]) <= 3 for i in range(len(l) - 1))

def is_safe(l):
    if (is_increasing(l) or is_decreasing(l)) and close_values(l):
        return True
    else:
        return False

if __name__ == '__main__':
    l = []
    safe = 0

    with open("data.txt", mode="rt") as file:
        for line in file:
            l.append([int(s) for s in line.strip().split()])

    for i in range(len(l)):
            for j in range(len(l[i])):   
                if is_safe(l[i][0:j] + l[i][j+1:]):
                    safe += 1
                    break

    print(safe)