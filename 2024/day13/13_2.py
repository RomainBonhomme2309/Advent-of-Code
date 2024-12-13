def solve_system2(x1, x2, price_x, y1, y2, price_y, offset):
    augmented_price_x = price_x + offset
    augmented_price_y = price_y + offset

    det = y2 * x1 - y1 * x2
    if det == 0:
        return (0, 0)

    pressed_a = augmented_price_x * y2 - augmented_price_y * x2
    pressed_b = augmented_price_y * x1 - augmented_price_x * y1

    if (pressed_a % det == 0) and (pressed_b % det == 0):
        return (int(pressed_a / det), int(pressed_b / det))
    else:
        return (0, 0)

def min_nb_tokens(machines):
    total_cost = 0

    for machine in machines:
        (x_a, y_a), (x_b, y_b), (prize_x, prize_y) = machine

        costs = solve_system2(x_a, x_b, prize_x, y_a, y_b, prize_y, 10_000_000_000_000)

        if costs is not None:
            total_cost += 3 * costs[0] + costs[1]

    return total_cost


if __name__ == '__main__':
    with open('13_input.txt', 'r') as f2:
        data = f2.read().splitlines()

    machines = []
    current_machine = []

    for line in data:
        if line.strip() == '':
            if current_machine:
                machines.append(current_machine)
                current_machine = []
        else:
            numbers = [int(x.split('+')[-1]) if '+' in x else int(x.split('=')[-1])
                       for x in line.split(', ')]
            current_machine.extend(numbers)

    if current_machine:
        machines.append(current_machine)

    machine_tuples = [list(zip(machine[::2], machine[1::2])) for machine in machines]

    res = min_nb_tokens(machine_tuples)

    print(res)
