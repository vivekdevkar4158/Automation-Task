
import logging
import os


class LogGen():
    @staticmethod
    def loggen():
        # Define the path for the logs directory
        logs_dir = os.path.join(os.path.abspath(os.curdir), 'logs')

        # Create logs directory if it doesn't exist
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        # Define the log file path
        path = os.path.join(logs_dir, 'automation.log')

        # Create a logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # Create file handler for writing logs to a file
        file_handler = logging.FileHandler(path)
        file_handler.setLevel(logging.DEBUG)

        # Create console handler for outputting logs to terminal
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Define log format
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        # Set formatter for both handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger


