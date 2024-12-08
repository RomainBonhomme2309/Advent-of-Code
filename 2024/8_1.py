def parse_map(input_map):
    """Parse the input map to extract antenna positions and frequencies."""
    antennas = []
    for y, row in enumerate(input_map):
        for x, char in enumerate(row):
            if char != '.':
                antennas.append((x, y, char))
    return antennas

def find_antinodes(antennas, grid_width, grid_height):
    """Calculate unique antinode locations within the grid bounds."""
    antinodes = set()
    
    for i, (x1, y1, freq1) in enumerate(antennas):
        for j, (x2, y2, freq2) in enumerate(antennas):
            if i >= j:  # Avoid duplicate pairs
                continue
            if freq1 != freq2:  # Frequencies must match
                continue
            
            # Calculate the difference vector between the antennas
            dx, dy = x2 - x1, y2 - y1
            
            # Antinode 1: One step "back" from the first antenna
            ax1, ay1 = x1 - dx, y1 - dy
            if 0 <= ax1 < grid_width and 0 <= ay1 < grid_height:
                antinodes.add((ax1, ay1))
            
            # Antinode 2: One step "forward" from the second antenna
            ax2, ay2 = x2 + dx, y2 + dy
            if 0 <= ax2 < grid_width and 0 <= ay2 < grid_height:
                antinodes.add((ax2, ay2))

    # Include the antennas themselves as antinodes
    for x, y, _ in antennas:
        antinodes.add((x, y))
    
    return antinodes

def count_unique_antinodes(input_map):
    """Main function to solve the problem."""
    grid_width = len(input_map[0])
    grid_height = len(input_map)
    antennas = parse_map(input_map)
    antinodes = find_antinodes(antennas, grid_width, grid_height)
    return len(antinodes)


if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        data = f.read().splitlines()

    res = count_unique_antinodes(data)
    print(res)
