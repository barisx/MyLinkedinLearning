class TestClass:
    @classmethod
    def setup_class(cls):
        print("Setup TestClass!")

    @classmethod
    def teardown_class(cls):
        print("Teardown TestClass!")

    def setup_method(self, method):
        if method == self.test1:
            print("Setting up test1!")
        elif method == self.test2:
            print("Setting up test2!")
        else:
            print("Setting up unknown test!")

    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down test1!")
        elif method == self.test2:
            print("\nTearing down test2!")
        else:
            print("\nTearing down unknown test!")

    # def setup_module(module):
    #     print("Setup Module!")
    #
    # def teardown_module(module):
    #     print("Teardown Module")

    # def setup_function(function):
    #     if function == test1:
    #         print("\nSetting up test1!")
    #     elif function == test2:
    #         print("\nSetting up test2!")
    #     else:
    #         print("\nSetting up unkown test!")

    # def teardown_function(function):
    #     if function == test1:
    #         print("Tearing down test1!")
    #     elif function == test2:
    #         print("\nTearing down test2")
    #     else:
    #         print("\nTearing down unknown test!")

    def test1(self):
        print("Executing test1!")

    def test2(self):
        print("Executing test2!")
        assert True


class MyTestClass():
    def test_it(self):
        assert True

    def test_it(self):
        assert True