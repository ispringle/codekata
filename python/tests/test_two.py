from codekata import two


class ChallengeTwoTest:
    mod = two.Day()

    def test_one(self):
        assert -1 == self.mod.solve(3, [])

    def test_two(self):
        assert -1 == self.mod.solve(3, [1])

    def test_three(self):
        assert 0 == self.mod.solve(1, [1])

    def test_four(self):
        assert 0 == self.mod.solve(1, [1, 3, 5])

    def test_five(self):
        assert 1 == self.mod.solve(3, [1, 3, 5])

    def test_six(self):
        assert 2 == self.mod.solve(5, [1, 3, 5])

    def test_seven(self):
        assert -1 == self.mod.solve(0, [1, 3, 5])

    def test_eight(self):
        assert -1 == self.mod.solve(2, [1, 3, 5])

    def test_nine(self):
        assert -1 == self.mod.solve(4, [1, 3, 5])

    def test_ten(self):
        assert -1 == self.mod.solve(6, [1, 3, 5])

    def test_eleven(self):
        assert 0 == self.mod.solve(1, [1, 3, 5, 7])

    def test_twelve(self):
        assert 1 == self.mod.solve(3, [1, 3, 5, 7])

    def test_thirteen(self):
        assert 2 == self.mod.solve(5, [1, 3, 5, 7])

    def test_fourteen(self):
        assert 3 == self.mod.solve(7, [1, 3, 5, 7])

    def test_fifteen(self):
        assert -1 == self.mod.solve(0, [1, 3, 5, 7])

    def test_sixteen(self):
        assert -1 == self.mod.solve(2, [1, 3, 5, 7])

    def test_seventeen(self):
        assert -1 == self.mod.solve(4, [1, 3, 5, 7])

    def test_eighteen(self):
        assert -1 == self.mod.solve(6, [1, 3, 5, 7])

    def test_nineteen(self):
        assert -1 == self.mod.solve(8, [1, 3, 5, 7])

    def test_twenty(self):
        import random
        n = random.randint(1000, 100000)
        t = random.randint(0, n)
        assert t - 1 == self.mod.solve(t, list(range(1, n + 1)))


class TestDayOne(ChallengeTwoTest):
    mod = two.One()

class TestDayTwo(ChallengeTwoTest):
    mod = two.Two()

class TestDayThree(ChallengeTwoTest):
    mod = two.Three()

class TestDayFour(ChallengeTwoTest):
    mod = two.Four()
