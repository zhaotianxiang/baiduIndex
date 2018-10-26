#coding:utf-8
import time
# 储存中间图片的文件夹
INTER_RESULT_FOLDER = "../inter_result_picture/"

# 储存待识别的图片文件夹
IDENTIIFIED_PICTURE_FOLDER = "../identified_picture/"

# 储存最终结果的文件夹
FINAL_RESULT_DIR = "../results/" 

# 储存最终结果的文件名
FINAL_RESULT_FILE_NAME = time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.csv'

# 关键字配置文件在
CONFIG_PATH = "../config/keywords_config.txt"

# 自定义日期的选择
MONTH_START = 0
MONTH_END = 1
YEAR_START = 0
YEAR_END = 1

# 年份定义
YEAR_2011 = 0
YEAR_2012 = 1
YEAR_2013 = 2
YEAR_2014 = 3
YEAR_2015 = 4
YEAR_2016 = 5
YEAR_2017 = 6
YEAR_2018 = 7

# 月份定义
JAN = 0
FEB = 1
MAR = 2
APR = 3
MAY = 4
JUN = 5
JUL = 6
AUG = 7
SEP = 8
OCT = 9
NOV = 10
DEC = 11

cookies ="""[
    {'domain': '.passport.baidu.com', 'expiry': 1799725209.034562, 'httpOnly': True, 'name': 'HOSUPPORT', 'path': '/', 'secure': False, 'value': '1'}, 
    {'domain': '.passport.baidu.com', 'expiry': 1799725220.528062, 'httpOnly': True, 'name': 'HISTORY', 'path': '/', 'secure': False, 'value': '34174b2828f32981f07400ae57299590321653'}, 
    {'domain': '.baidu.com', 'expiry': 1572061208.069166, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': 'D15980DE0B9D4F26159FC15108ACEFF5:FG=1'}, 
    {'domain': '.passport.baidu.com', 'expiry': 1572061208, 'httpOnly': False, 'name': 'Hm_lvt_90056b3f84f90da57dc0f40150f005d5', 'path': '/', 'secure': False, 'value': '1540525209'}, 
    {'domain': '.passport.baidu.com', 'expiry': 1799725220.527493, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': True, 'value': '911b2e0cbf307e1498c3d8afc26e0ffd2cb43301c19b1cac7bc048c29ad35c29'}, 
    {'domain': '.baidu.com', 'expiry': 1799725220.527714, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': False, 'value': 'W51UTEzamZtUVN4SUtIalNqY1FpYjRLNUVpV3pkenpWcE1LMnN-aFQ0bWtHZnBiQVFBQUFBJCQAAAAAAAAAAAEAAACoxLo4zOy0zcjwz-kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKSM0lukjNJbd'}, 
    {'domain': '.passport.baidu.com', 'httpOnly': False, 'name': 'Hm_lpvt_90056b3f84f90da57dc0f40150f005d5', 'path': '/', 'secure': False, 'value': '1540525209'}, 
    {'domain': '.passport.baidu.com', 'expiry': 1799725209.934022, 'httpOnly': True, 'name': 'UBI', 'path': '/', 'secure': False, 'value': 'fi_PncwhpxZ%7ETaKAU8zefnq-t4y4PYX5vNMlvSKFuQrGT31y9arAKwhmQx-xxHRr6jvGRVH1GcIIFmz3EKo'}, 
    {'domain': '.passport.baidu.com', 'expiry': 1799725220.52757, 'httpOnly': True, 'name': 'USERNAMETYPE', 'path': '/', 'secure': False, 'value': '3'}, 
    {'domain': '.passport.baidu.com', 'expiry': 1799725220.527643, 'httpOnly': True, 'name': 'SAVEUSERID', 'path': '/', 'secure': False, 'value': 'b827190fa613a935822fc024dbc750'}, 
    {'domain': '.passport.baidu.com', 'expiry': 1799725220.527829, 'httpOnly': True, 'name': 'PTOKEN', 'path': '/', 'secure': True, 'value': '0e126889d916356a653c911dd7dc8e13'}
]
"""