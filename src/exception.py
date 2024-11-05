import sys
from src.logger import logging

# Function to get detailed error information
def error_message_detail(error, error_detail: sys):
    # Get the traceback information from the error details
    _, _, exc_tb = error_detail.exc_info()

    # Extract the filename where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a formatted error message with the filename, line number, and error message
    error_message = "error occurred in python script [{0}] line number[{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    # Return the formatted error message
    return error_message


# Custom exception class to handle and provide detailed error information
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call the parent constructor (Exception) with the error message
        super().__init__(error_message)
        
        # Get the detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    # Override the __str__ method to return the custom error message when the exception is printed
    def __str__(self):
        return self.error_message
    
