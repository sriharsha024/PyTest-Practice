from pytest_bdd import scenarios,scenario, given, when, then
from pathlib import Path
import pytest

# -------------------------------------------------
# Feature file configuration
# -------------------------------------------------

FEATURE_DIR = "MyFeatures"
FEATURE_FILE = "fixtures.feature"

BASE_DIR = Path(__file__).resolve().parent
FEATURE_PATH = BASE_DIR / FEATURE_DIR / FEATURE_FILE

scenarios(FEATURE_PATH)

@pytest.fixture()
def setup_set():
    print("\n In fixture... setup() function.. \n")
    countries={"IND","USA","ENG","AUS"}
    return countries

@given("A datatype set")
def check_set_type(setup_set):
    print("In Background checking set type")
    if not isinstance(setup_set, set):
        pytest.xfail("The type is not set type")

@given("The set is not empty")
def check_set_notempty(setup_set):
    print("In Background checking set not empty")
    if len(setup_set)==0:
        pytest.xfail("The set of elems is empty")

@given("A set with 3 elements",target_fixture="setup_set1")
def set_of_elems(setup_set):
    print(setup_set)
    if len(setup_set)==0:
        pytest.xfail("The set of elems is empty")
    elif len(setup_set)>3:
        while(len(setup_set)>3):
            setup_set.pop()
    return setup_set
@when("Add 2 elements to the set")
def add_elems(setup_set1):
    setup_set1.add("SA")
    setup_set1.add("GER")

@then("The set should have 5 elements")
def final_set_elems(setup_set1):
    print(setup_set1)
    assert len(setup_set1)==5