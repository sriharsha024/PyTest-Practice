from pytest_bdd import scenarios,scenario, given, when, then
from pathlib import Path
import pytest

# -------------------------------------------------
# Feature file configuration
# -------------------------------------------------

FEATURE_DIR = "MyFeatures"
FEATURE_FILE = "first101.feature"

BASE_DIR = Path(__file__).resolve().parent
FEATURE_PATH = BASE_DIR / FEATURE_DIR / FEATURE_FILE


# -------------------------------------------------
# Global state (simple demo approach)
# -------------------------------------------------

def pytest_configure():
    pytest.AMT = 0


# -------------------------------------------------
# Scenario binding
# -------------------------------------------------

scenarios(FEATURE_PATH)

#@scenario(FEATURE_PATH, "Withdrawal of money")
#def test_withdrawal():
#    print("BDD scenario: Withdrawal of money")
#    pass

#@scenario(FEATURE_PATH,"Removal of items from set")
#def test_removalofItems():
#    pass

# -------------------------------------------------
# Step Definitions
# -------------------------------------------------

@given("The account balance is 100")
def current_balance():
    pytest.AMT = 100


@when("The account holder withdraws 30")
def withdraw_amount():
    pytest.AMT -= 30


@then("The account balance should be 70")
def final_balance():
    assert pytest.AMT == 70

@given("A set of 3 fruits",target_fixture="myset")
def current_fruits():
    myset={"apple","banana","cherry"}
    return myset
@when("We remove a fruit from the set")
def remove_fruit(myset):
    myset.pop()
    print(myset)

@then("The set will have 2 fruits")
def final_set(myset):
    assert len(myset)==2