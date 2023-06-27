import sys
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()      #inthis luine it will shw where there errror has been occcured
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="errror occurd in pyrhon script name [{0}] line number [{1} error message [{2}]]".format()
    file_name,exc_tb.tb_lineno,str(error)

    return error_message


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):    #init is constructor
        super()._init_(error_message)                   #probably inherit the exception class here
        self.error_message=error_message_detail(error_message,error_detail=error_detail)         #cal the function,,inherit the partent exceptionand the error detailv is drgged by thew sys
    
    
    def __str__(self):                    #when we raisev custom exceptiuon it is going to print error messAGE
        return self.error_message
    

       