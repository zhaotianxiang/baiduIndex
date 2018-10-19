import unittest
import time
from selenium import webdriver
import page
from selenium.webdriver.common.action_chains import ActionChains

class SearchBaiduIndex(unittest.TestCase):
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('lang=zh_CN.UTF-8')
        self.options.add_argument('user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=self.options)
        self.action = ActionChains(self.driver)

    def test_login_baidu(self):

        # login
        login_page = page.BaiduLoginPage(self.driver, self.action)
        login_page.openPage("https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F")
        login_page.select_manual_log_in()
        login_page.input_user_name("15951901003")
        login_page.input_user_password("aini1314@xq")
        time.sleep(10)
        login_page.click_submmit_button()
        print("congradulaions, success login!")

        # search
        baidu_index_page = page.BaiduIndexPage(self.driver, self.action)
        baidu_index_page.openPage("https://index.baidu.com/")
        baidu_index_page.input_search_key("赵丽颖")
        baidu_index_page.click_submit_button()

        baidu_index_page.maxWindows()
        baidu_index_page.click_self_define_date()
        baidu_index_page.click_month()
        baidu_index_page.click_select_define_month()
        baidu_index_page.click_date_submit()
        baidu_index_page.click_index_average()
        time.sleep(6)
        baidu_index_page.hoverOnAvgIndex(3)
        # try to display result of picture
        baidu_index_page.hoverOnAvgIndex(4)
        #save the result
        baidu_index_page.saveTheResult()
        time.sleep(10)
        # save result

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()
