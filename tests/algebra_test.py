from mathematics import algebra


class TestAdd:
    def test_add(self):
        assert algebra.add(1, 4) == 5
        assert algebra.add(7, 4) == 11
        assert algebra.add(8, 2) == 10


class TestSub:
    def test_add(self):
        assert algebra.sub(1, 4) == -3
        assert algebra.sub(11, 4) == 7
        assert algebra.sub(7, 6) == 1



class TestDiv:
    def test_div(self):
        assert algebra.div(8, 4) == 2
        assert algebra.div(9, -3) == -3
        assert algebra.div(8, 0) == print("dzielenie przez zero")


class TestMul:
    def test_mul(self):
        assert algebra.mul(8, 2) == 16
        assert algebra.mul(9, 4) == 36
        assert algebra.mul(4, 3) == 12
