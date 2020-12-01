import time


# Benchmark decorator
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print(f"{method.__name__} {(te - ts) * 1000} ms")
        return result
    return timed

# Task 1


@timeit
def task1_naive(expenses, target_sum):
    # Nested loop solution
    # O(n^2)
    for i in expenses:
        for j in expenses:
            if j + i == target_sum:
                return i * j
    return False


@timeit
def task1_hashtable(expenses, target_sum):
    # Using hashmaps for efficiency
    # O(N)
    hashtable = set()  # create a hashtable
    for expense in expenses:
        check = target_sum-expense
        if check in hashtable:  # check if the missing number is in the table
            # if it is, we got the solution
            return (target_sum-expense) * expense
        hashtable.add(expense)  # if not we add it to the table and continue
    return False


@timeit
def task1_twopointer(expenses, target_sum):
    # Two Pointer Algorithm: from both ends to center
    # This is going to depend on the sorting algorithmsel
    # O(n log n)
    expenses.sort()  # sorts the list so we can use TPA
    i = 0  # left index
    j = len(expenses) - 1  # right index
    while i < j:
        current_sum = expenses[i] + expenses[j]
        if current_sum == target_sum:
            return expenses[i] * expenses[j]
        elif current_sum < target_sum:
            i += 1  # move left index to the right
        else:
            j -= 1  # move right index to the left
    return False


# Task 2

@timeit
def task2_naive(expenses, target_sum):
    # Nested loop solution
    # O(n^3)
    for i in expenses:
        for j in expenses:
            for z in expenses:
                if j + i + z == target_sum:
                    return i * j * z
    return False


@timeit
def task2_hashtable(expenses, target_sum):
    # Hashtable implementation, similar to task1_hasktable
    # O(N^2)
    expenses_len = len(expenses)
    for i in range(expenses_len):
        hashtable = set()
        currents_sum = target_sum - expenses[i]
        for j in range(i+1, expenses_len):
            if currents_sum - expenses[j] in hashtable:
                return expenses[i] * expenses[j] * (currents_sum - expenses[j])
            hashtable.add(expenses[j])


@timeit
def task2_twopointer(expenses, target_sum):
    # Similar to task1_twopointer
    # O(N^2)
    expenses.sort()
    expenses_len = len(expenses)
    for i in range(expenses_len - 1):  # Fixing each number as we use TPA
        l_index = i + 1
        r_index = expenses_len - 1
        while l_index < r_index:
            current_sum = expenses[i] + expenses[l_index] + expenses[r_index]
            if current_sum == target_sum:
                return expenses[i] * expenses[l_index] * expenses[r_index]
            elif current_sum < target_sum:
                l_index += 1
            else:
                r_index -= 1
    return False


if __name__ == "__main__":
    EXPENSES = [int(expense) for expense in open("expenses.txt", "r")]
    TARGET_SUM = 2020
    task1 = task1_hashtable(EXPENSES, TARGET_SUM)
    print(f"Task 1: {task1}")
    task2 = task2_hashtable(EXPENSES, TARGET_SUM)
    print(f"Task 2: {task2}")
