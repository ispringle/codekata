class Day:
    def __init__(self):
        pass

    def solve(self):
        return "This should solve the problem!"


class One(Day):
    pass


class Two(Day):
    pass


class Three(Day):
    pass


class Four(Day):
    pass


class Five(Day):
    pass


days = {
    "1": One,
    "2": Two,
    "3": Three,
    "4": Four,
    "5": Five,
}


def select(day):
    return days[day]
