class MealyError(Exception):
    pass


class Mealy(object):
    def __init__(self):
        self.currentState = 'A'

    def join(self):
        if self.currentState == 'A':
            self.currentState = 'B'
            return 0
        if self.currentState == 'D':
            self.currentState = 'A'
            return 6
        if self.currentState == 'F':
            self.currentState = 'F'
            return 9
        raise MealyError("join")

    def lower(self):
        if self.currentState == 'B':
            self.currentState = 'C'
            return 2
        if self.currentState == 'D':
            self.currentState = 'E'
            return 5
        if self.currentState == 'A':
            self.currentState = 'G'
            return 1
        if self.currentState == 'F':
            self.currentState = 'G'
            return 8
        raise MealyError("lower")

    def fill(self):
        if self.currentState == 'C':
            self.currentState = 'D'
            return 4
        if self.currentState == 'B':
            self.currentState = 'F'
            return 3
        if self.currentState == 'E':
            self.currentState = 'F'
            return 7
        raise MealyError("fill")


def main():
    return Mealy()


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()  # ABCDABCDEFFG
    assert o.join() == 0
    assert o.lower() == 2
    assert o.fill() == 4
    assert o.join() == 6
    assert o.join() == 0
    assert o.lower() == 2
    assert o.fill() == 4

    assert o.lower() == 5
    assert o.fill() == 7
    assert o.join() == 9
    assert o.lower() == 8
    o = main()  # ABFG
    assert o.join() == 0
    assert o.fill() == 3
    assert o.lower() == 8
    o = main()  # AG
    assert o.lower() == 1
    raises(lambda: o.fill(), MealyError)
    raises(lambda: o.join(), MealyError)
    raises(lambda: o.lower(), MealyError)
