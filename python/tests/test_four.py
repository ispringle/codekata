from codekata import four


def test_weather():
    mod = four.WeatherMunger()
    assert '14' == mod.solve()

def test_football():
    mod = four.FootballMunger()
    assert 'Leicester' == mod.solve()
