from selenium import webdriver
from selenium.webdriver.common.by import By

from base_page.base import BasePage


class BaiDug(BasePage):
    input_el = (By.ID, 'kw')
    click_el = (By.XPATH, '//*[@id="su"]')

    url = 'https://www.baidu.com/'

    def input_text(self, wd):
        self.locator(self.input_el).send_keys(wd)

    def click(self):
        self.locator(self.click_el).click()

    def search(self, wd):
        self.open()
        self.input_text(wd)
        self.click()
        self.quit()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    wd = '今日头条'
    sp = BaiDug(driver, BaiDug.url)
    sp.search(wd)
