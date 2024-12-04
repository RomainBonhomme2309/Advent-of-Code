def count_xmas(grid):
    word = "XMAS"
    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (-1, 1)
    ]
    
    def check_direction(r, c, dr, dc):
        for i in range(len(word)):
            nr, nc = r + i * dr, c + i * dc
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != word[i]:
                return 0
        return 1

    count = 0
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                count += check_direction(r, c, dr, dc)
    
    return count

if __name__ == '__main__':
    with open('4_input.txt', 'r') as f2:
        data = f2.read().splitlines()

    res = count_xmas(data)

    print(res)
