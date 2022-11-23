import pytest

a = 110

@pytest.mark.skip('Podaję powód pominięcia testu')
def test_tc_005_Login_Logout_Testing():
    print('This is out test case code ....')
    print('This is end of my test case....')

@pytest.mark.Smoke
@pytest.mark.Regression
def test_tc_006_Login_Invalid_Testing():
    print('This is my smoke test')
    print('This is end my 3 test')

@pytest.mark.skipif(a>100, reason="pierwszy param warunek, drugi param podaję powód pominięcia")
def test_tc_007_liczby_a_Testing():
    print('This is out 4 test a')
    print('This is end of my 4 test')        

@pytest.mark.Smoke
def test_tc_008_Login_Valid_Testing():
    print('This is my smoke  test')
    print('This is end my 5 test')    