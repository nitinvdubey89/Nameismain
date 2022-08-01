##### create a new file viruatl env
### python3 -m venv .
### source  bin/activate
### python3 -m pip install nornir

### python3 -m pip install nornir_scrapli
## python3 -m pip install pytest
## python3 -m pip install pytest-check
## python3 -m pip install allure
## python3 -m pip install pytest-html-reporter



import pytest
from nornir import InitNornir
@pytest.fixture(scope="session", autouse=True)

def pytestnr():
    pytestnr = InitNornir(config_file="config.yaml")
    yield pytestnr
    nr.close_connections()
### disbale nornir logging in the config.yaml file as pytest will also do logging

def test_num():
    assert 3 == 4
#Assertion is a programming concept used while writing a code where the user declares a
# condition to be true using assert statement prior to running the module.
# If the condition is True, the control simply moves to the next line of code.
# In case if it is False the program stops running and returns AssertionError Exception.
#The function of assert statement is the same irrespective of the language in which it is implemented,
# it is a language-independent concept, only the syntax varies with the programming language.
# AssertionError with error_message.
#x = 1
#y = 0
#assert y != 0, "Invalid Operation" # denominator can't be 0
#   print(x / y)
#Traceback (most recent call last):
#  File "/home/bafc2f900d9791144fbf59f477cd4059.py", line 4, in
#    assert y!=0, "Invalid Operation" # denominator can't be 0
#AssertionError: Invalid Operation


test_num()  ## we dont need to call this function while using pytest
#The meaning of an AssertionError is that something happened that the
# developer thought was impossible to happen. So if an AssertionError is ever thrown,
# it is a clear sign of a programming error.

#Traceback (most recent call last):
#  File "C:/Users/Nitin/PycharmProjects/pythonProject/day-18-start-1/venv/nornirPytestunittesting.py", line 15, in <module>
#    test_num()
#  File "C:/Users/Nitin/PycharmProjects/pythonProject/day-18-start-1/venv/nornirPytestunittesting.py", line 14, in test_num
#    assert 3 == 4
#AssertionError