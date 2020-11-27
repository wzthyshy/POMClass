'''
登陆页面
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from base_page.base import BasePage

'''
    1：页面元素定位
    2：页面元素操作
'''


class LoginPage(BasePage):
    # 获取页面元素

    login_name = (By.XPATH, '//*[@id="loginname"]')
    login_psw = (By.XPATH, '//*[@id="password"]')
    code_el = (By.XPATH, '//*[@id="code"]')
    click_el = (By.XPATH, '//*[@id="to-recover"]')
    # 指定URL
    url = 'http://18h236a233.imwork.net:13257/FHMYSQL/'

    # 对元素操作进行封装
    def input_username(self, un):
        self.locator(self.login_name).send_keys(un)
        sleep(2)

    def input_pwd(self, psd):
        self.locator(self.login_psw).send_keys(psd)
        sleep(2)

    def seccode(self, code):
        self.locator(self.code_el).send_keys(code)
        sleep(2)

    def click(self):
        self.locator(self.click_el).click()

    # 调试
    def login(self, un, psd, code):
        self.open()
        self.input_username(un)
        self.input_pwd(psd)
        self.seccode(code)
        self.click()
        self.quit()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    username = '超级权限'
    psd = '123456'
    code = '0000'
    lp = LoginPage(driver, LoginPage.url)
    lp.login(username, psd, code)
