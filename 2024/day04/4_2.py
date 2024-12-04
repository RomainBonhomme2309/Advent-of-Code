def count_xmas_shapes(grid):
    word = "MAS"
    rows, cols = len(grid), len(grid[0])
    
    def check_xmas_shape(r, c):
        count = 0

        diagonal1 = [(r-1, c-1), (r, c), (r+1, c+1)]
        diagonal2 = [(r+1, c-1), (r, c), (r-1, c+1)]
        
        def is_valid(coords, pattern):
                return all(0 <= x < rows and 0 <= y < cols and grid[x][y] == pattern[i] 
                           for i, (x, y) in enumerate(coords))

        if is_valid(diagonal1, word) and is_valid(diagonal2, word):
            count += 1
        if is_valid(diagonal1, word[::-1]) and is_valid(diagonal2, word[::-1]):
            count += 1
        if is_valid(diagonal1, word) and is_valid(diagonal2, word[::-1]):
            count += 1
        if is_valid(diagonal1, word[::-1]) and is_valid(diagonal2, word):
            count += 1
        
        return count

    count = 0
    for r in range(rows):
        for c in range(cols):
            count += check_xmas_shape(r, c)

    return count

if __name__ == '__main__':
    with open('4_input.txt', 'r') as f2:
        data = f2.read().splitlines()
    
    res = count_xmas_shapes(data)

    print(res)
