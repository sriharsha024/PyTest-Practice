from utils.ConfigFileParser import ConfigFileParser

# -------------------------------------------------
# Configuration Setup
# -------------------------------------------------

config = ConfigFileParser("prod.ini")


# -------------------------------------------------
# Test Cases
# -------------------------------------------------

def test_get_gmail_url():
    """
    Verify that the Gmail URL is retrieved
    correctly from the production config.
    """
    url = config.get_gmail_url()
    print(url)
    assert url is not None


def test_get_outlook_url():
    """
    Verify that the Outlook URL is retrieved
    correctly from the production config.
    """
    url = config.get_outlook_url()
    print(url)
    assert url is not None
