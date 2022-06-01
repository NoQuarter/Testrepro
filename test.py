import logging

 #Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Test")

print("Go New changes")

