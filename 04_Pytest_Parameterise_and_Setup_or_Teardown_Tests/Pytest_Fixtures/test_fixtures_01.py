import pytest
import math


@pytest.fixture()
def setup_list():
    """
    Fixture that provides a list of city names.
    This fixture runs before each test that uses it.
    """
    print("\nSetting up city list fixture...\n")
    cities = ["NY", "LDN", "RDH", "SING", "MUM"]
    return cities


def test_getItem_01(setup_list):
    """
    Verify list slicing and first element access.
    """
    print(setup_list[1:3])
    assert setup_list[0] == "NY"


def test_getItem_02(setup_list):
    """
    Verify slicing with step value.
    """
    assert setup_list[::2] == ["NY", "RDH", "MUM"]


def myReverse(lst):
    """
    Reverse a list in place and return it.
    """
    lst.reverse()
    return lst


def test_reverseList(setup_list):
    """
    Validate reverse slicing and custom reverse function.
    """
    assert setup_list[::-2] == ["MUM", "RDH", "NY"]
    assert setup_list[::-1] == myReverse(setup_list)


@pytest.mark.xfail(
    reason="Known limitation: usefixtures does not provide access to fixture return values"
)
@pytest.mark.usefixtures("setup_list")
def test_usefixtures():
    """
    Demonstrates that @usefixtures executes the fixture
    but does NOT allow access to its returned value.
    """
    assert 1 == 1
    # setup_list is NOT available here
