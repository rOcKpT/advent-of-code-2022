def elf_calorie_calculation():
    list_of_calories = [0]
    elf_number = 1
    with open('day1_input.txt') as f:
        lines = f.readlines()
        for calories in lines:
            # print(calories)
            if calories == "\n":
                elf_number += 1
                list_of_calories.append(0)
                continue
            calories.replace("\n", "")
            list_of_calories[elf_number - 1] += int(calories)
    return list_of_calories


def top_elf_calories(list_of_caloreis):
    return max(list_of_caloreis)


def top_3_elf_caloreis(list_of_calories):
    list_of_calories.sort(reverse=True)
    print(list_of_calories)
    total = 0
    for index, elf in enumerate(list_of_calories):
        if index >= 3:
            break

        total += elf

    return total


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_calories = elf_calorie_calculation()
    print(top_elf_calories(list_calories))
    print(top_3_elf_caloreis(list_calories))
