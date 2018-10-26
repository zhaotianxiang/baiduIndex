import utils
import time
from element import BasePageElement
from locators import LoginPageLocators
from locators import BaiduIndexPageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self, driver, actions):
        self.driver = driver
        self.actions = actions

class BaiduLoginPage(BasePage):
    """百度登录页面类"""
    def openPage(self, url):
        self.driver.get(url)

    def select_manual_log_in(self):
        element = self.driver.find_element(*LoginPageLocators.MANUL_LOGIN_BUTTON)
        element.click()

    def input_user_name(self, userName):
        element = self.driver.find_element(*LoginPageLocators.USER_NAME_TEXT_ARE)
        element.clear()
        element.send_keys(userName)

    def input_user_password(self, userPassword):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_TEXT_ARE)
        element.clear()
        element.send_keys(userPassword)

    def click_submmit_button(self):
        element = self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        element.click()

class BaiduIndexPage(BasePage):
    '''百度指数首页'''
    def openPage(self, url):
        self.driver.get(url)

    def maxWindows(self):
        self.driver.maximize_window()

    def input_search_key(self, key):
        element = self.driver.find_element(*BaiduIndexPageLocators.SEARCH_KEY_INPUT_ARE)
        element.clear()
        element.send_keys(key)

    def input_new_search_key(self, key):
        element = self.driver.find_element(*BaiduIndexPageLocators.SEARCH_KEY_INPUT_NEW)
        element.clear()
        element.send_keys(key)

    def click_submit_button(self):
        element = self.driver.find_element(*BaiduIndexPageLocators.SEARCH_KEY_INPUT_SUBMIT)
        element.click()

    def click_new_submit_button(self):
        element = self.driver.find_element(*BaiduIndexPageLocators.SEARCH_KEY_INPUT_SUBMIT_new)
        element.click()

        #点击日期自定义按钮
    def click_self_define_date(self):
        element = self.driver.find_elements_by_css_selector(".box-toolbar a")[6]
        element.click()

    def click_start_or_end_year(self, index):
        element = self.driver.find_elements_by_css_selector(".selectA.yearA")[index]
        element.click()

    def click_select_one_year(self, year):
        element = self.driver.find_elements_by_css_selector(".selectA.yearA.slided .sltOpt a")[year]
        element.click()

    def click_start_or_end_month(self, index):
        element = self.driver.find_elements_by_css_selector(".selectA.monthA")[index]
        element.click()

    def click_select_one_month(self, month):
        element = self.driver.find_elements_by_css_selector(".selectA.monthA.slided .sltOpt li a")[month]
        element.click()

    # 点击日期提交按钮
    def click_date_submit(self):
        element = self.driver.find_elements_by_css_selector(".button.ml20")[0]
        element.click()

        # 点击平均值按钮
    def click_index_average(self):
        element = self.driver.find_element(*BaiduIndexPageLocators.AVERAGE_INDEX_BUTTON)
        element.click()

    def click_pc_index_button(self):
        element = self.driver.find_element(*BaiduIndexPageLocators.PC_INDEX_BUTTON)
        element.click()

    def click_mobile_index_button(self):
        element = self.driver.find_element(*BaiduIndexPageLocators.MOBILE_INDEX_BUTTON)
        element.click()
    # def page_down(self):
    #     self.actions

    def hoverOnAvgIndex(self, index):
        element = self.driver.find_elements_by_css_selector("#trend rect")[index]
        element_big_rect = self.driver.find_elements_by_css_selector("#trend rect")[index]
        location = element.location
        # self.actions.move_to_element_with_offset(element,element.size['width']/2+10,element.size['height']/2+10)
        self.actions.move_to_element(element)
        # self.actions.drag_and_drop(element_big_rect, element)
        self.actions.perform()
        time.sleep(1)

    def saveThePicture(self, fileName):
        element = self.driver.find_element(*BaiduIndexPageLocators.AVG_INDEX_PICTURE)
        location = element.location
        utils.saveElementAsPicture(element, fileName, self.driver)

    def saveData(self, date, keywords, indexType):
        avg_baidu_index = utils.ocr(keywords+'_'+indexType+'_'+date+'.png')




