import inspect
import logging


def custom_logger(logLevel=logging.DEBUG):
    #Gets the name of the class/method rom the where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    #By default, log all messages
    logger.setLevel(logging.DEBUG)

    filehandler = logging.FileHandler('automation.log', mode='a') #changed from filename=f'{logger_name}.log', mode='w'
    filehandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m%d%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)

    return logger