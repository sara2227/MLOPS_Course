from exception import CustomException
import logging
import sys

if __name__ == '__main__':

    try:
        a = 1/0
    except Exception as e:
        logging.info('Divide by zero')
        raise CustomException(e,sys)