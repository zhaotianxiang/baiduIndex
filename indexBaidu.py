import Constant
import unittest
import logging as log
import time
from selenium import webdriver
import page
from selenium.webdriver.common.action_chains import ActionChains
import utils
import pandas as pd
import numpy as np

class SearchBaiduIndex(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('lang=zh_CN.UTF-8')
        self.options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        self.action = ActionChains(self.driver)

    def test_baidu_index(self):

        # login
        login_page = page.BaiduLoginPage(self.driver, self.action)
        login_page.openPage("https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F")
        login_page.select_manual_log_in()
        login_page.input_user_name("15951901003")
        login_page.input_user_password("aini1314@xq")
        time.sleep(10)
        login_page.click_submmit_button()
        cookies = self.driver.get_cookies()
        print("congradulaions, success login!")

        # search index for beginner
        baidu_index_page = page.BaiduIndexPage(self.driver, self.action)
        baidu_index_page.openPage("https://index.baidu.com/")
        baidu_index_page.input_search_key("start")
        baidu_index_page.click_submit_button()

        '''
        理想化的函数：
        @param1: 地区:全国，北京，香港
        @param2: 查询日期:2018-09
        @param3: 查询关键字: 赵丽颖+zhaoliyig

        @output: void 处理过程中将结果转换成csv
        '''
        df = pd.DataFrame(columns=['key_words','date_range','index_type','baidu_index'])
        i = 0
        for keywords in utils.setAllKeywords():
            for date in utils.setAllDate():
                try:
                    baidu_index_page.input_new_search_key(keywords)
                    baidu_index_page.click_new_submit_button()
                    baidu_index_page.maxWindows()
                    baidu_index_page.click_self_define_date()
                    time.sleep(10)
                    baidu_index_page.click_month()
                    time.sleep(10)
                    baidu_index_page.click_select_define_month()
                    baidu_index_page.click_date_submit()
                    baidu_index_page.click_index_average()

                    for indexType in ["Total","PC","Mobile"]:
                        filename = keywords+'.'+indexType+'.'+date
                        if "PC" == indexType:
                            baidu_index_page.click_pc_index_button()
                        if "Mobile" == indexType:
                            baidu_index_page.click_mobile_index_button()
                        baidu_index_page.hoverOnAvgIndex(3)
                        baidu_index_page.hoverOnAvgIndex(4)
                        baidu_index_page.saveThePicture(filename)
                        time.sleep(1)
                        avg_index = utils.ocr(Constant.IDENTIIFIED_PICTURE_FOLDER+filename+".png").replace(",","")
                        df.loc[i] = [keywords, date, indexType, avg_index]
                        i+=1
                except Exception as e:
                    print(keywords+date+"get failed")
                    print(e)
                    time.sleep(60*60)
        df.to_csv(Constant.FINAL_RESULT_DIR+Constant.FINAL_RESULT_FILE_NAME,index=False,sep=',')
    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()
