import inspect
import logging
import inspect

def customlogger(logLevel=logging.DEBUG):
    logger = logging.getLogger(inspect.stack()[1][3]) # [1] means give me the second logger value, [3] means give me the fourth logger value
    #Or
    #logger = logging.getLogger(__file__)
    logger.setLevel(logLevel)

    filehandler=logging.FileHandler("automation.log")
    filehandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)

    return logger
