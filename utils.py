import io

from lxml import etree
from PIL import Image
import time
import pytesseract
import Constant
import cv2

def ocr(filename):
    number = -1
    try:
        image = Image.open(Constant.const.IDENTIIFIED_PICTURE_FOLDER + filename)
        print(image)
        number = pytesseract.image_to_string(image)
        print(number)
    except Exception as e:
        print(e)
    return number

def saveElementAsPicture(imgelement, filename, browser):
    scrollY = browser.execute_script("return window.scrollY;")
    x0 = imgelement.location['x'] + 2
    y0 = imgelement.location['y'] - scrollY + 2
    x1 = imgelement.location['x'] + imgelement.size['width'] - 2
    y1 = imgelement.size['height'] - 2

    print(x0, y0, x1, y1, scrollY)
    time.sleep(2)

    browser.save_screenshot(Constant.const.INTER_RESULT_FOLDER+filename+".png")
    picture = Image.open(Constant.const.INTER_RESULT_FOLDER+filename+".png")
    croped = picture.crop((x0, y0, x1, y1))
    croped.save(Constant.const.IDENTIIFIED_PICTURE_FOLDER+filename+".png")
    print("save the picture")

#二值化算法 这个没啥必要了 因为已经二值化了
def binarizing(img,threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

def setAllKeywords():
    return ["赵丽颖+zhaoliying"]

def setAllDate():
    return ["2018-9"]
