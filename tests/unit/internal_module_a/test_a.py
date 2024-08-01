from packagename.internal_module_a.a import add, sub, mul, div

def test_add():
    assert add(10, 20) == 30

def test_sub():
    assert sub(20, 10) == 10

def test_mul():
    assert mul(10, 20) == 200

def test_div():
    assert div(20, 10) == 2

