import pytest

a = 110
result = 'Testing'

@pytest.mark.skip('Podaję powód pominięcia testu')
def test_tc_001_Login_Logout_Testing():
    print('This is out test case code ....')
    print('This is end of my test case....')
    

@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc_003_Login_Invalid_Testing():
    print('This is my sanity and regression test')
    print('This is end my 3 test')
    assert result != 'Testing', 'To nie jest Testing'
    
@pytest.mark.skipif(a>100, reason="pierwszy param warunek, drugi param podaję powód pominięcia")
def test_tc_004_liczby_a_Testing():
    print('This is out 4 test a')
    print('This is end of my 4 test')        

@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc_003_Login_Valid_Testing():
    print('This is my sanity and regression test')
    print('This is end my 5 test')    