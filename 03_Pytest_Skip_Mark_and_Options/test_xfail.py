import sys
import pytest

def test_strjoin():
    """
    Validate string joining using space and comma separators.
    """
    s1 = "Python,Pytest and Automation"

    l1 = ["Python,Pytest", "and", "Automation"]
    assert s1 == " ".join(l1)

    l2 = ["Python", "Pytest and Automation"]
    assert s1 == ",".join(l2)


@pytest.mark.xfail(
    raises=IndexError,
    reason="Expected failure: index out of range access"
)
def test_str_04():
    """
    Demonstrates IndexError when accessing
    a string index beyond its length.
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert letters[10]


@pytest.mark.xfail(
    sys.platform == "win32",
    reason="Known issue on Windows: string and integer concatenation"
)
def test_str_05():
    """
    Demonstrates TypeError when attempting to
    concatenate a string with an integer.
    """
    letters = "abcd"
    num = 1234
    assert letters + num == "abcd1234"
