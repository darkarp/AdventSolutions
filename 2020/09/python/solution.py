def extract_input(filename="numbers.txt"):
    return [int(line.strip()) for line in open(filename)]


def find_invalid(number_list, preamble):
    for n, number in enumerate(number_list[preamble:]):
        if not find_pair(number, number_list[n:n+preamble]):
            break
    return number


def find_pair(target_sum, number_list):
    s = set()
    for number in number_list:
        check_number = target_sum-number
        if check_number in s:
            return True
        s.add(number)
    return False


def find_set(number, number_list):
    target_sum = 0
    contiguous = 0
    next_index = 0
    current_index = 0
    sum_set = []
    while current_index < len(number_list):
        if number_list[current_index] + target_sum == number:
            contiguous += 1
            for i in range(contiguous):
                sum_set.append(number_list[current_index-i])
            break
        elif number_list[current_index] + target_sum > number:
            next_index += 1
            contiguous = 0
            target_sum = 0
            current_index = next_index
        else:
            target_sum += number_list[current_index]
            contiguous += 1
        current_index += 1
    min_max_sum = min(sum_set) + max(sum_set)
    return min_max_sum


if __name__ == "__main__":
    number_list = extract_input()
    task1 = find_invalid(number_list, 25)
    task2 = find_set(task1, number_list)
    print(f"{task1=} {task2=}")
