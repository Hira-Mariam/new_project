import pandas as pd
import sys
import pickle
import numpy as np
import pymysql
from src.new_project.logger import logging
from src.new_project.exception import CustomException

def read_sql_data():
    logging.info('Reading SQL database started')
    try:
        mydb = pymysql.connect(
           host='localhost',
            user='root',
            password='*****',
            db='user_db'
         )
        
        logging.info('Connection Established', mydb)
        df = pd.read_sql_query('Select * from data', mydb)
        
        return df
    
    except Exception as ex:
        raise CustomException(ex,sys)