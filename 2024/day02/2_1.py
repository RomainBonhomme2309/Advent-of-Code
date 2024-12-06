import numpy as np

def is_increasing(lst):
    return all(i < j for i, j in zip(lst, lst[1:]))

def is_decreasing(lst):
    return all(i > j for i, j in zip(lst, lst[1:]))

def close_values(l):
    return all(np.abs(l[i] - l[i+1]) <= 3 for i in range(len(l) - 1))

if __name__ == '__main__':
    l = []
    safe = 0

    with open("data.txt", mode="rt") as file:
        for line in file:
            l.append([int(s) for s in line.strip().split()])

    for i in range(len(l)):
        if (is_increasing(l[i]) or is_decreasing(l[i])) and close_values(l[i]):
            safe += 1

    print(safe)