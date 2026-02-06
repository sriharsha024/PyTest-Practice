import pytest

# Module-level data used by the setup04 fixture
months = ["JAN", "FEB", "MAR"]


def test_checkrequest(setup04):
    """
    Verify that the setup04 fixture modifies the module-level
    months list by adding 'APR'.
    """
    assert "APR" in setup04
    assert len(setup04) == 4


def test_fact_fixture(setup05):
    """
    Validate the factory fixture (setup05) which returns
    different data structures based on input.
    """
    assert type(setup05("list")) is list
    assert type(setup05("tuple")) is tuple
