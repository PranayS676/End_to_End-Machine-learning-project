import sys
import logging
import traceback

def error_message_details(error):
    exc_type, exc_value, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message[{2}]".format(file_name, line_number, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error):
        super().__init__(str(error))
        self.error_message = error_message_details(error)
    
    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Setup basic logging

    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e)
