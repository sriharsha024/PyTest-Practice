# ==========================================================
# Pytest class-based test cases
# ==========================================================

class TestMyStuff:
    """Test suite for basic type and string operations"""

    def test_type(self):
        """Verify that the type of integer literal 5 is int"""
        assert type(5) == int

    def test_strs(self):
        """Verify that string upper() converts text to uppercase"""
        assert str.upper("python") == "PYTHON"
