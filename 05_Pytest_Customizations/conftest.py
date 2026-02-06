import pytest
import os

# -------------------------------------------------
# Configuration file paths
# -------------------------------------------------
QA_CONFIG = os.path.join(
    "05_Pytest_Customizations", "qa.prop"
)

PROD_CONFIG = os.path.join(
    "05_Pytest_Customizations", "prod.prop"
)


def pytest_addoption(parser):
    """
    Add a custom command-line option to pytest.

    Usage:
        pytest --cmdopt=QA
        pytest --cmdopt=Prod

    Default value is 'QA' if not provided.
    """
    parser.addoption(
        "--cmdopt",
        default="QA",
    )


@pytest.fixture()
def cmdopt(pytestconfig):
    """
    Fixture that reads the command-line option (--cmdopt)
    and opens the corresponding configuration file.

    This allows environment-specific test execution.
    """
    print("\nInside cmdopt fixture")

    # Read the value passed from command line
    env = pytestconfig.getoption("cmdopt")

    # Choose config file based on environment
    if env.lower() == "prod":
        config_file = PROD_CONFIG
    else:
        config_file = QA_CONFIG

    # Open the selected config file
    f = open(config_file, "r")

    yield f   # Provide file handle to the test

    # Teardown: close the file after test execution
    f.close()
