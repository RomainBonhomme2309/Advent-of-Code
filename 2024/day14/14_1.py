def compute_safety(data, w, t, time_limit):
    grid = [[0] * w for _ in range(t)]

    for p, v in data:
        p_x, p_y = p
        v_x, v_y = v

        new_x = (p_x + v_x * time_limit) % w
        new_y = (p_y + v_y * time_limit) % t

        grid[new_y][new_x] += 1

    quadrant_counts = [0, 0, 0, 0]

    for y in range(t):
        for x in range(w):
            if x < w // 2 and y < t // 2:
                quadrant_counts[0] += grid[y][x]
            elif x > w // 2 and y < t // 2:
                quadrant_counts[1] += grid[y][x]
            elif x < w // 2 and y > t // 2:
                quadrant_counts[2] += grid[y][x]
            elif x > w // 2 and y > t // 2:
                quadrant_counts[3] += grid[y][x]

    safety_factor = quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3]
    
    return safety_factor


if __name__ == '__main__':
    with open('14_input.txt', 'r') as f2:
        data = f2.read().splitlines()

    parsed_data = []

    for line in data:
        if line.strip():  # Skip empty lines
            p_str, v_str = line.split(' v=')  # Split at ' v='
            p_values = tuple(map(int, p_str.split('=')[1].split(',')))  # Convert 'p' to a tuple
            v_values = tuple(map(int, v_str.split(',')))  # Convert 'v' to a tuple
            parsed_data.append((p_values, v_values))  # Store as a tuple of (p, v)

    w, t = 101, 103
    time_limit = 100

    res = compute_safety(parsed_data, w, t, time_limit)

    print(res)
