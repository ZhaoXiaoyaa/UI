from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_mainpage import MainPage
import unittest
# 发表投票帖子
# 进行投票
# 取出投票各个选项的名称以及投票比例
# 取出投票的主题名称
class Discuz_four(BaseTestCase):
    def test_vote(self):
        mainPage = MainPage(self.driver)
        name = mainPage.login("admin", "1393269559")
        if "admin" in name:
            mainPage.click_defaul()
            # mainPage.chains()
            mainPage.click_vote()
            mainPage.vote("宋雪东","真帅","真漂亮","真白")
            mainPage.get_value()

if __name__=="__main__":
    unittest.main(verbosity=2)