import pytest


@pytest.fixture()
def setup():
    print("I will be print first")


def test_fixture(setup):
    print("i will be executed last")

