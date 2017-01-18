from utils import *
from testcases.BASE import BASE
from utils.exception.failexception import FailException

class tc_ID*****(Base):    
    offing_list=[]
    def coveroff(self,on_list):
        for each_item in on_list:
            if isinstance(each_item,list):
                offing_list.extend(each_item)
            else:
                offing_list.append(each_item)
        return offing_list
    
        
    def test_run(self):
        case_name = self.__class__.__name__
        logger.info("========== Begin of Running Test Case %s ==========" % case_name)
        try:
            try:
                username = self.get_rhsm_cons("username")
                password = self.get_rhsm_cons("password")
                self.open_subscription_manager()
                self.register_and_autosubscribe_in_gui(username, password)
                self.click_button("main-window","all-available-subscriptions")
                all_list=self.list_objects("main-window")
                offed_list=coveroff(all_list)
                if 'lblPressUpdatetosearchforsubscription' in off_list:
                    logger.info("========== Success  ==========" % case_name)
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
