# >>>> pytest -v -s -m "test1 or test3"
"""
collected 4 items / 2 deselected / 2 selected

test_file1.py::test1
Test1!
PASSED
testSubDirectory/test_file3.py::test3
Test3!
PASSED

==================================================================================== warnings summary =====================================================================================
test_file1.py:3
  /home/barisx/PycharmProjects/pythonProject1/Unit Testing and Test Driven Development on Python/test_file1.py:3: PytestUnknownMarkWarning: Unknown pytest.mark.test1 - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/mark.html
    @pytest.mark.test1

test_file2.py:3
  /home/barisx/PycharmProjects/pythonProject1/Unit Testing and Test Driven Development on Python/test_file2.py:3: PytestUnknownMarkWarning: Unknown pytest.mark.test2 - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/mark.html
    @pytest.mark.test2

testSubDirectory/test_file3.py:3
  /home/barisx/PycharmProjects/pythonProject1/Unit Testing and Test Driven Development on Python/testSubDirectory/test_file3.py:3: PytestUnknownMarkWarning: Unknown pytest.mark.test3 - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/mark.html
    @pytest.mark.test3

-- Docs: https://docs.pytest.org/en/stable/warnings.html
======================================================================= 2 passed, 2 deselected, 3 warnings in 0.01s ======================
"""