import configparser

from pathlib import Path

cfgFile="qa.ini"
cfgFileDirectory="config"

config=configparser.ConfigParser()
# Get the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Construct full path: <BASE_DIR>/config/data.csv
CONFIG_FILE_PATH = BASE_DIR / cfgFileDirectory / cfgFile

config.read(CONFIG_FILE_PATH)

def getGmailUrl():
    return config['gmail']['url']

def getGmailUser():
    return config['gmail']['user']

def getGmailPass():
    return config['gmail']['pass']

