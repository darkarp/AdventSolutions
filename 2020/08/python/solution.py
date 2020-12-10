class Interpreter:
    def __init__(self, code: list[str]) -> None:
        self.acc = 0
        self.ip = 0
        self.code = code
        self.jump_table = []
        self.nop_table = []

    def reload_registers(self) -> None:
        self.acc = 0
        self.ip = 0
        self.jump_table = []
        self.nop_table = []

    def interpret(self, instruction: str) -> None:
        operation, number = instruction.split(" ")
        number = int(number)
        if operation == "jmp":
            self.jump_table.append(self.ip)
            self.ip += number-1
        elif operation == "acc":
            self.acc += number
        elif operation == "nop":
            self.nop_table.append(self.ip)

    def run(self) -> None:
        self.reload_registers()
        while self.ip < len(self.code)-1:
            self.interpret(self.code[self.ip])
            self.ip += 1

    def run_until_repeat(self) -> bool:
        self.reload_registers()
        loop_flag = False
        executed = set()
        while not loop_flag and self.ip < len(self.code)-1:
            self.interpret(self.code[self.ip])
            if self.ip in executed:
                loop_flag = True
            executed.add(self.ip)
            self.ip += 1
        return loop_flag

    def identify_corruption(self) -> None:
        if not self.run_until_repeat():
            return print("[-] Code not Corrupted")
        for nop in self.nop_table:
            self.code[nop] = self.code[nop].replace("nop", "jmp")
            loop = self.run_until_repeat()
            if not loop:
                print(f"[+] Fixed on line {nop}: {self.code[nop]}")
            self.code[nop] = self.code[nop].replace("jmp", "nop")
        for jmp in self.jump_table:
            self.code[jmp] = self.code[jmp].replace("jmp", "nop")
            loop = self.run_until_repeat()
            if not loop:
                return print(f"[+] Fixed line {jmp}: {self.code[jmp]}")
            self.code[jmp] = self.code[jmp].replace("nop", "jmp")
        return print("[-] Couldn't find corruption!")


def extract_input(filename: str = "input.txt") -> list[str]:
    return [line.strip() for line in open(filename)]


def find_acc_before_repeat(interpreter: Interpreter) -> int:
    interpreter.run_until_repeat()
    return interpreter.acc


def find_acc_corrupted(interpreter: Interpreter) -> int:
    interpreter.identify_corruption()
    return interpreter.acc


if __name__ == "__main__":
    code = extract_input()
    interpreter = Interpreter(code=code)
    task1 = find_acc_before_repeat(interpreter)
    task2 = find_acc_corrupted(interpreter)
    print(f"{task1=} {task2=}")
