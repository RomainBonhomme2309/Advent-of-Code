from collections import Counter

def split_middle(nb):
    nb_str = str(nb)
    mid = len(nb_str) // 2
    return int(nb_str[:mid]), int(nb_str[mid:])

def split_middle_counts(counts):
    new_counts = Counter()
    for num, count in counts.items():
        if len(str(num)) % 2 == 0:
            front, back = split_middle(num)
            new_counts[front] += count
            new_counts[back] += count
        else:
            new_counts[num] += count
    return new_counts

def calculate_number_stones(data, nb_blinks):
    counts = Counter(data)

    for _ in range(nb_blinks):
        new_counts = Counter()
        for num, count in counts.items():
            if num == 0:
                new_counts[1] += count
            elif len(str(num)) % 2 == 0:
                front, back = split_middle(num)
                new_counts[front] += count
                new_counts[back] += count
            else:
                new_counts[num * 2024] += count
        counts = new_counts

    return sum(counts.values())

if __name__ == "__main__":
    with open('11_input.txt', 'r') as f:
        data = [int(x) for x in f.read().strip().split()]

    nb_blinks = 25

    res = calculate_number_stones(data, nb_blinks)

    print(res)

