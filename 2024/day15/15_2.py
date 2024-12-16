def resize_map(map_data):
    resized_map = []
    for row in map_data:
        new_row = []
        for tile in row:
            if tile == '#':
                new_row.append('##')
            elif tile == 'O':
                new_row.append('[]')
            elif tile == '.':
                new_row.append('..')
            elif tile == '@':
                new_row.append('@.')
            elif tile == '[' or tile == ']':
                new_row.append('[]')
        resized_map.append("".join(new_row))

    final_map = []
    for row in resized_map:
        if '@' not in row and '[]' not in row and '.' not in row:
            final_map.append(row)
        final_map.append(row)

    return [list(row) for row in final_map]


def simulate_warehouse(map_data, moves):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

    robot_pos = None
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == '@':
                robot_pos = (i, j)
                map_data[i][j] = '.'
                break
            elif robot_pos:
                break

    for move in moves:
        dr, dc = directions[move]
        new_robot_pos = (robot_pos[0] + dr, robot_pos[1] + dc)
        r, c = new_robot_pos

        if 0 <= r < len(map_data) and 0 <= c + 1 < len(map_data[0]):
            if map_data[r][c] == '.':
                robot_pos = new_robot_pos
            elif map_data[r][c] == '[':
                box_r, box_c = r + dr, c + dc
                while True:
                    if (0 <= box_r < len(map_data) and 0 <= box_c < len(map_data[0]) and map_data[box_r][box_c] != '.' and map_data[box_r][box_c] != '#'):
                        box_r += dr
                        box_c += dc
                        continue
                    elif (0 <= box_r < len(map_data) and 0 <= box_c < len(map_data[0]) and map_data[box_r][box_c] == '.'):
                        map_data[box_r][box_c] = '['
                        map_data[r][c] = '.'
                        
                        robot_pos = (r, c)
                        break
                    
                    else:
                        break
                    
            elif map_data[r][c+1] == ']':
                box_r, box_c = r + dr, c + dc
                while True:
                    if (0 <= box_r < len(map_data) and 0 <= box_c < len(map_data[0]) and map_data[box_r][box_c] != '.' and map_data[box_r][box_c] != '#'):
                        box_r += dr
                        box_c += dc
                        continue
                    elif (0 <= box_r < len(map_data) and 0 <= box_c < len(map_data[0]) and map_data[box_r][box_c] == '.'):
                        map_data[box_r][box_c] = ']'
                        map_data[r][c] = '.'
                        
                        robot_pos = (r, c)
                        break
                    
                    else:
                        break
                    
        for i in range(len(map_data)):
            print(map_data[i])
        print()

    gps_sum = 0
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j:j+2] == ['[', ']']:
                gps_sum += (100 * i) + j

    return gps_sum

if __name__ == "__main__":
    with open('test.txt', 'r') as f2:
        data = f2.read().splitlines()

    original_map_data = []
    for line in data:
        if line.startswith('<') or line.startswith('^') or line.startswith('v') or line.startswith('>'):
            moves = line.strip()
        else:
            original_map_data.append(list(line.strip()))

    scaled_map_data = resize_map(original_map_data)
    
    for i in range(len(scaled_map_data)):
        print(scaled_map_data[i])

    res = simulate_warehouse(scaled_map_data, moves)

    print(res)
