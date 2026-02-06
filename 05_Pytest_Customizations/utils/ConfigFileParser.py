import configparser
from pathlib import Path


class ConfigFileParser:
    """
    Loads configuration values from an INI file and
    provides helper methods to access email settings.
    """

    CONFIG_DIR = "config"

    def __init__(self, config_file: str = "qa.ini"):
        """
        Initialize the configuration parser.

        :param config_file: Name of the INI file (default: qa.ini)
        """
        self.config_file = config_file

        # Resolve project base directory
        self.base_dir = Path(__file__).resolve().parent.parent

        # Build full path to the config file
        self.config_path = self.base_dir / self.CONFIG_DIR / self.config_file

        # Load configuration
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)

    # -----------------------------
    # Gmail Configuration
    # -----------------------------

    def get_gmail_url(self):
        """Return Gmail service URL."""
        return self.config["gmail"]["url"]

    def get_gmail_user(self):
        """Return Gmail username."""
        return self.config["gmail"]["user"]

    def get_gmail_password(self):
        """Return Gmail password."""
        return self.config["gmail"]["pass"]

    # -----------------------------
    # Outlook Configuration
    # -----------------------------

    def get_outlook_url(self):
        """Return Outlook service URL."""
        return self.config["outlook"]["url"]

    def get_outlook_user(self):
        """Return Outlook username."""
        return self.config["outlook"]["user"]

    def get_outlook_password(self):
        """Return Outlook password."""
        return self.config["outlook"]["pass"]
