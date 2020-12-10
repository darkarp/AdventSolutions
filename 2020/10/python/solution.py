def extract_input(filename="outlets.txt"):
    return {int(line.strip()) for line in open(filename)}


def get_count(outlet_list: set, number: int) -> int:
    # Retrieve number of different branches from one number
    count = 0
    for i in outlet_list:
        if i in (number - 1, number-2, number-3):
            count += 1
    return count


def get_first_difference(outlet_list: set, number: int) -> int:
    # Get the difference of next valid number
    if number+1 in outlet_list:
        return 1
    elif number+2 in outlet_list:
        return 2
    elif number+3 in outlet_list:
        return 3
    return 0


def count_differences(outlet_list: set, outlet_charge: int) -> int:
    # Count and return number if differences multipliedself.
    # (number of 1-differences * number of 2-differences)
    pos_tracker = 0
    diff_counter_1 = 0
    diff_counter_3 = 1
    while pos_tracker < outlet_list[-1]:
        diff = get_first_difference(outlet_list, pos_tracker)
        if diff == 1:
            diff_counter_1 += 1
        elif diff == 3:
            diff_counter_3 += 1
        pos_tracker += diff
    return diff_counter_1 * diff_counter_3


def count_arrangements(outlet_list: set, outlet_charge: int):
    # Count total paths based on number of posibilities of each number
    # Credits to Francisco Traquete for heling me out with this one.
    # My previous solution was very time and space inefficient
    diff_dict = {outlet_charge: 1}
    for number in outlet_list:
        diff_dict[number] = 0
        for difference in range(number-3, number):
            if difference in diff_dict:
                diff_dict[number] += diff_dict[difference]
    return diff_dict[outlet_list[-1]]


if __name__ == "__main__":
    outlet_list = sorted(extract_input())
    outlet_charge = 0
    task1 = count_differences(outlet_list, outlet_charge)
    task2 = count_arrangements(outlet_list, outlet_charge)
    print(f"{task1=} {task2=}")
