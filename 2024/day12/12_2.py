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
    num_sides = 0

    while stack:
      cx, cy = stack.pop()
      area += 1

      for nx, ny in get_neighbors(cx, cy):
        if data[nx][ny] == plant_type:
          if not visited[nx][ny]:
            visited[nx][ny] = True
            stack.append((nx, ny))
        else:
          if (nx, ny) not in visited:
            num_sides += 1

    return area, num_sides

  visited = [[False] * len(data[0]) for _ in range(len(data))]
  total_price = 0

  for i in range(len(data)):
    for j in range(len(data[0])):
      if not visited[i][j]:
        plant_type = data[i][j]
        area, num_sides = dfs(i, j, plant_type)
        total_price += area * num_sides

  return total_price

if __name__ == '__main__':
  with open('test.txt', 'r') as f2:
    data = f2.read().splitlines()

  res = fencing_price(data)

  print(res)
