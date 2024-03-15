import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixtureDemo(setup):
        print("I will execute steps in fixtureDemo methods")

    def test_fixtureDemo1(setup):
        print("I will execute steps in fixtureDemo1 methods")

    def test_fixtureDemo2(setup):
        print("I will execute steps in fixtureDemo2 methods")

    def test_fixtureDemo3(setup):
        print("I will execute steps in fixtureDemo3 methods")

    def test_fixtureDemo4(setup):
        print("I will execute steps in fixtureDemo4 methods")