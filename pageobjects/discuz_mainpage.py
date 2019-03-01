from framework.base import BasePage
from selenium.webdriver.common.by import By
from framework.logger import logger

logger=logger(logger="BasePage").getlog()
class MainPage(BasePage):
    #登录 名 密码  登录按钮
    username_input_loc=(By.CSS_SELECTOR,"#ls_username")
    pwd_input_loc=(By.CSS_SELECTOR,"#ls_password")
    login_button_loc=(By.CSS_SELECTOR,".fastlg_l>button")
    #默认版块
    defaul_link=(By.CSS_SELECTOR,".fl_icn>a")
    #发帖
    send_title=(By.CSS_SELECTOR,"#subject")
    send_detail=(By.CSS_SELECTOR,".pt")
    send_button=(By.CSS_SELECTOR,".pnpost .pnc")
    #回帖
    reply=(By.CSS_SELECTOR,".area .pt")
    reply_button=(By.CSS_SELECTOR,".ptm button")
    exit_button=(By.LINK_TEXT,"退出")#退出
    name=(By.CSS_SELECTOR,".vwmy>a")#判断是否登录
    #删除
    click_tit=(By.CSS_SELECTOR,".num .xi2")
    dele_tit=(By.CSS_SELECTOR,"#modmenu>a")
    # check_box=(By.CSS_SELECTOR,"#threadlisttableid tbody:last-of-type ")
    # delete_link=(By.LINK_TEXT,"删除")
    cencel=(By.CSS_SELECTOR,".o button")
    #管理中心
    manager_center=(By.LINK_TEXT,"管理中心")
    manager_pwd=(By.XPATH,'//input[@name="admin_password"]')
    manager_submit=(By.CSS_SELECTOR,".loginnofloat input")
    manager_name = (By.CSS_SELECTOR, ".uinfo")
    forum_link=(By.LINK_TEXT,"论坛")
    #添加新板块
    add_new=(By.CSS_SELECTOR,".lastboard>a")
    new_name=(By.CSS_SELECTOR,"tr:nth-last-child(1) .board input")
    add_sub=(By.CSS_SELECTOR,"#submit_editsubmit")#添加新版块 提交按钮
    exi=(By.CSS_SELECTOR,".mainhd .uinfo p:first-of-type a")#管理中心  退出
    click_new=(By.CSS_SELECTOR,".fl_row img")#点击版块
    #搜索帖子
    search_haotest=(By.CSS_SELECTOR,".scbar_txt_td #scbar_txt")
    search_btn=(By.CSS_SELECTOR,".scbar_btn_td #scbar_btn")
    haotest_link=(By.CSS_SELECTOR,".pbw a strong font")
    haotest_tit=(By.CSS_SELECTOR,".ts")
    result=(By.CSS_SELECTOR,".ts span")
    #鼠标  发帖按钮  发起投票
    ele=(By.ID,"newspecial")
    ss_vote=(By.CSS_SELECTOR,".poll a")#鼠标悬停时
    sss_vote=(By.CSS_SELECTOR,".mbw li:nth-child(2) a")
    vote_tit=(By.CSS_SELECTOR,".z #subject")
    # area=(By.CSS_SELECTOR,"#e_iframe")
    check_one=(By.CSS_SELECTOR,".sinf div:nth-last-child(2) p:nth-child(1) input")
    check_two = (By.CSS_SELECTOR, ".sinf div:nth-last-child(2) p:nth-child(2) input")
    check_three = (By.CSS_SELECTOR, ".sinf div:nth-last-child(2) p:nth-child(3) input")
    send_vote = (By.CSS_SELECTOR, ".pnpost button:nth-child(2)")
    vote_sub=(By.CSS_SELECTOR,".pcht .pn")
    choose_btn=(By.CSS_SELECTOR,".pslt #option_1")
    s_one=(By.CSS_SELECTOR,".pcht tr:nth-child(1) td label")
    s_two=(By.CSS_SELECTOR,".pcht tr:nth-child(3) td label")
    s_three = (By.CSS_SELECTOR, ".pcht tr:nth-child(5) td label")
    per_one=(By.CSS_SELECTOR,".pcht tr:nth-child(2) td:nth-child(2)")
    per_two=(By.CSS_SELECTOR,".pcht tr:nth-child(4) td:nth-child(2)")
    per_three=(By.CSS_SELECTOR,".pcht tr:nth-child(6) td:nth-child(2)")
    # s=(By.CSS_SELECTOR,".pcht tr td label")
    # p=(By.CSS_SELECTOR,".pcht tr td:nth-child(2) label")
    main_tit=(By.CSS_SELECTOR,".ts span")
    hao_cli=(By.CSS_SELECTOR,".pbw h3 font")

