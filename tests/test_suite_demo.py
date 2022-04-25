import unittest
from tests.home.home_test import HomeTests
from tests.home.login_test import LoginTests

## Get all test from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(HomeTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)

## Create a test suite combining all test cases
smoke_test = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
