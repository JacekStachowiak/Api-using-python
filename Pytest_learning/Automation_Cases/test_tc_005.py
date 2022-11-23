import pytest

a = 110

@pytest.mark.Smoke
def test_tc_014_Login_Logout_Testing():
    print('This is out Smoke test')
    print('This is end of my test case....')
    
@pytest.mark.Sanity
def test_tc_015_Login_Invalid_Testing():
    print('This is sanity test')
    print('This is end my 3 test')

@pytest.mark.Sanity
def test_tc_016_liczby_a_Testing():
    print('This is sanity test ')
    print('This is end of my 4 test')        

@pytest.mark.Sanity
def test_tc_017_Login_Valid_Testing():
    print('This is sanity test')
    print('This is end my 5 test')    