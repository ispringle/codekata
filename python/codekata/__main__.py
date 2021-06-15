import sys
import random

module_dict = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "21": "twentyone",
}

HELP_STRING = """
    python codekata {challenge_number} {day}
"""


def main():
    challenge = None
    day = None
    if len(sys.argv) < 3:
        print(HELP_STRING)
        sys.exit()
    else:
        challenge = sys.argv[1]
        day = sys.argv[2]
    if challenge in module_dict:
        import importlib
        solution_mod = importlib.import_module(module_dict[challenge])
    else:
        print("Please ensure a solution module exists for this day.")
        sys.exit()
    print(solution_mod.select(day)().solve(5, [1, 3, 5]))
    print(solution_mod.select(day)().solve(3, [1]))
    print(solution_mod.select(day)().solve(3, []))
    n = random.randint(10, 100)
    t = random.randint(0, n)
    print(t - 1, solution_mod.select(day)().solve(t, list(range(1, n + 1))))


if __name__ == "__main__":
    main()
