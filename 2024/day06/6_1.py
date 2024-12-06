def find_path(data):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char in directions:
                current_pos = (i, j)
                current_dir = char
                break
    
    positions = set()
    min_row, max_row = 0, len(data)
    min_col, max_col = 0, len(data[0])
    
    while True:
        positions.add(current_pos)
        dr, dc = directions[current_dir]
        next_pos = (current_pos[0] + dr, current_pos[1] + dc)
        
        if not (min_row <= next_pos[0] < max_row and min_col <= next_pos[1] < max_col):
            break
        
        next_r, next_c = next_pos
        if data[next_r][next_c] == '#':
            current_dir = turn_right[current_dir]
        else:
            current_pos = next_pos

    return len(positions)


if __name__ == '__main__':
    with open('6_input.txt', 'r') as f2:
        data = f2.read().splitlines()
    data = [[c for c in s] for s in data]

    res = find_path(data)

    print(res)
