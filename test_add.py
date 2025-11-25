from add import add

def test_add_two_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-2, -6) == -8
