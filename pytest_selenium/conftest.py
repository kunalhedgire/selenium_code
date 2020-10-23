import pytest


@pytest.fixture(scope="class")
def setup():
    print("This is a setup")
    yield
    print("After yield")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]



