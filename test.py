from axion.chronicle import get_logger

logger = get_logger(__name__)

logger.info("Chronicle initialized.")
logger.warning("Warning test.")
logger.error("Error test.")