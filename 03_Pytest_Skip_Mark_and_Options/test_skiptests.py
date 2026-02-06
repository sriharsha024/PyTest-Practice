import sys
import pytest

# ==========================================================
# Skip all tests in this module when running on Windows
# ==========================================================
pytestmark = pytest.mark.skipif(
    sys.platform == "Linux",
    reason="Skipped on Linux platform"
)

# Constant used for Celsius → Fahrenheit conversion
CONST = 9 / 5


def cent_to_fah(cent: float = 0) -> float:
    """
    Convert Celsius to Fahrenheit.

    Formula:
        F = (C × 9/5) + 32
    """
    return (cent * CONST) + 32


@pytest.mark.skip(reason="Demonstration of unconditional skip")
def test_case_01():
    """
    Verify that conversion constant is of type float.
    This test is intentionally skipped.
    """
    assert type(CONST) is float


@pytest.mark.skipif(
    sys.version_info > (4, 0),
    reason="Skipped for Python versions above 4.0 (future compatibility check)"
)

def test_case_02():
    """
    Verify default Celsius to Fahrenheit conversion.
    0°C should convert to 32°F.
    """
    assert cent_to_fah() == 32


@pytest.mark.skipif(
    pytest.__version__ == "5.5.0",
    reason="Known issue with pytest version 5.5.0"
)
def test_case_03():
    """
    Verify Celsius to Fahrenheit conversion for 38°C.
    """
    assert cent_to_fah(38) == 100.4
