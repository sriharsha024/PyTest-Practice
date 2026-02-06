from pytest_bdd import scenarios, given, when, then, parsers
from pathlib import Path

# -------------------------------------------------
# Feature binding
# -------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
FEATURE_PATH = BASE_DIR / "MyFeatures" / "parameterize.feature"

scenarios(FEATURE_PATH)

# =================================================
# SCENARIO 1: Check varieties of fruit (SET)
# =================================================

@given(parsers.parse("There are {count:d} varities of fruits"), target_fixture="fruit_set")
def fruit_set(count):
    assert count == 3
    return {"apple", "banana", "cherry"}


@when("We add a same variety of fruit")
def add_same_variety(fruit_set):
    fruit_set.add("apple")


@then("There is a same count of varieties")
def same_count(fruit_set):
    assert len(fruit_set) == 3


@when("if we add a different variety of fruit")
def add_different_variety(fruit_set):
    fruit_set.add("orange")


@then(parsers.parse("The count of varities increases to {count:d}"))
def increased_count(fruit_set, count):
    assert len(fruit_set) == count

