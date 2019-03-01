import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import  logger
import time
logger=logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath("."))
    chrome_driver_path=dir+"/tools/chromedriver.exe"
    ie_driver_path=dir+"/tools/IEDriverServer.exe"
    firefox_driver_path=dir+"/tools/geckodriver.exe"

    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath("."))+"/config/config.ini"
        config.read(file_path)

        browser=config.get("browserType","browsername")
        logger.info("你选择%s浏览器"%browser)
        url=config.get("testServer","URL")
        logger.info("测试的服务链接是%s"%url)
        if browser=="Firefox":
            self.driver=webdriver.Firefox(executable_path=self.firefox_driver_path)
            logger.info("开始火狐浏览器")
        elif browser=="Chrome":
            self.driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("开始Chrome浏览器")
        elif browser=="IE":
            self.driver=webdriver.Ie(self.ie_driver_path)
            logger.info("开始IE浏览器")
        self.driver.get(url)
        logger.info("打开链接%s"%url)
        self.driver.maximize_window()
        logger.info("当前窗口最大化")
        self.driver.implicitly_wait(10)
        logger.info("设置隐式等待时间10秒")
        return self.driver
    def quit_browser(self):
        logger.info("现在关闭退出浏览器")
        time.sleep(10)
        self.driver.quit()

