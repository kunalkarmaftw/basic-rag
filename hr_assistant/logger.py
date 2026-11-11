"""Step 0 : Share logger used by every other step.

Every module in this app asks this file for a logger instead of setting up its own. That way all logs (from document loading to final answer) end up in one place, in consistent format.
"""

import logging
import os
from datetime import datetime

#main log directory
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

# One log for every day, named with the time the run started. everytime we start our app, logs will be created. 

#getting today's date
today = datetime.now().strftime("%Y-%m-%d")

#creating a folder for today's date
daily_log_dir = os.path.join(LOGS_DIR, today)
os.makedirs(daily_log_dir, exist_ok=True)

#define the log file inside today's folder
RUN_LOG_FILE = os.path.join(daily_log_dir,"application.log") #writing the logs in the file.

logging.basicConfig( ## this is just going to observe our application.
    level=logging.INFO, ##.info is like just giving the information thats it.
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s", ##%(asctime)s -> printing the time. %(levelname)s -> it tells about the level like info, debug etc. %(name)s -> from which file the info or error is coming.  %(message)s -> what message is coming.
    handlers=[
        logging.FileHandler(RUN_LOG_FILE, mode="a", encoding="utf-8"), ##filehandles -> it can access the particular file like agents.py, llm.py etc. # mode = a means append more, it add new files to existing conten. and "w" is for write mode, it clears existing file content.
        logging.StreamHandler(), # streamhandler -> it will stream the moment something happens
    ]

)

def get_logger(name:str) -> logging.Logger: #the name argument is the name of the file.
    return logging.getLogger(name) #this is will be returning the name of the file.