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
import json

class SearchBaiduIndex():
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('lang=zh_CN.UTF-8')
        self.options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        self.action = ActionChains(self.driver)

    def login(self):
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

    def test_baidu_index(self):
        baidu_index_page = page.BaiduIndexPage(self.driver, self.action)
        baidu_index_page.openPage("https://index.baidu.com/")
        baidu_index_page.input_search_key("start")
        baidu_index_page.click_submit_button()
        baidu_index_page.maxWindows()

        '''
        理想化的函数：
        @param1: 地区:全国, 北京，香港
        @param2: 查询日期:2018-09
        @param3: 查询关键字: 赵丽颖+zhaoliyig

        @output: void 处理过程中将结果转换成csv
        '''
        df = pd.DataFrame(columns=['key_words','date_range','index_type','baidu_index'])
        i = 0
        for keywords in utils.setAllKeywords():
            for date in utils.setAllDate():
                # try:
                    baidu_index_page.input_new_search_key(keywords)
                    baidu_index_page.click_new_submit_button()
                    time.sleep(1)
                    # 开始自定义时间
                    self.inputSelfDefineDate(baidu_index_page, Constant.YEAR_2011, Constant.OCT,  Constant.YEAR_2012, Constant.OCT)
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
                # except Exception as e:
                #     print(keywords+date+"get failed")
                #     print(e)
                #     time.sleep(60*60)
        df.to_csv(Constant.FINAL_RESULT_DIR+Constant.FINAL_RESULT_FILE_NAME,index=False,sep=',')
    
    def inputSelfDefineDate(self, baidu_index_page, startYear, startMonth, endYear, endMonth):
        # 开始自定义时间
        baidu_index_page.click_self_define_date()
        # 选择年份
        baidu_index_page.click_start_or_end_year(Constant.YEAR_START)
        baidu_index_page.click_select_one_year(startYear)
        # 选择结束年份
        baidu_index_page.click_start_or_end_year(Constant.YEAR_END)
        baidu_index_page.click_select_one_year(endYear)
        #选择开始月份
        baidu_index_page.click_start_or_end_month(Constant.MONTH_START)
        baidu_index_page.click_select_one_month(startMonth)
        #选择结束月份
        baidu_index_page.click_start_or_end_month(Constant.MONTH_END)
        baidu_index_page.click_select_one_month(endMonth)
        # 点击提交时间自定义
        baidu_index_page.click_date_submit()

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    # 申请对象
    baiduIndex = SearchBaiduIndex()
    baiduIndex.setUp()
    baiduIndex.login()
    baiduIndex.test_baidu_index()
    baiduIndex.tearDown()