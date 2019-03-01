from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import logger
import os
import time
#封装所有页面都公用的方法
logger=logger(logger="BasePage").getlog()
#基类  父类
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    #后退
    def back(self):
        self.driver.back()
    #前进
    def forward(self):
        self.driver.forward()
    # 清除
    def clear(self, *loc):
        el = self.find_element(*loc)
        try:
            el.clear()
            logger.info("清除文本框的内容")
        except Exception as e:
            logger.error("文本框内容清除失败%s" % e)
            self.get_windows_img()
    #传递url
    def open_url(self,url):
        self.driver.get(url)
    #关闭浏览器
    def quit_browser(self):
        self.driver.quit()
#获取截图
    def get_windows_img(self):
        file_path= os.path.dirname(os.path.abspath("."))+"/screenshots/"
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        screen_name = file_path + rq + ".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("有截屏并且保存的路径是/screenshots/")
        except Exception as e:
            self.get_windows_img()
            logger.error("%s截屏失败%e")

    #关闭当前页面
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭并退出浏览器")
        except Exception as e:
            logger.error("退出浏览器，失败%s"%e)
            self.get_windows_img()
    #查找元素
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info("%s找到页面元素%s"%(self,loc))
            return self.driver.find_element(*loc)
        except:
            logger.error("%s页面中没有找到%s元素"%(self,loc))
            self.get_windows_img()
#
    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            logger.info("%s找到页面元素%s"%(self,loc))
            return self.driver.find_elements(*loc)
        except:
            logger.error("%s页面中没有找到%s元素"%(self,loc))
            self.get_windows_img()
    #传递值
    def send_keys(self,text,*loc):
        el=self.find_element(*loc)
        # el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容%s"%text)
        except Exception as e:
            logger.error("输入内容失败%s"%e)
            self.get_windows_img()

    #点击
    def click(self,*loc):
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info("%s元素被点击"%el)
        except Exception as e:
            logger.error("%s元素点击失败"%e)
            self.get_windows_img()
    def iframe(self,n):
        self.driver.switch_to.frame(n)
#激活当前窗口
    def current_window_handle(self):
        window_list = self.driver.current_window_handle
        self.driver.switch_to.window(window_list)

# 激活窗口
    def window_handles(self, i):
        try:
            self.driver.switch_to.window(self.driver.window_handles[i])
            logger.info("激活窗口成功")
        except Exception as e:
            logger.error("激活窗口失败%s" % e)
            self.get_windows_img()
    # def delete(self,*loc):
    #     el = self.find_element(*loc)
    #     try:
    #         el.click()
    #         logger.info("%s元素被删除" % el.text)
    #     except Exception as e:
    #         logger.error("%s元素删除失败" % el.text)
