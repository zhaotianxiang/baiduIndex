from selenium.webdriver.common.by import By
# SUBMIT_BUTTON = (By.XPATH, 'TANGRAM__PSP_3__submit')
# SUBMIT_BUTTON = (By.CSS_SELECTOR, 'TANGRAM__PSP_3__submit')
'''
网页元素的查询方法如下所示：

ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
'''

class LoginPageLocators(object):
    MANUL_LOGIN_BUTTON = (By.ID, 'TANGRAM__PSP_3__footerULoginBtn') 
    PASSWORD_TEXT_ARE = (By.ID, 'TANGRAM__PSP_3__password')
    USER_NAME_TEXT_ARE = (By.ID, 'TANGRAM__PSP_3__userName')
    SUBMIT_BUTTON = (By.ID, 'TANGRAM__PSP_3__submit')

class BaiduIndexPageLocators(object):
    SEARCH_KEY_INPUT_ARE = (By.XPATH, """//*[@id="search-input-form"]/input[3]""")
    SEARCH_KEY_INPUT_SUBMIT = (By.XPATH, """//*[@id="home"]/div[2]/div[2]/div/div[1]/div/div[2]/div/span/span""")


    # 百度云指数时间自定义
    SELF_DEFINE_DATE_BUTTON = ".box-toolbar a"

    # 选中年份
    SELECT_YEAR = ".selectA.yearA"

    # 确认年份 0~7 2011~2018
    CONFIRM_YEAR = ".selectA.yearA.slided .sltOpt a"

    # 选中月份
    SELECT_MONTH = ".selectA.monthA"

    # 确认月份 [0]~[11] == 1月~12月
    CONFIRM_MONTH = ".selectA.monthA.slided .sltOpt li a"

    # 自定义月份提交
    SELF_DEFINE_DATE_SUBMIT = ".button.ml20"

    AVERAGE_INDEX_BUTTON = (By.XPATH, """//*[@id="trend-meanline"]/span""")

    ALL_INDEX_BUTTON = (By.CLASS_NAME, "icon-all") 
    PC_INDEX_BUTTON = (By.CLASS_NAME, "icon-pc") 
    MOBILE_INDEX_BUTTON = (By.CLASS_NAME, "icon-wise") 

    AVG_RECT = (By.CSS_SELECTOR, "#trend rect")
    AVG_INDEX_PICTURE = (By.CLASS_NAME, "contentWord")

    SEARCH_KEY_INPUT_NEW = (By.CSS_SELECTOR, "#schword")
    SEARCH_KEY_INPUT_SUBMIT_new = (By.CSS_SELECTOR, "#schsubmit")



