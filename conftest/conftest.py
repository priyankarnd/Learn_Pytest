import pytest

@pytest.fixture
def input_value():
   input = 39
   return input

'''
We can define the fixture functions in this file to make them accessible across multiple test files.

Now, we have the files test_div_by_3_6.py and test_div_by_13.py making use of the fixture
defined in conftest.py. 

The tests will look for fixture in the same file. As the fixture is not found in the file, 
it will check for fixture in conftest.py file. On finding it, the fixture method is invoked 
and the result is returned to the input argument of the test.

'''