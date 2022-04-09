from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
from traceback import print_stack
import logging

class TestStatus(SeleniumDriver):

    log = cl.custom_logger(logging.INFO)

    def __init__(self,driver):

        super(TestStatus, self).__init__(driver)
        self.result_list = []

    def set_result(self,result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append('PASS')
                    self.log.info(f'### VERIFICATION SUCCESSFUL {result_message}')
                else:
                    self.result_list.append('FAIL')
                    self.log.error(f'### VERIFICATION FAILED {result_message}')
                    self.screen_shot(result_message)
            else:
                self.result_list.append('FAIL')
                self.log.error(f'### VERIFICATION FAILED {result_message}')
                self.screen_shot(result_message)
        except:
            self.result_list.append('FAIL')
            self.log.error(f'### EXCEPTION OCCURED!!!')
            self.screen_shot(result_message)
            print_stack()

    def mark(self, result, result_message):
        self.set_result(result, result_message)

    def mark_final(self,test_name, result, result_message):
        self.set_result(result, result_message)
        if 'FAIL' in self.result_list:
            self.log.error(f'{test_name} ### TEST FAILED')
            self.result_list.clear()
            assert True == False
        else:
            self.log.info(f'{test_name} ### TEST SUCCESSFUL')
            self.result_list.clear()
            assert True == True