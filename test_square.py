from square import square
def test_positive():
    assert square(2) == 4
def  test_negative_and_zero():
   assert square(-3) == 9
def test_zero():    
    assert square(0) == 0