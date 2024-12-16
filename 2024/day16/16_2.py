import heapq

def dijkstra(grid, starts):
    delta = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}

    dist = {}
    pq = []
    for sr, sc, dir in starts:
        dist[(sr, sc, dir)] = 0
        heapq.heappush(pq, (0, sr, sc, dir))

    while pq:
        d, row, col, direction = heapq.heappop(pq)
        if dist[(row, col, direction)] < d:
            continue
        for next_dir in "EWNS".replace(direction, ""):
            if (row, col, next_dir) not in dist or dist[(row, col, next_dir)] > d + 1000:
                dist[(row, col, next_dir)] = d + 1000
                heapq.heappush(pq, (d + 1000, row, col, next_dir))
        dr, dc = delta[direction]
        next_row, next_col = row + dr, col + dc
        if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]) and grid[next_row][next_col] != "#":
            if (next_row, next_col, direction) not in dist or dist[(next_row, next_col, direction)] > d + 1:
                dist[(next_row, next_col, direction)] = d + 1
                heapq.heappush(pq, (d + 1, next_row, next_col, direction))

    return dist

def part1(grid, s, e):
    (sr, sc), (er, ec) = s, e
    dist = dijkstra(grid, [(sr, sc, "E")])
    best = float('inf')

    for dir in "EWNS":
        if (er, ec, dir) in dist:
            best = min(best, dist[(er, ec, dir)])

    return best

def solve(grid, optimal):
    from_start = dijkstra(grid, [(s[0], s[1], "E")])
    from_end = dijkstra(grid, [(e[0], e[1], d) for d in "EWNS"])

    flip = {"E": "W", "W": "E", "N": "S", "S": "N"}
    result = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for dir in "EWNS":
                state_from_start = (row, col, dir)
                state_from_end = (row, col, flip[dir])
                if state_from_start in from_start and state_from_end in from_end:
                    if from_start[state_from_start] + from_end[state_from_end] == optimal:
                        result.add((row, col))

    return len(result)

if __name__ == '__main__':
    with open('16_input.txt', 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]

    s = None
    e = None

    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == "S":
                s = (r, c)
            elif ch == "E":
                e = (r, c)

    optimal = part1(grid, s, e)
    
    res = solve(grid, optimal)

    print(res)
