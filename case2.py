##############################################################################
## Test Description
##############################################################################
"""
"""
##############################################################################

from utils import *
from testcases.rhsm.rhsmguibase import RHSMGuiBase
from utils.exception.failexception import FailException

class tc_facts_update_(RHSMGuiBase):

    def test_run(self):
        case_name = self.__class__.__name__
        logger.info("========== Begin of Running Test Case %s ==========" % self.__class__.__name__)
        try:
            try:
                username = self.get_rhsm_cons("username")
                password = self.get_rhsm_cons("password")
                self.open_subscription_manager()
                self.register_and_autosubscribe_in_gui(username, password) //need to add uuid
                self.click_view_system_facts_menu()
                self.check_hostype_and_isguest_gui_vs_cli()
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
