def fencing_price(data):
    def get_neighbors(x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(data) and 0 <= ny < len(data[0]):
                yield nx, ny

    def dfs(x, y, plant_type):
        stack = [(x, y)]
        visited[x][y] = True
        area = 0
        perimeter = 0

        while stack:
            cx, cy = stack.pop()
            area += 1

            for nx, ny in get_neighbors(cx, cy):
                if data[nx][ny] == plant_type:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
                else:
                    perimeter += 1

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < len(data) and 0 <= ny < len(data[0])):
                    perimeter += 1

        return area, perimeter

    visited = [[False] * len(data[0]) for _ in range(len(data))]
    total_price = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            if not visited[i][j]:
                plant_type = data[i][j]
                area, perimeter = dfs(i, j, plant_type)
                total_price += area * perimeter

    return total_price

if __name__ == '__main__':
    with open('12_input.txt', 'r') as f2:
        data = f2.read().splitlines()

    res = fencing_price(data)

    print(res)
