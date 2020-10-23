import pytest


@pytest.mark.smoke
def test_first(setup):
    a = 3
    b = 4
    print("in smoke mark")
    assert a+1 == b


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")


