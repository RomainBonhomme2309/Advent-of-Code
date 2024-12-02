import numpy as np
import os

def simple_distance(x1, x2):
    return np.abs(x1 - x2)

def total_distance(x):
    return np.sum(x)

def sort_list(x):
    return np.sort(x)


if __name__ == '__main__':
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, 'data.txt')
    input_file = open(file_path, 'r')

    l1, l2, dist = [], [], []

    for line in input_file:
        p1, p2 = line.split()
        l1.append(int(p1))
        l2.append(int(p2))

    l1 = sort_list(l1)
    l2 = sort_list(l2)

    for i in range(len(l1)):
        dist.append(simple_distance(l1[i], l2[i]))

    total = total_distance(dist)

    print(total)
