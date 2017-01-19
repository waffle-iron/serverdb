import pytest
def test_test():
    """test for making sure the testing platform is working"""
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        test_test()
