def min_nb_tokens(machines):
    total_cost = 0

    for machine in machines:
        (x_a, y_a), (x_b, y_b), (prize_x, prize_y) = machine
        min_cost = float('inf')
        found_solution = False

        for a_count in range(101):
            for b_count in range(101):
                x_position = a_count * x_a + b_count * x_b
                y_position = a_count * y_a + b_count * y_b

                if x_position == prize_x and y_position == prize_y:
                    found_solution = True
                    cost = a_count * 3 + b_count * 1
                    min_cost = min(min_cost, cost)

        if found_solution:
            total_cost += min_cost

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
