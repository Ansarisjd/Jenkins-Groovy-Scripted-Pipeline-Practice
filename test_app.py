from app import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_with_negative_numbers():
    assert add(-2, -3) == -5
    assert add(-1, -1) == -2
    assert add(-5, 5) == 0    

