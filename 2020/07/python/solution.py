class Bag:
    class InnerBag:
        def __init__(self, name, number):
            self.name = name
            self.number = number

    def __init__(self, name="Default"):
        self.name = name
        self.content = []

    def update_content(self, bag: InnerBag):
        self.content.append(bag)

    def get_childs(self):
        return self.content

    def get_number_childs(self):
        count = 0
        for child in self.get_childs():
            if child.name != "other":
                count += child.number
        return count


def extract_input(filename="rules.txt"):
    return [line.strip() for line in open(filename)]


def is_int(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def create_bags(rule_list):
    # Creates a list of Bag objects with their children
    bags = []
    for rule in rule_list:
        father, children_raw = (rule.replace("bags", "").replace("bag", "").replace(".", "").strip()
                                for rule in rule.split("contain", 1))
        children_raw = tuple((number, name) for (number, name) in (values.split(" ", 1) for values in (value.strip()
                                                                                                       for value in children_raw.split(","))))
        children = {}
        bag = Bag(name=father)
        for number, name in children_raw:
            if number == "no":
                number = 0
            inner_bag = bag.InnerBag(name=name, number=int(number))
            bag.update_content(inner_bag)
        bags.append(bag)
    return bags


def get_bag(bag_list: list, name):
    # Retrieves bag from bag list from name
    for bag in bag_list:
        if bag.name == name:
            return bag


def count_childs_min(bag_list: list, bag_name: str):
    # Trying to avoid recursion as much as possible because I suck at it.
    visited = set()
    while True:
        prev_len = len(visited)
        for bag in bag_list:
            for child in bag.get_childs():
                if child.name == bag_name or child.name in visited:
                    visited.add(bag.name)
        if len(visited) == prev_len:
            break
    return len(visited)


def count_childs_all(bag_list: list, bag_name: str):
    # Too much of a pain to avoid recursion
    total = 0
    current_bag = get_bag(bag_list, bag_name)

    def expand_child(child):
        return child.number + (child.number *
                               count_childs_all(bag_list, child.name))
    for child in current_bag.get_childs():
        if child.name != "other" and current_bag:
            total += expand_child(child)
    return total


if __name__ == "__main__":
    rules = extract_input()
    bags = create_bags(rules)
    task1 = count_childs_min(bags, "shiny gold")
    task2 = count_childs_all(bags, "shiny gold")
    print(f"{task1=} {task2=}")
