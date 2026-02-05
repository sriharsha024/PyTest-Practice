import pytest

# ==========================================================
# Pytest assertion examples covering different use cases
# ==========================================================

def test_b1():
    """Test simple comparison"""
    assert 4 < 5


def test_b2():
    """
    Truthy assertion.
    NOTE: assert 0 would FAIL, assert 1 passes.
    """
    assert 1


def test_b3():
    """Test string equality"""
    assert "abcd" == "abcd"


def test_b4():
    """Test arithmetic expression with operator precedence"""
    assert (5 - 1 * 4 / 2) == 3.0


def test_b5():
    """Test divmod() output (quotient, remainder)"""
    assert divmod(14, 5) == (2, 4)


def test_b6():
    """Test substring membership"""
    assert "put" in "Hi Hello put"


def test_b7():
    """Test element membership in a list"""
    assert 5 in [1, 3, 5, 7, 4]


def test_b8():
    """
    Test list comparison (lexicographical order).
    NOTE:
    [1, 3] < [1, 3, 5, 7, 4] → PASS
    [1, 13] < [1, 3, 5, 7, 4] → FAIL
    """
    assert [1, 3] < [1, 3, 5, 7, 4]


def test_b9():
    """Verify ZeroDivisionError is raised"""
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_b10():
    """
    Expecting an Exception.
    This test FAILS because 2 > 2 does NOT raise an exception.
    """
    with pytest.raises(Exception):
        assert 2 > 2


def test_b11():
    """
    Capturing exception information.
    This test FAILS because the assertion passes
    and no exception is raised.
    """
    with pytest.raises(Exception) as exeinfo:
        assert (1, 2, 3) == (1, 2, 3)

    print(exeinfo)


def func_1():
    """Function that intentionally raises a ValueError"""
    raise ValueError("Exception func1 raised... ")


def test_b12():
    """Validate exception message from a function"""
    with pytest.raises(Exception) as exeinfo:
        func_1()

    print(exeinfo)
    assert str(exeinfo.value) == "Exception func1 raised... "
