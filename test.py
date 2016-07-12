__author__ = 'frankyzhou'
from selenium import webdriver
import time

while(1):
    driver = webdriver.PhantomJS()
    driver.get("http://m.weibo.cn/p/231048zh200217")
    time.sleep(3)
    print(driver.title)
    driver.close()