def find_mid(line):
    mid = len(line) // 2
    return line[mid]

def check_safety(rules, line):
    for i in range(len(line)):
        for rule in rules:
            if line[i] == rule[0]:
                if rule[1] in line[:i]:
                    return False
                    
    return True

def sum_mid_safe_lines(rules, lines):
    safe, mid = [], []
    for i in range(len(lines)):
        if check_safety(rules, lines[i]): safe.append(lines[i])

    for line in safe:
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

    res = sum_mid_safe_lines(rules, lines)

    print(res)
