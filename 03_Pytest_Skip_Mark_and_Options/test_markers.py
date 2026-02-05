import pytest

# ==========================================================
# Module-level markers
# All tests in this file belong to:
#   - sanity tests
#   - string-related tests
# ==========================================================
pytestmark = [pytest.mark.sanity, pytest.mark.str]


def test_str_01():
    """
    Validate numeric-to-string conversion and
    string concatenation behavior.
    """
    num = 9 / 4
    s1 = "I like " + "pytest automation"

    assert str(num) == "2.25"
    assert s1 == "I like pytest automation"
    assert s1 + str(num) == "I like pytest automation2.25"


@pytest.mark.smoke
def test_str_02():
    """
    Smoke test to verify the total number of
    lowercase English alphabet characters.
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert len(letters) == 26


def test_str_03():
    """
    Verify string indexing by checking
    the first and last characters.
    """
    letters = "abcdefghijklmnopqrstuvwxyz"

    assert letters[0] == "a"
    assert letters[-1] == letters[25] == "z"


def test_strslice():
    """
    Validate different string slicing scenarios:
    full slice, forward slice, negative slice,
    and stepped slice.
    """
    letters = "abcdefghijklmnopqrstuvwxyz"

    assert letters[:] == letters
    assert letters[10:] == "klmnopqrstuvwxyz"
    assert letters[-3:] == "xyz"
    assert letters[:21:5] == "afkpu"


def test_strsplit():
    """
    Verify string splitting using
    whitespace and comma delimiters.
    """
    s1 = "Python,Pytest and Automation"

    assert s1.split() == ["Python,Pytest", "and", "Automation"]
    assert s1.split(",") == ["Python", "Pytest and Automation"]


def test_strjoin():
    """
    Validate string joining using
    space and comma separators.
    """
    s1 = "Python,Pytest and Automation"

    l1 = ["Python,Pytest", "and", "Automation"]
    assert s1 == " ".join(l1)

    l2 = ["Python", "Pytest and Automation"]
    assert s1 == ",".join(l2)
