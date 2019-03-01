import logging
import time
import os
class logger(object):
    def __init__(self,logger):
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath("."))+"/logs/"
        # log_path = os.path.dirname(os.getcwd())+"/logs/"
        log_name=log_path+rq+".log"
        fh=logging.FileHandler(log_name)
        ch=logging.StreamHandler()
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        fh.setLevel(logging.INFO)
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")  # 设置输出格式
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
    def getlog(self):
        return self.logger
