"""import pytest

@pytest.fixture()
def setup():
    print("\nSetup")

def test1(setup):
    print("Executing test1!")
    assert True

@pytest.mark.usefixtures("setup")
def test2():
    print("Eexecuting test2!")
    assert True
"""

import pytest

@pytest.fixture(autouse=True)
def setup():
    print("\nSetup")

def test1(setup):
    print("Executing test1!")
    assert True

def test2():
    print("Eexecuting test2!")
    assert True