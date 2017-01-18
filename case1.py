##############################################################################
## Test Description
##############################################################################
"""

"""
##############################################################################

from utils import *
from testcases.rhsm.rhsmguibase import RHSMGuiBase
from utils.exception.failexception import FailException

class tc_register_with_invaild_key(RHSMGuiBase):
    
    def test_run(self):
        case_name = self.__class__.__name__
        logger.info("========== Begin of Running Test Case %s ==========" % case_name)
        try:
            try:
                self.open_subscription_manager()
                self.check_checkbox("main-window, "firstboot-activationkey-checkbox")
                self.click_dialog_next_button()
                self.input_text('main-window', 'firstboot-organization-entry-text', 'ACME_Corporation')
                self.input_text('main-window', 'firstboot-activation-key-text', 'wrong')
                self.click_register_button()
                self.check_window_exist('error-dialog')
                self.assert_(True, case_name)
            except Exception, e:
                logger.error("FAILED - ERROR Message:" + str(e))
                self.assert_(False, case_name)
        finally:
            self.capture_image(case_name)
            self.restore_gui_environment()
            logger.info("========== End of Running Test Case: %s ==========" % case_name)

if __name__ == "__main__":
    unittest.main()
