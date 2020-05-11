import time
from allure import MASTER_HELPER as helper
from selenium import webdriver
from pages.soc.loginPage import LoginPage
from pages.soc.indexpage.Data_summary import DataSummary

@helper.feature("首页-数据概要用例合集")
class Test_LogSummary():
    @helper.step("初始化")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.loginpage = LoginPage(self.driver)
        self.datasummarypage = DataSummary(self.driver)

        self.loginpage.login(username="admin", pwd="1qaz@WSX")
        time.sleep(8)

    # @helper.step("判断是否有多台电脑上或者多个浏览器上已经登录")
    # def test_login_lot(self):
    #     if self.datasummarypage.get_text(self.datasummarypage.login_message) == " 用户在多台电脑上或者多个浏览器上已经登录。":
    #         self.datasummarypage.login_message_close()


    @helper.step("查看日志源总数")
    def test_logsum(self):
        assert self.datasummarypage.get_text(self.datasummarypage.log_source_sum) == "5"

    @helper.step("关闭浏览器")
    def teardown_class(self):
        self.datasummarypage.quit()

