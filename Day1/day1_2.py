import numpy as np
import os

def simple_similarity(x, l):
    sim = [i for i,val in enumerate(l) if val==x]
    count = len(sim)
    return x * count

def total_similarity(x):
    return np.sum(x)


if __name__ == '__main__':
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, 'data.txt')
    input_file = open(file_path, 'r')

    l1, l2, sim = [], [], []

    for line in input_file:
        p1, p2 = line.split()
        l1.append(int(p1))
        l2.append(int(p2))

    for i in range(len(l1)):
        sim.append(simple_similarity(l1[i], l2))

    total = total_similarity(sim)

    print(total)
