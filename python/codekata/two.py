class Day:
    def __init__(self):
        pass

    def solve(self, t, a):
        return a.index(t)


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
    def solve(self, t, a):
        def mid(a):
           return len(a) // 2

        def s(t, a, meta_m):
            m = meta_m
            while a:
                print(a, m, meta_m)
                if a[m] == t:
                    return meta_m
                elif m == 0:
                    return -1
                if a[m] > t:
                    a = a[:m]
                    x = mid(a)
                    meta_m -= m - x
                    m = x
                else:
                    a = a[m:]
                    m = mid(a)
                    meta_m += m
            return -1
        m = mid(a)
        return s(t, a, m)


class SortedArray:
    def __init__(self, a_list):
        self.array = sorted(a_list)

    def __getattr__(self, attr):
        if attr == 'length':
            return len(self.array)
        elif attr == 'mid':
            return len(self.array) // 2

    def get(self, index):
        return self.array[index]

    def find(self, target):
        s, m, e = 0, self.mid, self.length
        while s != e:
            m = (e + s) // 2
            if self.get(m) == target:
                return m
            elif self.get(m) > target:
                e = m
            else:
                s = m + 1
        return -1

class Four(Day):
    def solve(self, t, a):
        array = SortedArray(a)
        return array.find(t)


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
