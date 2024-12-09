def extract_blocks(processed):
    blocks = []
    current_symbol = processed[0]
    start_index = 0
    length = 0

    for i, symbol in enumerate(processed):
        if symbol == current_symbol:
            length += 1
        else:
            blocks.append((current_symbol, start_index, length))
            current_symbol = symbol
            start_index = i
            length = 1

    blocks.append((current_symbol, start_index, length))
    return blocks

def compact_files(processed):
    blocks = extract_blocks(processed)

    for symbol, start, length in reversed(blocks):
        if symbol == '.':
            continue

        for i, (free_symbol, free_start, free_length) in enumerate(blocks):
            if free_symbol == '.' and free_length >= length and free_start < start:

                processed[free_start:free_start + length] = [symbol] * length
                processed[start:start + length] = ['.'] * length

                blocks = extract_blocks(processed)
                break
    return processed

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

    processed = compact_files(processed)

    for i in range(len(processed)):
        if processed[i] != '.':
            checksum += i * processed[i]

    return checksum


if __name__ == "__main__":
    with open('9_input.txt', 'r') as f:
        data = [int(c) for c in f.read().strip()]

    res = compute_checksum(data)

    print(res)
