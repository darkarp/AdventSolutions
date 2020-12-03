# Task 1
def task1_naive(password_list):
    pass_valid = 0
    for line in password_list:
        pass_range, letter_check, password = (
            item.strip().replace(":", "") for item in line.split(" "))
        min_letter, max_letter = (int(number)
                                  for number in pass_range.split("-"))
        letter_count = password.count(letter_check)
        if letter_count >= min_letter and letter_count <= max_letter:
            pass_valid += 1
    return pass_valid


# Task 2
def task2_naive(password_list):
    valid_passwords = 0
    for line in password_list:
        pass_range, letter_check, password = (
            item.strip().replace(":", "") for item in line.split(" "))
        min_letter, max_letter = (int(number)
                                  for number in pass_range.split("-"))
        if (password[min_letter-1] == letter_check) ^ (password[max_letter-1] == letter_check):
            valid_passwords += 1
    return valid_passwords


if __name__ == "__main__":
    passwords = [line for line in open("passwords.txt", "r")]
    task1 = task1_naive(passwords)
    task2 = task2_naive(passwords)
    print(task1, task2)
