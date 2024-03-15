import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


def test_SecondGreetCreditCard():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
