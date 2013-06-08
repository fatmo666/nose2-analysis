"""
This module provides decorators that assist the test author to write tests.
"""


def with_setup(setup):
    """
    A decorator that sets the setup method to be executed before the test.

    It currently works only for function test cases.

    :param setup: The method to be executed before the test.
    :type setup: function
    """

    def decorator(testcase):
        testcase.setup = setup

        return testcase

    return decorator
