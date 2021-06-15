class Munger:
    def __init__(self, url):
        import os
        import requests

        file_name = url.split('/')[-1]

        if os.path.isfile(file_name):
            with open(file_name, 'r') as f:
                self.data = f.read()
        else:
            r = requests.get(url)
            with open(file_name, 'w') as f:
                f.write(r.text)
                self.data = r.text

    def extract_data(self, i=0, cond=lambda x: x or False):
        self.extracted = [
            x.split() for x in self.data.splitlines()[i:] if cond(x)
        ]
        return self

    def calculate_diff(self, h, i, j, cond=lambda x: x or False, stripper=''):
        self.diffs = [(x[h],
                       int(x[i].strip(stripper)) - int(x[j].strip(stripper)))
                      for x in self.extracted if cond(x)]
        return self

    def get_min(self):
        from operator import itemgetter
        return min(self.diffs, key=itemgetter(1))

    def solve(self):
        pass


class WeatherMunger(Munger):
    def __init__(self):
        super().__init__('http://codekata.com/data/04/weather.dat')

    def solve(self):
        return self.extract_data(i=2).calculate_diff(
            0, 1, 2, cond=lambda x: x[0] != "mo", stripper="*").get_min()[0]


class FootballMunger(Munger):
    def __init__(self):
        super().__init__('http://codekata.com/data/04/football.dat')

    def solve(self):
        return self.extract_data(i=1,
                                 cond=lambda x: '---' not in x).calculate_diff(
                                     1, 6, 8).get_min()[0]
