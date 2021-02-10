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


import pytest

@pytest.fixture(autouse=True)
def setup():
    print("\nSetup")

def test1(setup):
    print("Executing test1!")
    assert True

def test2():
    print("Executing test2!")
    assert True
"""

import pytest

@pytest.fixture()
def setup1():
    print("\nSetup 1")
    yield
    print("\nTeardown 1")

@pytest.fixture()
def setup2(request):
    print("\nSetup 2")

    def teardown_a():
        print("\nTeardown A")

    def teardown_b():
        print("\nTeardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test1(setup1):
    print("Executing test 1")

def test2(setup2):
    print("Executing test 2")

"""Output
pytest_test.py::test_AssertTrue PASSED
test_file.py::test1 
Setup 1
Executing test 1
PASSED
Teardown 1

test_file.py::test2 
Setup 2
Executing test 2
PASSED
Teardown B

Teardown A



"""

import pytest

@pytest.fixture(scope="module", autouse=True)
def setupModule2():
    print("\nSetup Module2")

@pytest.fixture(scope="class", autouse=True)
def setupClass2():
    print("\nSetup Class2")

@pytest.fixture(scope="function", autouse=True)
def setupFunction2():
    print("\nSetup Function2")

class TestClass:
    def test_it(self):
        print("TestIt")
        assert True

    def test_it2(self):
        print("TestIt2")
        assert True

"""Output
pytest_test.py::test_AssertTrue PASSED
test_file.py::TestClass::test_it 
Setup Module2

Setup Class2

Setup Function2
TestIt
PASSED
test_file.py::TestClass::test_it2 
Setup Function2
TestIt2
PASSED

"""

import pytest


@pytest.fixture(params=[1, 2, 3])
def setup(request):
    retVal = request.param
    print("\nSetup! retVal = {}".format(retVal))
    return retVal


def test1(setup):
    print("\nsetup = {}".format(setup))
    assert True


"""Output
test_file.py::test1[1] 
Setup! retVal = 1

setup = 1
PASSED
test_file.py::test1[2] 
Setup! retVal = 2

setup = 2
PASSED
test_file.py::test1[3] 
Setup! retVal = 3

setup = 3
PASSED

"""