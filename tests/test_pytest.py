import pytest
"""test for making sure the testing platform is working"""
def test_test():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        test_test()
