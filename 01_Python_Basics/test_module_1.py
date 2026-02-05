# ==========================================================
# Basic pytest test cases demonstrating arithmetic assertions
# ==========================================================

def test_a1():
    """Test addition operation"""
    assert 5 + 5 == 10


def test_a2():
    """Test integer division and print a success message"""
    print("Testcase Passed ...")
    assert 18 // 5 == 3


def test_a3():
    """Test multiplication operation"""
    assert 5 * 5 == 25


def test_a4():
    """Test exponentiation (power) operation"""
    assert 5 ** 5 == 3125


def test_a5():
    """Test subtraction operation"""
    assert 5 - 5 == 0


def test_a6():
    """Test division operation"""
    assert 5 / 5 == 1


def test_a7():
    """
    Intentional failure using explicit AssertionError.
    Demonstrates how pytest reports custom failure messages.
    """
    if 18 // 5 != 10:
        raise AssertionError("Failed intentionally")


def test_a8():
    """
    Intentional failure using assert statement with message.
    Shows a cleaner way to report assertion failures.
    """
    assert 18 // 5 == 10, "Failed intentionally: 18//5 is not 10"
