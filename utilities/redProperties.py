
import configparser
import os

config = configparser.RawConfigParser()

# Debugging: Print the absolute path being used
config_path = os.path.join(os.path.abspath(os.curdir), 'configurations', 'config.ini')
print(f"Reading Config File from: {config_path}")  # Debugging

config.read(config_path)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('commonInfo', 'baseURL')

    @staticmethod
    def getUseremail():
        return config.get('commonInfo', 'email')

    @staticmethod
    def getPassword():
        return config.get('commonInfo', 'password')

