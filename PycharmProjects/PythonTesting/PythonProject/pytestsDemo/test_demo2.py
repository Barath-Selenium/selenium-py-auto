import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"

@pytest.mark.xfail
def test_secondCreditCard():
    a = 5
    b = 10
    assert a+5 == b, "Addition don't match"




