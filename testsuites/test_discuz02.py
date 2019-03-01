from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_mainpage import MainPage
import unittest
import time
# 管理员用户登录
# 进入默认板块，删除帖子
# 进入版块管理(管理中心--论坛)
# 创建新的版块
# 管理员退出
# 普通用户登录
# 在新的版块下发帖
# 回复帖子
class Discuz_two(BaseTestCase):
    def test_admin(self):
        mainPage=MainPage(self.driver)
        name=mainPage.login("admin","1393269559")
        if "admin" in name:
            mainPage.delete()
            mainPage.click_man()
            # mainPage.exit()
            # mainPage.login("admin", "1393269559")
            mainPage.man_center("1393269559")
            # if "admin" ==mainPage.man_center("1393269559"):
            mainPage.forum()
            mainPage.ad_new("添加")
            mainPage.ex()
            mainPage.exit()
            time.sleep(3)

            nama=mainPage.login("sasa", "1393269559")
            if "sasa" in nama:
                mainPage.new_add("你好","你好啊nihaonihaonihao")
                mainPage.new_re("hellohellohellohello")


if __name__=="__main__":
    unittest.main(verbosity=2)
