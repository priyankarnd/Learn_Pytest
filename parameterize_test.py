'''
Pass the parameters within pytest by passing multiple inputs

'''

import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])

def test_mult(num,output):
    assert 11 * num == output





