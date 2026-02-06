import pytest


# ----------------------------------------
# Fixture parameterization examples
# ----------------------------------------

@pytest.fixture(params=[(3, 4), [3, 5]], ids=["tuple", "list"])
def fixture_01(request):
    """
    Provides either a tuple or a list based on parameterization.
    """
    return request.param


@pytest.fixture(params=["access", "slice", "assign", "len"])
def fixture_02(request):
    """
    Provides different operation types for testing.
    """
    return request.param


def test_fix_param01(fixture_01):
    """
    Verify that fixture_01 returns either a tuple or a list.
    """
    assert type(fixture_01) in (tuple, list)


def test_fix_param02(fixture_01, fixture_02):
    """
    Perform different operations on the fixture data
    based on the provided operation type.
    """
    if fixture_02 == "access":
        assert fixture_01[0]

    elif fixture_02 == "slice":
        assert fixture_01[::-1]

    elif fixture_02 == "assign":
        fixture_01[0] = 99
        assert True

    elif fixture_02 == "len":
        assert len(fixture_01)
