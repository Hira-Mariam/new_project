import sys
from src.new_project.logger import logging
from src.new_project.exception import CustomException

if __name__=="__main__":
    logging.info("The execution has started")

try:
    #data_ingestion=data_Ingestion.
    a=10

except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e,sys)

from src.new_project import utils
df=utils.read_sql_data()
print(df)