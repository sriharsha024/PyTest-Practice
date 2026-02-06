import pytest
from utils.util import get_data


@pytest.mark.parametrize("a, b, c, d", get_data())
def test_checkdata_fromFile(a, b, c, d):
    """
    Validate data read from external file using
    pytest parameterization.
    """
    print(d)

