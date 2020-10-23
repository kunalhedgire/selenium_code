import logging


def test_logging():

    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter('%(asctime)s :%(levelname)s :%(name)s :%(message)s')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    logger.setLevel(logging.INFO)
    logger.debug("This is a debug")
    logger.info("This is a info")
    logger.warning("This is a warning")
    logger.error("This is a error")



