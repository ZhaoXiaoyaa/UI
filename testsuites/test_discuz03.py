from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_mainpage import MainPage
import unittest
from ddt import ddt,data,unpack
# 用户登录
# 进行帖子搜索
# 搜索haotest帖子
# 进入搜索的帖子
# 验证帖子标题和期望的一致
# 用户退出

@ddt
class Discuz_three(BaseTestCase):
    @unpack
    def test_search(self):
        mainPage=MainPage(self.driver)
        name=mainPage.login("admin","1393269559")
        if "admin" in name:
            mainPage.search_hao("haotest")
            mainPage.click_haotest()
            result =mainPage.get_haotest_tit()
            self.assertEqual(result,"haotest" , msg=result)
            mainPage.exit()

if __name__=="__main__":
    unittest.main(verbosity=2)