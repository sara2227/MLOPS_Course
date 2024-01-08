import logging
import os 
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs")

if not os.path.exists(logs_path):
    os.mkdir(logs_path)

LOG_FILE_PATH = os.path.join("logs",LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s" ,
    level=logging.INFO,
)

# this part just write for test the logger code
# if __name__ == "__main__":
#     logging.info("Logging has started!")