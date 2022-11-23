import pytest

@pytest.fixture(scope='module')
def fixture_code():
    print('To jest nasz kod wykonywany przed testami')
    print('-'*50)
    yield
    print('-'*45)
    print('To jest nasz kod wykonywany po teście, na samym końcu !!!')
    print('-'*45)


@pytest.mark.skip('Podaję powód pominięcia testu')
def test_tc_009_Login_Logout_Testing():
    print('This is out test case code ....')
    print('This is end of my test case....')

@pytest.mark.Regression    
@pytest.mark.Smoke
def test_tc_010_Login_Invalid_Testing(fixture_code):
    print('This is smoke test')
    print('This is end my 10 test')

@pytest.mark.Regression
def test_tc_011_liczby_a_Testing(fixture_code):
    print('This is out 4 test a')
    print('This is end of my 11 test')        

@pytest.mark.Sanity
@pytest.mark.Regression
def test_tc_012_Login_Valid_Testing(fixture_code):
    print('This is sanity test')
    print('This is end my 12 test')    