import sys
sys.path.append(r"D:\Modular coding End to end\ml_pipeline_project")
import logging
from src import logger

def error_message_detail(error , error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()   #getting all the infomation
    file_name = exc_tb.tb_frame.f_code.co_filename    #getting file name 
    error_message = "Error occur in python script name [{0}] line number [{1}] and error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    
    )
    return error_message
class CustomException(Exception):
    def __init__(self , error_message , error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message , error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
        logging.info("Custom Exception testing")
        raise CustomException(e , sys)
    
