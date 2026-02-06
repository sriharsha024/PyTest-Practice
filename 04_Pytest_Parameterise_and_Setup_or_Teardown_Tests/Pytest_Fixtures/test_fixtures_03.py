import pytest


def test_delItem(setup01):
    """
    Verify deletion of the last element from the list
    created by the setup01 fixture.
    """
    del setup01[-1]                  # Remove last item from the list
    print("\nUpdated list:", setup01, "\n")

    # Validate that the list matches the original weekdays list
    assert setup01 == pytest.weekdays1


def test_removeItem(setup02):
    """
    Verify removal of a specific element ('THU')
    from the list created by the setup02 fixture.
    """
    print("\nInitial list:", setup02, "\n")

    setup02.remove("THU")             # Remove specific item
    assert setup02 == pytest.weekdays2
