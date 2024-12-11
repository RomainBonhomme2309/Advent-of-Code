def split_middle(nb):
    nb_str = str(nb)
    mid = len(nb_str) // 2
    return int(nb_str[:mid]), int(nb_str[mid:])

def calculate_number_stones(data, nb_blinks):
    def modify_config(config, iter):
        if iter > nb_blinks:
            return len(config)
        
        new_config = []
        for nb in config:
            if nb == 0:
                new_config.append(1)
            elif len(str(abs(nb))) % 2 == 0:
                front, back = split_middle(nb)
                new_config.append(front)
                new_config.append(back)
            else:
                new_config.append(nb * 2024)

        return modify_config(new_config, iter + 1)

    return modify_config(data, 1)

if __name__ == "__main__":
    with open('11_input.txt', 'r') as f:
        data = [int(x) for x in f.read().strip().split()]

    nb_blinks = 25

    res = calculate_number_stones(data, nb_blinks)

    print(res)
