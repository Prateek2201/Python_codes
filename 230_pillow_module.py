# installation of Pillow lib
# chg img extension
# resize img files
# sharpness
# brightness
# color
# contrast
# Image blue, GaussianBlur

from PIL import Image,ImageEnhance,ImageFilter
import os

##img1 = Image.open('cat.jpg')
#img1.save('cat.png')
#img1.show('cat.png')
##MAX_SIZE = (250,250)
##img1.thumbnail(MAX_SIZE)
##img1.save('catsmall.jpg')

##for item in os.listdir():
##    if item.endswith('.jpg'):
##        img1 = Image.open(item)
##        filename,extension = os.path.splitext(item)
##        img1.save(f'{filename}.png')

##img1 = Image.open('cat.jpg')
##enhancer = ImageEnhance.Color(img1)     #Sharpness Brightness, Contrast
##enhancer.enhance(2).save('catedited.jpg')

img1 = Image.open('cat.jpg')
img1.filter(ImageFilter.GaussianBlur(radius=4)).save('catedited.jpg')
