import csv
from pathlib import Path

# -------------------------------
# File & Directory Configuration
# -------------------------------

DATA_FILE_NAME = "data.csv"      # CSV file name
CONFIG_DIR_NAME = "config"       # Directory where CSV exists

# Get the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Construct full path: <BASE_DIR>/config/data.csv
DATA_FILE_PATH = BASE_DIR / CONFIG_DIR_NAME / DATA_FILE_NAME


# -------------------------------
# Data Reading Function
# -------------------------------

def get_data():
    """
    Reads data from a CSV file and returns it as a list of tuples.
    Skips the header row.
    """

    with open(DATA_FILE_PATH, mode="r", newline="") as file:
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Convert each row to a tuple and store in a list
        data = [tuple(row) for row in reader]

    return data


# -------------------------------
# Function Call (for testing)
# -------------------------------

print(get_data())