#点击默认版块
    def click_defaul(self):
        try:
            self.click(*self.defaul_link)
            logger.info("成功点击默认版块")
        except Exception as e:
            logger.error("点击默认版块失败%s" % e)
            self.get_windows_img()

#登录
    def login(self,username,pwd):
        try:
            self.send_keys(username,*self.username_input_loc)
            self.send_keys(pwd,*self.pwd_input_loc)
            self.click(*self.login_button_loc)
            logger.info("登录成功")
            return self.find_element(*self.name).text
        except Exception as e:
            logger.error("登录失败%s" % e)
            self.get_windows_img()

#发帖
    def send(self,title,detail):
        try:
            self.click_defaul()
            self.send_keys(title,*self.send_title)
            self.send_keys(detail, *self.send_detail)
            self.click(*self.send_button)
            logger.info("发帖成功")
        except Exception as e:
            logger.error("发帖失败%s" % e)
            self.get_windows_img()

#回帖
    def repl(self,reply):
        try:
            self.send_keys(reply,*self.reply)
            self.click(*self.reply_button)
            logger.info("回帖成功")
        except Exception as e:
            logger.error("回帖失败%s" % e)
            self.get_windows_img()
#退出登录
    def exit(self):
        try:
            self.click(*self.exit_button)
            logger.info("退出登录成功")
        except Exception as e:
            logger.error("退出失败%s" % e)
            self.get_windows_img()
#删除帖子
    def delete(self):
        try:
            self.click_defaul()
            self.click(*self.click_tit)
            # self.window_handles(1)
            self.click(*self.dele_tit)
            self.click(*self.cencel)
            logger.info("删除帖子成功")
        except Exception as e:
            logger.error("删除帖子失败%s" % e)
            self.get_windows_img()
#点击管理中心
    def click_man(self):
        try:
            self.click(*self.manager_center)
            self.window_handles(1)
            logger.info("点击管理中心成功")
        except Exception as e:
            logger.error("点击管理中心失败%s" % e)
            self.get_windows_img()
#管理中心   登录（密码）
    def man_center(self,pwd):
        try:
            self.send_keys(pwd, *self.manager_pwd)
            self.click(*self.manager_submit)
            self.window_handles(1)
            # return self.find_element(*self.manager_name).text
            logger.info("管理中心登录成功")
        except Exception as e:
            logger.error("管理中心登录失败%s" % e)
            self.get_windows_img()
#点击论坛
    def forum(self):
        try:
            self.click(*self.forum_link)
            logger.info("点击论坛成功")
        except Exception as e:
            logger.error("点击论坛失败%s" % e)
            self.get_windows_img()
#添加新版块
    def ad_new(self,new):
        try:
            self.iframe(0)
            self.click(*self.add_new)
            self.clear(*self.new_name)
            self.send_keys(new,*self.new_name)
            self.click(*self.add_sub)
            logger.info("添加新版块成功")
        except Exception as e:
            logger.error("添加新版块失败%s" % e)
            self.get_windows_img()
