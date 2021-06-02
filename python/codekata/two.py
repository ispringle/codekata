class Day:
    def __init__(self):
        pass

    def solve(self, t, a):
        pass


class One:
    def solve(self, t, a):
        s, m, e = 0, 0, len(a)
        while s != e:
            m = (e + s) // 2
            if a[m] == t:
                return m
            elif a[m] > t:
                e = m
            else:
                s = m + 1
        return -1


class Two(Day):
    def solve(self, t, a, s=0, e=-1):
        if e == -1: e = len(a) - 1
        if e <= s: return e if a and a[e] == t else -1
        m = (s + e) // 2
        if a[m] > t:
            return self.solve(t, a, s, m - 1)
        elif a[m] < t:
            return self.solve(t, a, m + 1, e)
        else:
            return m


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
