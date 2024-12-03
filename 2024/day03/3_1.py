import re

def extract_and_sum(data):
    return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d{1,3}),\s*(\d{1,3})\)", data))
    

if __name__ == '__main__':
    with open('data.txt', 'r') as f2:
        data = f2.read()
    
    res = extract_and_sum(data)

    print(res)
