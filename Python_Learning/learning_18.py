# Testing

# With testing, you try to break things until the function becomes perfect
# A method where individual units of source code of are tested
# Tests are simply another python file
# Most modules have their own test files ~ They are accompanied
# test files dont run in production
# use the module unittest

# First import the file
# Then create a class

# import unittest
# import learning_17


# class Test17(unittest.TestCase):  # Inherit what unittest gives us which is TestCase
#     def test_learning_17(self):  # Always takes self into parameters

#         test_param = 10  # (if this is what is pasted in)

#         # Always takes in the tested parameters
#         result = learning_17.add_5(test_param)

#         # Assert equal =  Make sure the 2 parameters are equal
#         self.assertEqual(result, 15)


# unittest.learning_17()

import unittest
import main


class TestMain(unittest.TestCase):

    def setUp(self):  # setUp Runs before each test
        print("About to runa function")

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'shkshks'
        result = main.do_stuff(test_param)
        # Checks if the result is going to be a value error, which returns True
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        test_param = None
        result = main._stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Number cannot be  0')

    def tearDown(self):  # Runs at the end of every funtion call
        print("Test in finished successfully")


if __name__ == '__main__':  # Makes sure main file is being run
    unittest.main()

# Assertion errors come from the test files.

# isinstance() will return True or False and checks if the error is an instance of the error in the brakets

# When we run this test file we will get two tests that say OK because we have two teste going on.

# Python3 -m unittest ~ Runs all tests from all modules at the same time

# Adding -v (verbose) gives more details about the tests we ran

# You can add comments about the tests using Docstrings ~ Must be on a single line though
