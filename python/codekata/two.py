class Day:
    def __init__(self):
        pass


class One:
    def solve(self, target, sorted_array):
        s, m, e = 0, 0, len(sorted_array)
        while s != e:
            m = (e + s) // 2
            if sorted_array[m] == target:
                return m
            elif sorted_array[m] > target:
                e = m
            else:
                s = m + 1
        return -1


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
