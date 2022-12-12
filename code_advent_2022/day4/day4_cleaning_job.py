def pair_to_list(pair):
    """

    :param pair: "2-4"
    :return:
    """
    start, end = pair.split("-")
    start = int(start)
    end = int(end)
    section_to_clean = []
    while start <= end:
        section_to_clean.append(start)
        start += 1

    return section_to_clean


def get_number_of_totally_overlapped_elfs(cleaning_pairs):
    value = 0

    for pairs in cleaning_pairs:
        elf_1, elf_2 = pairs.split(",")

        elf_1 = pair_to_list(elf_1)
        elf_2 = pair_to_list(elf_2)

        interceptions = list(set(elf_1).intersection(elf_2))

        if len(interceptions) >= len(elf_1) or len(interceptions) >= len(elf_2):
            value += 1

    return value


def get_number_of_overlapped_elfs(cleaning_pairs):
    value = 0

    for pairs in cleaning_pairs:
        pairs = pairs.replace("\n", "")

        elf_1, elf_2 = pairs.split(",")

        elf_1_start, elf_1_end = elf_1.split("-")
        elf_2_start, elf_2_end = elf_2.split("-")

        conditions_to_overlap = (
            int(elf_1_start) <= int(elf_2_end) and int(elf_1_end) >= int(elf_2_start),
            int(elf_2_start) <= int(elf_1_end) and int(elf_2_end) >= int(elf_1_start),
        )
        if any(conditions_to_overlap):
            value += 1

    return value


def run_example_1():
    with open('day4_input_example.txt') as f:
        cleaning_pairs = f.readlines()
        print(get_number_of_totally_overlapped_elfs(cleaning_pairs))


def solve_challenge_1():
    with open('day4_input.txt') as f:
        cleaning_pairs = f.readlines()
        print(get_number_of_totally_overlapped_elfs(cleaning_pairs))


def run_example_2():
    with open('day4_input_example.txt') as f:
        cleaning_pairs = f.readlines()
        print(get_number_of_overlapped_elfs(cleaning_pairs))


def solve_challenge_2():
    with open('day4_input.txt') as f:
        cleaning_pairs = f.readlines()

        print(get_number_of_overlapped_elfs(cleaning_pairs))


if __name__ == '__main__':
    run_example_1()
    solve_challenge_1()
    run_example_2()
    solve_challenge_2()
