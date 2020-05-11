#coding=utf-8
'''封装统一登入登入页面类'''
from common.basePage import BasePage
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage(BasePage):

    '''统一登录网址'''
    url = "https://192.168.31.119"

    #账号、密码、登入
    username_input = ('id', 'user')
    password_input = ('id', 'pass')
    login_button = ('xpath', '//button[@class=" J_LoginBtn"]')
    js = "document.querySelector('.J_LoginBtn').click()"
    # group_choose = ('xpath','//p[.="东经科技"]/parent::div/button')
    # driver = webdriver.Chrome()
    # driver.execute_script("arguments[0].style.display='block';",group_choose)


    def login(self,username,pwd):
        '''登陆系统，账号：admin，密码：1qaz@WSX'''
        self.get(self.url)

        self.sendKeys(self.username_input, text=username)
        self.sendKeys(self.password_input, text=pwd)
        self.click(self.login_button)
        self.driver.execute_script(self.js)
        print("1231413123")
        # ActionChains(self.driver).move_to_element(self.group_choose).click(self.group_choose).perform()
        # print("2222222222")
        # self.click(self.group_choose)
        # self.maximize_window()


if __name__ == '__main__':

    driver = webdriver.Chrome()
    lg = LoginPage(driver)
    # js = "document.querySelector('.J_LoginBtn').click()"
    # driver.execute_script(js)
    # jsActionChains(driver).move_to_element(group_choose).click(group_choose).perform()
    lg.login(username="admin", pwd="1qaz@WSX")


