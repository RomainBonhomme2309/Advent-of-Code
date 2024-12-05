def find_mid(line):
    mid = len(line) // 2
    return line[mid]

def swap(line, l1, i, l2, j):
    tmp = l1
    line[i] = l2
    line[j] = tmp

    return line

def check_safety(rules, line):
    for i in range(len(line)):
        for rule in rules:
            if line[i] == rule[0]:
                if rule[1] in line[:i]:
                    return False
                    
    return True

def reorder_line(rules, line):
    while True:
        for i in range(1, len(line)):
            for rule in rules:
                if line[i] == rule[0]:
                    for j in range(len(line[:i])):
                        if line[j] == rule[1]:
                            line = swap(line, line[i], i, line[j], j)

        if check_safety(rules, line): return line

def sum_mid_unsafe_lines(rules, lines):
    unsafe, mid = [], []
    for i in range(len(lines)):
        if not (check_safety(rules, lines[i])): unsafe.append(lines[i])

    for i, line in enumerate(unsafe):
        unsafe[i] = reorder_line(rules, line)
        mid.append(find_mid(line))

    return sum(mid)

if __name__ == '__main__':
    rules, lines = [], []
    splitter = 0

    with open('5_input.txt', 'r') as f2:
        data = f2.read().splitlines()

        for i in range(len(data)):
            if data[i] == '': splitter = i
    
    rules = [[int(s) for s in st.split('|')] for st in  data[:splitter]]
    lines = [[int(s) for s in st.split(',')] for st in data[splitter+1:]]

    res = sum_mid_unsafe_lines(rules, lines)

    print(res)
