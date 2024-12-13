#Write a TestCase class with methods for setup(), run(), and teardown(). Create objects of the TestCase class to represent individual test cases.
class TestCase:
    def __init__(self, test):
        self.test = test

    def setup(self):
        print(f"Setting Up {self.test}")

    def run(sefl):
        print(f"Running {sefl.test}")


    def teardown(self):
        print(f"Tearing down {self.test}")

test1 = TestCase("Open Home Page")
test1.setup()
test1.run()
test1.teardown()

#Implement method overriding in a test automation context. Override a method in the child test class to customize the test execution.
class BuyTestCase(TestCase):
    def run(sefl):
        print(print(f"Running Test Buy flow {sefl.test}"))

test2 = BuyTestCase("Amazon")
test2.run()


#Create a multiple inheritance example: Write a class that inherits from multiple parent classes (e.g., BaseTest and a custom mixin class),
# and check how MRO impacts method calls.

class UnitTest:
    def setup(self):
        print("Setting up the test")

    def teardown(self):
        print("Cleaning up the test")

class MyTest:
    def setup(self):
        print("Setting up My Test")

class LoginTest(MyTest, UnitTest):
    def run(self):
        print("Running login test")

test = LoginTest()
test.setup() # Output: Setting up common tasks
test.run() # Output: Running login test
test.teardown() # Output: Cleaning up the tes