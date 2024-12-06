def find_initial_path(data):
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

    return positions

def find_path_cycle(data, input_pos, input_dir):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    positions = set((input_pos, input_dir))
    min_row, max_row = 0, len(data)
    min_col, max_col = 0, len(data[0])

    current_pos = input_pos
    current_dir = input_dir
    
    while True:
        if (current_pos, current_dir) in positions: 
            return True

        positions.add((current_pos, current_dir))

        dr, dc = directions[current_dir]
        next_pos = (current_pos[0] + dr, current_pos[1] + dc)
        
        if not (min_row <= next_pos[0] < max_row and min_col <= next_pos[1] < max_col):
            break
        
        next_r, next_c = next_pos
        if data[next_r][next_c] == '#':
            current_dir = turn_right[current_dir]
        else:
            current_pos = next_pos

    return False

def find_loop_positions(data):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

    loop_positions = 0
    visited = find_initial_path(data)

    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char in directions:
                initial_pos = (i, j)
                initial_dir = char
                break

    for obstruction in visited:
        new_data = [row[:] for row in data]
        or_r, or_c = obstruction
        new_data[or_r][or_c] = '#'


        if find_path_cycle(new_data, initial_pos, initial_dir): 
            loop_positions += 1

    return loop_positions


if __name__ == '__main__':
    with open('6_input.txt', 'r') as f2:
        data = f2.read().splitlines()

    data = [[c for c in s] for s in data]

    res = find_loop_positions(data)

    print(res)
