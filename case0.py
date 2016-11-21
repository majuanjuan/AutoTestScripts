from utils import *
from testcases.BASE import BASE
from utils.exception.failexception import FailException

class tc_ID*****(Base):

    def test_run(self):
        case_name = self.__class__.__name__
        logger.info("========== Begin of Running Test Case %s ==========" % case_name)
        try:
           try:
               if self.guiexist('WINDOW1'):
                  self.close_window('WINDOW1')
               cmd = "COMMAND_A"
               (ret,output) = self.runcmd(cmd,"OUTPUT_A")
               if ret == 0:
                   self.close_window('DIALOG')
                   cmd = "COMMAND_B"
                   (retu,output) = self.runcmd(cmd,"COMMAND_A)
                   if retu == 0:
                       self.check_window_exist('DIALOG') 
                       self.click_button('DIALOG','WINDOW_S')
                       self.check_window_exist('WINDOW_G')
                       cmd = "COMMAND_B"
                       (ret,output) = self.runcmd(cmd,"OUTPUT_B")
                       if retur == 0:
                           self.check_window_exist('DIALOG')
                       else:
                           raise FailException("Test Failed")
                   else:
                       raise FailException("Test Failed")
               else:
                   raise FailException("Test Failed")
           
        finally:
            self.capture_image(case_name)
            self.restore_gui_environment()
            logger.info("========== End of Running Test Case: %s ==========" % case_name)

if __name__ == "__main__":
    unittest.main()
