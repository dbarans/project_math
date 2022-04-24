from mathematics import geometry

class TestKwadrat:
    def test_kwadrat(self):
        assert geometry.kwadrat(5) == 25

class TestProstokat:
    def test_prostokat(self):
        assert geometry.prostokat(5, 6) == 30


class TestTrojkat:
    def test_trojkat(self):
        assert geometry.trojkat(5, 6) == 15

class TestKolo:
    def test_trojkat(self):
        assert geometry.kolo(1) == 3.141592653589793
