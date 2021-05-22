from PIL import Image
import os



for picture in os.listdir('orig'):
    if picture.endswith('.jpg'):
        img = Image.open(os.path.join('orig',picture))   # 读取图片
        # 也可以寫成img = Image.open('orig/' + picture)
        img = img.convert("L")   # 转化为黑白图片
        img.save(os.path.join('result',picture[:-4] + '_grey.jpg'))   # 存储图片