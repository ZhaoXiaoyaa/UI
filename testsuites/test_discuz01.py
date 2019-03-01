from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_mainpage import MainPage
import unittest
# 用户登录
# 默认板块发帖
# 默认板块回帖
# 用户退出
class Discuz(BaseTestCase):
    def test_login(self):
        mainPage=MainPage(self.driver)
        name=mainPage.login("sas","1393269559")
        if "sasa" in name:
            mainPage.send("Hello","Hello,unittest!")
            mainPage.repl("asdfg")
            mainPage.exit()

if __name__=="__main__":
    unittest.main(verbosity=2)
