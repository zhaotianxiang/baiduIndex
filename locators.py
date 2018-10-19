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

    SELF_DEFINE_DATE_BUTTON = (By.CLASS_NAME, 'chartselectdiy')
    SELF_DEFINE_DATE_BUTTON2 = (By.CSS_SELECTOR, "#auto_gsid_15 > div:nth-child(2) > div:nth-child(2) > a.chartselectdiy")
    SELE_DEFINE_DATE_MONTH = (By.XPATH, """//*[@id="auto_gsid_16"]/div[2]/span[2]/span[2]/span""")
    # 点击月份是9月
    SELECT_MONTH_OCTOBER = (By.XPATH, """//*[@id="auto_gsid_17"]/ul/li[2]/a[3]""")
    SELF_DEFINE_DATE_SUBMIT = (By.XPATH, """//*[@id="auto_gsid_16"]/div[3]/input[1]""")
    AVERAGE_INDEX_BUTTON = (By.XPATH, """//*[@id="trend-meanline"]/span""")

    ALL_INDEX_BUTTON = (By.CLASS_NAME, "icon-all") 
    PC_INDEX_BUTTON = (By.CLASS_NAME, "icon-pc") 
    MOBILE_INDEX_BUTTON = (By.CLASS_NAME, "icon-wise") 

    AVG_RECT = (By.CSS_SELECTOR, "#trend rect")
    AVG_INDEX_PICTURE = (By.CLASS_NAME, "contentWord")



