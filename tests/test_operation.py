from src.math_operations import add, subs



def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0


def test_sub():
    assert subs(5,3) ==2
    assert subs( -1,-1)==-2