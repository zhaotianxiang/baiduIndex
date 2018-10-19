import utils
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
        print(element)
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

    def click_submit_button(self):
        element = self.driver.find_element(*BaiduIndexPageLocators.SEARCH_KEY_INPUT_SUBMIT)
        element.click()

        #点击日期自定义按钮
    def click_self_define_date(self):
        element = self.driver.find_element(*BaiduIndexPageLocators.SELF_DEFINE_DATE_BUTTON)
        element.click()

    def click_month(self):
        element = self.driver.find_element(*BaiduIndexPageLocators.SELE_DEFINE_DATE_MONTH)
        element.click()

    def click_select_define_month(self):
        element = self.driver.find_element(*BaiduIndexPageLocators.SELECT_MONTH_OCTOBER)
        element.click()

    def click_date_submit(self):
        element = self.driver.find_element(*BaiduIndexPageLocators.SELF_DEFINE_DATE_SUBMIT)
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
        location = element.location
        print(location['x'],location['y'])
        self.actions.move_to_element(element)
        self.actions.click(element)
        self.actions.perform()

    def saveTheResult(self):
        element = self.driver.find_element(*BaiduIndexPageLocators.AVG_INDEX_PICTURE)
        location = element.location
        print("图片元素和位置已经确定啦！")
        print(location['x'],location['y'])
        saveElementAsPicture(element, "../picture/test", self.driver)
