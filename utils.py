def saveElementAsPicture(imgelement, path, browser):
    # 找到图片坐标
    locations = imgelement.location
    # 跨浏览器兼容
    scroll = browser.execute_script("return window.scrollY;")
    top = locations['y'] - scroll
    # 找到图片大小
    sizes = imgelement.size
    # 构造关键词长度
    add_length = (len(keyword) - 2) * sizes['width'] / 15
    # 构造指数的位置
    rangle = (
    int(locations['x'] + sizes['width'] / 4 + add_length), int(top + sizes['height'] / 2),
    int(locations['x'] + sizes['width'] * 2 / 3), int(top + sizes['height']))
    time.sleep(2)
    # 截取当前浏览器
    browser.save_screenshot(str(path) + ".png")
    # 打开截图切割
    img = Image.open(str(path) + ".png")
    jpg = img.crop(rangle)
    jpg.save(str(path) + ".jpg")
    # 将图片放大一倍
    # 原图大小73.29
    jpgzoom = Image.open(str(path) + ".jpg")
    (x, y) = jpgzoom.size
    x_s = 146
    y_s = 58
    out = jpgzoom.resize((x_s, y_s), Image.ANTIALIAS)
    out.save(path+'big', 'jpg', quality=95)
    print("成功保存了图片")
