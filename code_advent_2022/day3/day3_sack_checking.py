import string


def calculate_item_value(letter):
    if letter.islower():
        return string.ascii_lowercase.index(letter) + 1
    return string.ascii_uppercase.index(letter) + 27


def sack_check_for_duplicates(sacks):
    value = 0
    for sack in sacks:
        sack = sack.replace("\n", "")
        split_sack_at = int(len(sack) / 2)
        sack_part_1 = sack[:split_sack_at]
        sack_part_2 = sack[split_sack_at:]

        list_of_duplicated_items = list(set(sack_part_1).intersection(sack_part_2))
        for item in list_of_duplicated_items:
            value += calculate_item_value(item)
    return value


def find_badges(sacks):
    groups_of = 3
    group_max = groups_of
    stored_items = None
    tokens = []
    value = 0

    for index, sack in enumerate(sacks):
        sack = sack.replace("\n", "")
        if index >= group_max:
            group_max += groups_of
            tokens.append(stored_items)
            stored_items = None

        if stored_items is None:
            stored_items = sack
            continue

        if stored_items is not None or stored_items != []:
            list_of_duplicated_items = list(set(sack).intersection(stored_items))
            stored_items = "".join(list_of_duplicated_items)

    tokens.append(stored_items)  # stores the last group badge

    for token in tokens:
        if token:
            value += calculate_item_value(token)
    return value


def run_example_1():
    with open('day3_input_example.txt') as f:
        sacks = f.readlines()
        print(sack_check_for_duplicates(sacks))


def solve_challenge_1():
    with open('day3_input.txt') as f:
        sacks = f.readlines()
        print(sack_check_for_duplicates(sacks))


def run_example_2():
    with open('day3_input_example.txt') as f:
        sacks = f.readlines()
        print(find_badges(sacks))


def solve_challenge_2():
    with open('day3_input.txt') as f:
        sacks = f.readlines()

        print(find_badges(sacks))


if __name__ == '__main__':
    run_example_1()
    solve_challenge_1()
    run_example_2()
    solve_challenge_2()
