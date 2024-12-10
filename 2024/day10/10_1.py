def find_trailheads(map):
    trailheads = []
    for r, row in enumerate(map):
        for c, height in enumerate(row):
            if height == 0:
                trailheads.append((r, c))
    return trailheads

def calculate_score(map, trailhead):
    rows, cols = len(map), len(map[0])
    visited = set()
    path = [trailhead]
    reachable_nines = set()

    while path:
        r, c = path.pop(0)
        if (r, c) in visited:
            continue
        visited.add((r, c))

        current_height = map[r][c]
        if current_height == 9:
            reachable_nines.add((r, c))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if map[nr][nc] == current_height + 1:
                    path.append((nr, nc))

    return len(reachable_nines)

def calculate_total_score(data):
    trailheads = find_trailheads(data)
    total_score = 0

    for trailhead in trailheads:
        total_score += calculate_score(data, trailhead)

    return total_score


if __name__ == '__main__':
    with open('10_input.txt', 'r') as f:
        data = [[int(c) for c in line.strip()] for line in f.read().splitlines()]

    res = calculate_total_score(data)

    print(res)
