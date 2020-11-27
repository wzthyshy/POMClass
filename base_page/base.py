'''
基类  ：在所有页面中，一些公共的执行
    1、打开浏览器
    2、获取URl
    3、定位元素
    4、关闭浏览器
'''
from time import sleep

from selenium import webdriver


class BasePage(object):
    # 构造函数
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # 定位页面元素，后续需要对元素进行操作，所以需要返回值
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 获取url
    def open(self):
        self.driver.get(self.url)

    # 关闭浏览器
    def quit(self):
        sleep(2)
        self.driver.quit()
