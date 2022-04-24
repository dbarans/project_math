from mathematics import geometry

class TestKwadrat:
    def test_kwadrat(self):
        assert geometry.kwadrat(5) == 25

class TestProstokat:
    def test_prostokat(self):
        assert geometry.prostokat(5, 6) == 30