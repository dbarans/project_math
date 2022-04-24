from mathematics import algebra


class TestAdd:
    def test_add(self):
        assert algebra.add(1, 4) == 5

class TestSub:
    def test_add(self):
        assert algebra.sub(1, 4) == -3

class TestDiv:
    def test_div(self):
        assert algebra.div(8, 4) == 2

class TestMul:
    def test_mul(self):
        assert algebra.mul(8, 2) == 16