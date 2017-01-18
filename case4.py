##############################################################################
## Test Description
##############################################################################
"""
"""
##############################################################################

from utils import *
from testcases.rhsm.rhsmguibase import RHSMGuiBase
from utils.exception.failexception import FailException

class tc_jump_to_correct_windwo(RHSMGuiBase):

    def test_run(self):
        case_name = self.__class__.__name__
        logger.info("========== Begin of Running Test Case %s ==========" % self.__class__.__name__)
        try:
            try:
                self.open_subscription_manager()
                self.click_register_button()
                self.check_checkbox("main-window", "firstboot-activationkey-checkbox")
                self.click_dialog_next_button()
                self.click_button("main-window","btndefaultbutton")
                self.click_dialog_next_button()
                self.check_elemnet_enbale("main-window",txt,"txtinputkey")
                self.assert_(True, case_name)
            except Exception, e:
                logger.error("Test Failed - ERROR Message:" + str(e))
                self.assert_(False, case_name)
        finally:
            self.remove_proxy()
            self.capture_image(case_name)
            self.restore_gui_environment()
            logger.info("========== End of Running Test Case: %s ==========" % case_name)

if __name__ == "__main__":
    unittest.main()
