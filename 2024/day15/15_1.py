def simulate_warehouse(map_data):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

    robot_pos = None
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == '@':
                robot_pos = (i, j)
                map_data[i][j] = '.'
                break
        if robot_pos:
            break

    for move in moves:
        dr, dc = directions[move]
        new_robot_pos = (robot_pos[0] + dr, robot_pos[1] + dc)
        r, c = new_robot_pos

        if 0 <= r < len(map_data) and 0 <= c < len(map_data[0]):
            if map_data[r][c] == '.':
                robot_pos = new_robot_pos
            elif map_data[r][c] == 'O':
                box_r, box_c = r + dr, c + dc
                while 0 <= box_r < len(map_data) and 0 <= box_c < len(map_data[0]) and map_data[box_r][box_c] == 'O':
                    next_box_r, next_box_c = box_r + dr, box_c + dc
                    if 0 <= next_box_r < len(map_data) and 0 <= next_box_c < len(map_data[0]) and map_data[next_box_r][next_box_c] == '.':
                        map_data[next_box_r][next_box_c] = 'O'
                        map_data[box_r][box_c] = '.'
                        box_r, box_c = next_box_r, next_box_c
                    else:
                        break

                robot_pos = new_robot_pos
                
    print(map_data)

    gps_sum = 0
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            if map_data[i][j] == 'O':
                gps_sum += i + (100 * j)
    
    return gps_sum

if __name__ == "__main__":
    with open('test.txt', 'r') as f2:
        data = f2.read().splitlines()

    map_data = []
    for line in data:
        if line.startswith('<') or line.startswith('^') or line.startswith('v') or line.startswith('>'):
            moves = line.strip()
        else:
            map_data.append(list(line.strip()))

    res = simulate_warehouse(map_data)

    print(res)
