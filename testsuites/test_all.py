import unittest
import os
import HTMLTestRunner
#设置报告文件保存路径
cur_path=os.path.dirname(os.path.realpath(__file__))
report_path=os.path.join(cur_path,"report")#在cur_path下创建新目录   report
if not os.path.exists(report_path):#文件是否存在
    os.mkdir(report_path)#创建一个目录
#构造测试套件
test_dir="./"
suite=unittest.TestLoader().discover(test_dir,pattern="test_discuz01.py")#TestSuite类
# suite=unittest.TestSuite()
# suite.addTest(unittest.makeSuite(Discuz))
# suite.addTest(unittest.makeSuite(Discuz_two))
if __name__=="__main__":
    #打开文件，将result写入文件中
    html_report=report_path+r"\result1.html"
    fp=open(html_report,"wb")
    #初始化HTMLTestRunner 实例对象 生成报告
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    # runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
