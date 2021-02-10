import pytest

@pytest.mark.test3
def test3():
    print("\nTest3!")
    assert True

# >>>> pytest -v -s testSubDirectory/
"""Output
collected 1 item                                                                                                                                                                          

testSubDirectory/test_file3.py::test3 
Test3!
PASSED

==================================================================================== 1 passed in 0.00s ==================
"""

# >>>>  pytest -v -s -k "test3"
"""
collected 2 items / 1 deselected / 1 selected                                                                                                                                             

testSubDirectory/test_file3.py::test3 
Test3!
PASSED

============================================================================= 1 passed, 1 deselected in 0.01s ===========================
"""

# >>>>  pytest -v -s -k "test2"
"""
=================================================================================== test session starts ===================================================================================
platform linux -- Python 3.8.5, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- /home/barisx/PycharmProjects/pythonProject1/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/barisx/PycharmProjects/pythonProject1/Unit Testing and Test Driven Development on Python
collected 2 items / 2 deselected                                                                                                                                                          

================================================================================== 2 deselected in 0.01s ==================================
"""

# >>>>  pytest -v -s -k "test2 or test3"
"""
platform linux -- Python 3.8.5, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- /home/barisx/PycharmProjects/pythonProject1/venv/bin/python
cachedir: .pytest_cache
rootdir: /home/barisx/PycharmProjects/pythonProject1/Unit Testing and Test Driven Development on Python
collected 2 items / 1 deselected / 1 selected                                                                                                                                             

testSubDirectory/test_file3.py::test3 
Test3!
PASSED

============================================================================= 1 passed, 1 deselected in 0.01s ========================================
"""

