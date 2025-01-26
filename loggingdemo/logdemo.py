import logging


logging.basicConfig(filename="sample.log", level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug("Debug Python Test")
logging.info("Info Python Test")
logging.warning("Warning Python Test")
logging.error("Error Python Test")
logging.critical("Critical Python test")