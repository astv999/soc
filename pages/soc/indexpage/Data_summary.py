from selenium import webdriver
from common.basePage import BasePage




class DataSummary(BasePage):

    log_source_sum = ("xpath",'//h4[@class="module__num J_count_up"]')
    login_message = ("xpath",'//*[@id="session"]/p[1]/text()')
    login_message_close = ("xpath",'//*[@id="cancel"]')



    def close_login_message(self):
        if self.login_message_close:
            self.click(self.login_message_close)








