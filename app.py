import sys
from src.new_project.logger import logging
from src.new_project.exception import CustomException

if __name__=="main":
    logging.info("The execution has started")

try:
    #data_ingestion=data_Ingestion.
    100/0

except Exception as e:
    logging.info("custom exception")
    raise(CustomException)