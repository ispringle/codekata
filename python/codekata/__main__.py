import sys

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
        solution_mod = importlib.import_module(module_dict[day])
    else:
        print("Please ensure a solution module exists for this day.")
        sys.exit()
    solution_mod.select(day).solve()


if __name__ == "__main__":
    main()
