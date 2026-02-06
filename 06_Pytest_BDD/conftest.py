from pytest_bdd import given, when, then, parsers

@given(parsers.parse("There are {count:d} fruits"), target_fixture="fruit_data")
def fruit_data(count):
    return {"start": count, "eat": 0}

@when(parsers.parse("I eat {amount:d} fruits"))
def eat_fruits(fruit_data, amount):
    fruit_data["eat"] += amount

@then(parsers.parse("I should have {remaining:d} fruits"))
def remaining_fruits(fruit_data, remaining):
    assert fruit_data["start"] - fruit_data["eat"] == remaining
