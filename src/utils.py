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
        image = Image.open(filename)
        number = pytesseract.image_to_string(image)
        print("OCR "+filename+" TO:  "+number)
    except Exception as e:
        print(e)
    return number

def saveElementAsPicture(imgelement, filename, browser):
    scrollY = browser.execute_script("return window.scrollY;")
    x0 = imgelement.location['x'] + 2
    y0 = imgelement.location['y'] - scrollY + 5
    x1 = imgelement.location['x'] + imgelement.size['width'] - 2
    y1 = y0+ imgelement.size['height'] - 11

    # print(x0, y0, x1, y1, scrollY)
    time.sleep(1)
    browser.save_screenshot(Constant.INTER_RESULT_FOLDER+filename+".png")
    picture = Image.open(Constant.INTER_RESULT_FOLDER+filename+".png")
    croped = picture.crop((x0, y0, x1, y1))
    picture.close()

    croped.save(Constant.IDENTIIFIED_PICTURE_FOLDER+filename+".png")
    # print("save the picture")

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
    ret = []
    file =  open(Constant.CONFIG_PATH,'r',encoding='utf8')
    for line in file.readlines():
        line = line.replace("\n","").replace("\ufeff","")
        item = line.split(',')
        ret.append(item[0]+'+'+item[1])
    return ["赵丽颖"]

def setAllDate():
    return ["2018-9"]

