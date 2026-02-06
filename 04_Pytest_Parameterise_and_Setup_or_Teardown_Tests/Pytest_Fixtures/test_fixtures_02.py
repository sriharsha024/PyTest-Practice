import pytest
import os

# -------------------------------
# Test data
# -------------------------------
weekdays1 = ["MON", "TUE", "WED"]
weekdays2 = ["FRI", "SAT", "SUN"]

filename = r"D:\PYTEST-PRACTICE\04_Pytest_Parameterise_and_Setup_or_Teardown_Tests\Pytest_Fixtures\file1.txt"


# -------------------------------
# Fixture 1: Modify weekday list
# -------------------------------
@pytest.fixture()
def setup01():
    """
    Prepare a weekday list by adding 'THU'.
    Cleanup is performed after the test using teardown logic.
    """
    wk1 = weekdays1.copy()
    wk1.append("THU")          # Setup phase (before yield)

    yield wk1                  # Provide data to the test

    print("\nTeardown: Cleaning up setup01 fixture")
    wk1.pop()                  # Teardown phase (after yield)


# -------------------------------
# Fixture 2: Insert weekday at start
# -------------------------------
@pytest.fixture()
def setup02():
    """
    Prepare a weekday list by inserting 'THU' at the beginning.
    """
    wk2 = weekdays2.copy()
    wk2.insert(0, "THU")       # Setup phase

    yield wk2                  # Provide data to the test

    print("\nTeardown: Completed setup02 fixture")


# -------------------------------
# Fixture 3: File setup and cleanup
# -------------------------------
@pytest.fixture()
def setup03():
    """
    Create a file, write content, and return a file handle.
    The file is removed during teardown.
    """
    with open(filename, "w") as f:
        f.write("Pytest is good")

    f = open(filename, "r+")   # Reopen file for reading
    print("\nSetup: File created and opened")

    yield f                    # Provide file object to the test

    print("\nTeardown: Closing and deleting file")
    f.close()
    os.remove(filename)


# -------------------------------
# Test cases
# -------------------------------
def test_extendList(setup01):
    """
    Verify that extending the weekday list produces
    the correct ordered result.
    """
    setup01.extend(weekdays2)
    assert setup01 == ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]


def test_len(setup01, setup02):
    """
    Validate that combined list lengths match
    when fixtures are applied.
    """
    assert len(weekdays1 + setup02) == len(setup01 + weekdays2)


def test_filetest(setup03):
    """
    Verify file content written during setup.
    """
    assert setup03.readline() == "Pytest is good"
