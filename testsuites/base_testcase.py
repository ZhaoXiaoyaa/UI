import unittest
from selenium import webdriver
# from configparser import ConfigParser
# from framework.logger import  logger
from framework.browser_engine import BrowserEngine
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.be=BrowserEngine()
        self.driver=self.be.open_browser()
    def tearDown(self):
        self.be.quit_browser()

