def convert_input_to_rock_paper_scissor(selection: str):
    if selection == "A" or selection == "X":
        return "rock"

    if selection == "B" or selection == "Y":
        return "paper"

    if selection == "C" or selection == "Z":
        return "scissors"


def convert_input_to_win_lose_draw(selection: str):
    if selection == "X":
        return "p2"

    if selection == "Y":
        return "draw"

    if selection == "Z":
        return "p1"


def rock_paper_scissor_rules(p1: str, p2: str) -> str:
    """
    Returns the outcome of a rock, paper, scissor match

    :param p1: "rock", "paper", "scissor"
    :param p2: "rock", "paper", "scissors"
    :return: string with the following: "p1", "p2", "draw"
    """
    if p1 == p2:
        return "draw"

    p1_condition_to_win = (
        p1 == "paper" and p2 == "rock",
        p1 == "scissors" and p2 == "paper",
        p1 == "rock" and p2 == "scissors",
    )
    if any(p1_condition_to_win):
        return "p1"
    return "p2"


def what_to_play_to_get_the_outcome(outcome: str, p2: str) -> str:
    """
    Returns the outcome of a rock, paper, scissor match

    :param outcome: "p1", "p2", "draw"
    :param p2: "rock", "paper", "scissors"
    :return: string with the following: "p1", "p2", "draw"
    """
    if outcome == "draw":
        return p2

    if outcome == "p1":
        if p2 == "rock":
            return "paper"
        if p2 == "paper":
            return "scissors"
        return "rock"
    if p2 == "rock":
        return "scissors"
    if p2 == "paper":
        return "rock"
    return "paper"


def elf_game_points(p1: str, p2: str) -> int:
    """
    returns the amount of points player 1 gets in a game

    :param p1:
    :param p2:
    :return: the total points
    """
    game_points = 0

    if p1 == "rock":
        game_points += 1
    if p1 == "paper":
        game_points += 2
    if p1 == "scissors":
        game_points += 3

    game_result = rock_paper_scissor_rules(p1, p2)

    if game_result == "p1":
        game_points += 6
    if game_result == "draw":
        game_points += 3

    return game_points


def elf_tournament():
    total_points = 0

    with open('day2_input.txt') as f:
        tournament = f.readlines()
        for match in tournament:
            p2 = convert_input_to_rock_paper_scissor(match[0])
            p1 = convert_input_to_rock_paper_scissor(match[2])
            total_points += elf_game_points(p1, p2)
    return total_points


def elf_tournament_with_defined_outcome():
    total_points = 0

    with open('day2_input.txt') as f:
        tournament = f.readlines()
        for match in tournament:
            p2 = convert_input_to_rock_paper_scissor(match[0])
            p1 = convert_input_to_win_lose_draw(match[2])
            p1 = what_to_play_to_get_the_outcome(p1, p2)
            total_points += elf_game_points(p1, p2)
    return total_points


if __name__ == '__main__':
    print(elf_tournament())
    print(elf_tournament_with_defined_outcome())
