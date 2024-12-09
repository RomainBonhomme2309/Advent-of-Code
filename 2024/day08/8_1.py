def parse_map(input_map):
    antennas = []
    for x, row in enumerate(input_map):
        for y, char in enumerate(row):
            if char != '.':
                antennas.append((x, y, char))
    return antennas

def find_antinodes(antennas, grid_width, grid_height):
    antinodes = set()
    
    for i, (x1, y1, freq1) in enumerate(antennas):
        for j, (x2, y2, freq2) in enumerate(antennas):
            if freq1 != freq2:
                continue

            dx, dy = x2 - x1, y2 - y1

            ax2, ay2 = x2 + dx, y2 + dy
            if 0 <= ax2 < grid_width and 0 <= ay2 < grid_height and dx != 0 and dy != 0:
                antinodes.add((ax2, ay2))
    
    return antinodes

def count_unique_antinodes(input_map):
    grid_width = len(input_map)
    grid_height = len(input_map[0])
    antennas = parse_map(input_map)
    antinodes = find_antinodes(antennas, grid_width, grid_height)
    return len(antinodes)


if __name__ == '__main__':
    with open('8_input.txt', 'r') as f:
        data = f.read().splitlines()

    res = count_unique_antinodes(data)

    print(res)
