import pytest

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executed as last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Barath", "Krishna","krishna.com"]


@pytest.fixture(params=[("chrome","Barath","Krsna"),("Firefox","Krsna"), ("IE","ss")])
def crossBrowser(request):
    return request.param

