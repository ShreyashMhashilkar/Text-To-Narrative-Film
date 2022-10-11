
import PIL
import os
from PIL import Image
path = r'C:\Users\lenovo\Documents\TextToNarrativeFilms\images\\'

def convert_images(path):

    for file in os.listdir(path):
        f_img = path+file
        img = Image.open(f_img)
        img = img.resize((400,200))
        img.save(f_img)

convert_images(path)