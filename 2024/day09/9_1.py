def compute_checksum(data):
    checksum = 0
    full, free = [], []

    for i in range(len(data)):
        if (i % 2) == 0:
            full.append(i)
        else:
            free.append(i)

    nb_to_add = 0
    processed = []

    for i in range(len(full)):
        for _ in range(data[full[i]]):
            processed.append(nb_to_add)

        if i < len(free):
            for _ in range(data[free[i]]):
                processed.append('.')

        nb_to_add += 1

    while '.' in processed:
        last = processed.pop()
        if last != '.':
            dot_index = processed.index('.')
            processed[dot_index] = last

    checksum = 0

    for i in range(len(processed)):
        checksum += i * processed[i]

    return checksum


if __name__ == "__main__":
    with open('9_input.txt', 'r') as f:
        data = [int(c) for c in f.read().strip()]

    res = compute_checksum(data)

    print(res)
