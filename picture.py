from PIL import Image
import os



for picture in os.listdir('.'):
    if picture.endswith('.jpg'):
        img = Image.open(picture)   # 读取图片
        img = img.convert("L")   # 转化为黑白图片
        img.save(picture[:-4] + "_grey.jpg")   # 存储图片