import pytest


def pytest_configure():
    """
    Configure global test data at pytest startup.
    These variables can be accessed as pytest.weekdays1 / pytest.weekdays2.
    """
    pytest.weekdays1 = ["MON", "TUE", "WED"]
    pytest.weekdays2 = ["FRI", "SAT", "SUN"]


@pytest.fixture(scope="module")
def setup01():
    """
    Module-scoped fixture that prepares a weekday list
    by adding 'THU'. Cleanup happens after all tests
    in the module are executed.
    """
    wk1 = pytest.weekdays1.copy()
    wk1.append("THU")            # Setup phase (before yield)

    yield wk1                    # Provide data to tests

    print("\nTeardown: setup01 fixture completed (module scope)")
    # Teardown logic can be added here if needed
    # wk1.clear()
    # wk1.pop()


@pytest.fixture(scope="session")
def setup02():
    """
    Function-scoped fixture that inserts 'THU'
    at the beginning of the weekday list.
    """
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, "THU")          # Setup phase

    yield wk2                    # Provide data to tests

    print("\nTeardown: setup02 fixture completed")


@pytest.fixture()
def setup04(request):
    """
    Fixture that demonstrates use of the request object
    to access test context such as module, function, and scope.
    """
    months = getattr(request.module, "months")

    print("\nInside setup04 fixture")
    print("Fixture scope      :", request.scope)
    print("Calling function   :", request.function.__name__)
    print("Calling module     :", request.module.__name__)

    months.append("APR")          # Modify shared module data

    yield months                  # Provide updated data to test


@pytest.fixture()
def setup05():
    """
    Factory fixture that returns different data structures
    based on input argument.
    """
    def get_structure(name):
        if name == "list":
            return [1, 2, 3]
        elif name == "tuple":
            return (1, 3, 4)

    return get_structure
