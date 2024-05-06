#This script automates mass image editing using python to enhance and filter photo quality amongst a single or large group of photos

from PIL import Image, ImageEnhance, ImageFilter 
import os 

path = './imgs' # folder for raw image 
pathOut = '/editedImgs'# folder for editied folder 

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).rotate(360)# for b & w use convert('L')  # Image enhancement |
    factor = 1.5                                                                    #                   |
    enhancer = ImageEnhance.Contrast(edit)                                          #                   |
    edit = enhancer.enhance(factor)                                                 #                   |
                                                                                    #                   v
    clean_name = os.path.splitext(filename)[0]
    edit.save (f'.{pathOut}/{clean_name}_edited.jpg')

    


