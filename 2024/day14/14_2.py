import os
from PIL import Image

def save_grid_images(data, w, t, max_time, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    positions = [p for p, _ in data]
    velocities = [v for _, v in data]

    for time in range(max_time):
        grid = [[0] * w for _ in range(t)]

        for i, (p, v) in enumerate(zip(positions, velocities)):
            new_x = (p[0] + v[0] * time) % w
            new_y = (p[1] + v[1] * time) % t
            grid[new_y][new_x] += 1

        img = Image.new('RGB', (w, t), "white")
        pixels = img.load()

        for y in range(t):
            for x in range(w):
                if grid[y][x] > 0:
                    pixels[x, y] = (0, 0, 0)

        img.save(os.path.join(output_folder, f"grid_{time:04d}.png"))

    print(f"Saved {max_time} images in '{output_folder}'.")

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
    max_time = 10000
    output_folder = "robot_grid_images"

    save_grid_images(parsed_data, w, t, max_time, output_folder)