#退出管理中心
    def ex(self):
        try:
            self.current_window_handle()
            self.click(*self.exi)
            logger.info("退出管理中心成功")
        except Exception as e:
            logger.error("退出管理中心失败%s" % e)
            self.get_windows_img()
#普通用户发帖
    def new_add(self,title,detail):
        try:
            self.click(*self.click_new)
            self.send_keys(title, *self.send_title)
            self.send_keys(detail, *self.send_detail)
            self.click(*self.send_button)
            logger.info("普通用户发帖成功")
        except Exception as e:
            logger.error("普通用户发帖失败%s" % e)
            self.get_windows_img()
#普通用户回帖
    def new_re(self,reply):
        try:
            self.send_keys(reply, *self.reply)
            self.click(*self.reply_button)
            logger.info("普通用户回帖成功")
        except Exception as e:
            logger.error("普通用户回帖失败%s" % e)
            self.get_windows_img()
#搜索haotest
    def search_hao(self,haotest):
        try:
            self.clear(*self.search_haotest)
            self.send_keys(haotest,*self.search_haotest)
            self.click(*self.search_btn)
            self.window_handles(1)
            logger.info("搜索%s成功"%haotest)
        except Exception as e:
            logger.error("普通用户回帖失败%s" % e)
            self.get_windows_img()

    def click_haotest(self):
        try:
            self.click(*self.hao_cli)
            self.window_handles(2)
            logger.info("成功点击搜索出的内容")
        except Exception as e:
            logger.error("点击搜索出的内容失败%s" % e)
            self.get_windows_img()

    def get_haotest_tit(self):
        try:
            res=self.find_element(*self.result).text
            logger.info("成功获取得到的内容")
            return res
        except Exception as e:
            logger.error("获取得到的内容失败%s" % e)
            self.get_windows_img()
#鼠标悬停  点击
    # def chains(self):
    #     ActionChains(self.driver).move_to_element(self.ele).click(self.ss_vote).perform()
    def click_vote(self):
        try:
            self.click(*self.ele)
            self.click(*self.sss_vote)
            logger.info("成功点击发起投票")
        except Exception as e:
            logger.error("点击发起投票失败%s" % e)
            self.get_windows_img()

    def vote(self,tit,deda,dedb,dedc):
        try:
            self.send_keys(tit,*self.vote_tit)
            self.send_keys(deda, *self.check_one)
            self.send_keys(dedb, *self.check_two)
            self.send_keys(dedc, *self.check_three)
            self.click(*self.send_vote)
            self.click(*self.choose_btn)
            self.click(*self.vote_sub)
            logger.info("成功发起投票")
        except Exception as e:
            logger.error("发起投票失败%s" % e)
            self.get_windows_img()

    def get_value(self):
        try:
            # ss_list=self.find_elements(self.s)
            # per_list=self.find_elements(self.p)
            one_s=self.find_element(*self.s_one).text
            two_s=self.find_element(*self.s_two).text
            three_s=self.find_element(*self.s_three).text
            one_per=self.find_element(*self.per_one).text
            two_per=self.find_element(*self.per_two).text
            three_per=self.find_element(*self.per_three).text
            self.s_list = [one_s, two_s, three_s]
            self.per_list = [one_per, two_per, three_per]
            # print("名称%s"%one_s)
            # s_list=[]
            # p_list=[]
            # self.a = self.find_elements(*self.s)
            # self.b = self.find_elements(*self.p)
            # for j in range(0,len(self.a)):
            #     s_list.append(self.a[j].text)
            # for p in range(0,len(self.b)):
            #     p_list.append(self.b[p].text)
            tit=self.find_element(*self.main_tit).text
            print("标题：",tit)
            for i in range(0,len(self.s_list)) :
                print("名称：{}\n比例：{}".format(self.s_list[i],self.per_list[i]))
                logger.info("成功获取标题 名称 比例")
        except Exception as e:
            logger.error("获取标题 名称 比例失败%s" % e)
            self.get_windows_img()