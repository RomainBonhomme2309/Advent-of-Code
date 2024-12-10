def find_trailheads(topographic_map):
    trailheads = []
    for r, row in enumerate(topographic_map):
        for c, height in enumerate(row):
            if height == 0:
                trailheads.append((r, c))
    return trailheads

def calculate_rating(topographic_map, trailhead):
    rows, cols = len(topographic_map), len(topographic_map[0])
    r_start, c_start = trailhead

    def dfs(r, c, path):
        if (r, c) in path:
            return 0

        path.add((r, c))
        current_height = topographic_map[r][c]

        if current_height == 9:
            path.remove((r, c))
            return 1

        trail_count = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                next_height = topographic_map[nr][nc]
                if next_height == current_height + 1:
                    trail_count += dfs(nr, nc, path)

        path.remove((r, c))
        return trail_count

    return dfs(r_start, c_start, set())
def calculate_total_rating(topographic_map):
    trailheads = find_trailheads(topographic_map)
    total_rating = 0

    for trailhead in trailheads:
        total_rating += calculate_rating(topographic_map, trailhead)

    return total_rating

if __name__ == '__main__':
    with open('10_input.txt', 'r') as f:
        data = [[int(c) for c in line.strip()] for line in f.read().splitlines()]

    res = calculate_total_rating(data)

    print(res)
