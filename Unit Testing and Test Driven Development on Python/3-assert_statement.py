
def test_IntAssert():
    assert 1==1

def test_StrAssert():
    assert "str" == "str"

def test_floatAssert():
    assert 1.0 == 1.0

def test_arrayAssert():
    assert [1,2,3] == [1,2,3]

def test_dictAssert():
    assert {"1": 1} == {"1": 1}

"""
=================================================================================== test session starts ===================================================================================
platform linux -- Python 3.8.5, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- /home/barisx/PycharmProjects/pythonProject1/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/barisx/PycharmProjects/pythonProject1/Unit Testing and Test Driven Development on Python
collected 6 items                                                                                                                                                                         

pytest_test.py::test_AssertTrue PASSED
test_file.py::test_IntAssert PASSED
test_file.py::test_StrAssert PASSED
test_file.py::test_floatAssert PASSED
test_file.py::test_arrayAssert PASSED
test_file.py::test_dictAssert PASSED

==================================================================================== 6 passed in 0.01s =================================================
"""

def test_float():
    assert (0.1 + 0.2) == 0.3


"""
test_file.py::test_float FAILED

======================================================================================== FAILURES =========================================================================================
_______________________________________________________________________________________ test_float ________________________________________________________________________________________

    def test_float():
>       assert (0.1 + 0.2) == 0.3
E       assert 0.30000000000000004 == 0.3
E         +0.30000000000000004
E         -0.3

test_file.py:3: AssertionError
================================================================================= short test summary info =================================================================================
FAILED test_file.py::test_float - assert 0.30000000000000004 == 0.3
=============================================================================== 1 failed, 1 passed in 0.02s ====================================================
"""

from pytest import raises


def raisesValueException():
    pass


def test_exception():
    with raises(ValueError):
        raisesValueException()


"""
======================================================================================== FAILURES =========================================================================================
_____________________________________________________________________________________ test_exception ______________________________________________________________________________________

    def test_exception():
        with raises(ValueError):
>           raisesValueException()
E           Failed: DID NOT RAISE <class 'ValueError'>

test_file.py:8: Failed
================================================================================= short test summary info =================================================================================
FAILED test_file.py::test_exception - Failed: DID NOT RAISE <class 'ValueError'>
=============================================================================== 1 failed, 1 passed in 0.02s ====
"""