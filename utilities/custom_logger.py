import logging
import inspect


def custom_logger(log_level):
    # Get the name of class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    file_handle = logging.FileHandler('automation.log', mode='a')
    file_handle.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    file_handle.setFormatter(formatter)
    logger.addHandler(file_handle)
    return logger
