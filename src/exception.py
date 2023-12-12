import sys
#exception occurs,sys will get info
import logging
def error_messege_deteails(error,error_detail:sys):
    _,_,exe_tb = error_detail.exc_info()
    #exception of whichline,what error
    file_name = exe_tb.tb_frame.f_code.co_filename
    error_messege ="Error occured in python script name [{0}] line number [{1}] error messege [{2}] rror messege".format(
        file_name,exe_tb.tb_lineno,str(error))

    return error_messege 

class Custum_Exception(Exception):
    def __init__(self,error_messege,error_detail:sys):
        super().__init__(error_messege)
        self.error_messege = error_messege_deteails(error_messege,error_detail=error_detail)

    def __str__(self):
        return self.error_messege
    

if __name__ ==  "__main__":

    try:
        s=1/0
    except Exception as e:
        logging.info("not dived")
        raise Custum_Exception(e,sys)

