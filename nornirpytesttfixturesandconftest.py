Fixtures are functions, which will run before each test function to which it is applied. Fixtures are used to feed some data to the tests such as database connections, URLs to test and some sort of input data. Therefore, instead of running the same code for every test, we can attach fixture function to the tests and it will run and return the data to the test before executing each test.

A function is marked as a fixture by −

@pytest.fixture
A test function can use a fixture by mentioning the fixture name as an input parameter.

Create a file test_div_by_3_6.py and add the below code to it

import pytest

@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
Here, we have a fixture function named input_value, which supplies the input to the tests. To access the fixture function, the tests have to mention the fixture name as input parameter.

Pytest while the test is getting executed, will see the fixture name as input parameter. It then executes the fixture function and the returned value is stored to the input parameter, which can be used by the test.

Execute the test using the following command −

pytest -k divisible -v
The above command will generate the following result −


We can define the fixture functions in this file to make them accessible across multiple test files.

Create a new file conftest.py and add the below code into it −

import pytest

@pytest.fixture
def input_value():
   input = 39
   return input
Edit the test_div_by_3_6.py to remove the fixture function −

import pytest

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
Create a new file test_div_by_13.py −

import pytest

def test_divisible_by_13(input_value):
   assert input_value % 13 == 0
Now, we have the files test_div_by_3_6.py and test_div_by_13.py making use of the fixture defined in conftest.py.

Run the tests by executing the following command −

pytest -k divisible -v
The above command will generate the following result −

test_div_by_13.py::test_divisible_by_13 PASSED
test_div_by_3_6.py::test_divisible_by_3 PASSED
test_div_by_3_6.py::test_divisible_by_6 FAILED
============================================== FAILURES
==============================================
________________________________________ test_divisible_by_6
_________________________________________
input_value = 39
def test_divisible_by_6(input_value):
> assert input_value % 6 == 0
E assert (39 % 6) == 0
test_div_by_3_6.py:7: AssertionError
========================== 1 failed, 2 passed, 6 deselected in 0.09 seconds
==========================
The tests will look for fixture in the same file. As the fixture is not found in the file, it will check for fixture in conftest.py file. On finding it, the fixture method is invoked and the result is returned to the input argument of the test.

You declare a fixture
with the @ pytest.fixture() decorator above the fixture function.
Then you put the fixture function name as an argument in the definition of the test function,
which can now use the fixture without explicitly instantiating the object it returns.Using a fixture,
I can refactor my tests as follows:


test_div_by_3_6.py::test_divisible_by_3 PASSED
test_div_by_3_6.py::test_divisible_by_6 FAILED
============================================== FAILURES
==============================================
________________________________________ test_divisible_by_6
_________________________________________
input_value = 39
def test_divisible_by_6(input_value):
> assert input_value % 6 == 0
E assert (39 % 6) == 0
test_div_by_3_6.py:12: AssertionError
========================== 1 failed, 1 passed, 6 deselected in 0.07 seconds
==========================
However, the approach comes with its own limitation. A fixture function defined inside a test file has a scope within the test file only. We cannot use that fixture in another test file. To make a fixture available to multiple test files, we have to define the fixture function in a file called conftest.py. conftest.py is explained in the next chapter.

import pytest


@pytest.fixture()
def poly():
    return Polynomial([[4, 3], [-2, 1]])


def test_exponents(poly):
    exponents = [term[1] for term in poly.terms]
    valid_exponents = map(lambda x: x == int(x) and x >= 0, exponents)
    assert all(valid_exponents)


def test_derivative_exponents(poly):
    exponents = [term[1] for term in poly.derivative().terms]
    valid_exponents = map(lambda x: x == int(x) and x >= 0, exponents)
    assert all(valid_exponents)


def test_str_leading_minus(poly):
    if len(poly.terms) == 0:
        first_term = 0
    else:
        first_term = poly.terms[0][0]
    assert first_term >= 0 or str(poly).startswith('-')