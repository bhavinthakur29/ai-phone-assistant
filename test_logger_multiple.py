from axion.chronicle import get_logger


logger1 = get_logger("module_one")
logger2 = get_logger("module_two")


logger1.info("First logger test.")
logger2.info("Second logger test.")