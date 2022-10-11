import imp
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import PIL
import os
from PIL import Image
path = r'C:\Users\lenovo\Documents\TextToNarrativeFilms\images\\'


def download_img(word_list):
    
    for word in word_list:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://images.google.com/')
        driver.maximize_window()
        search = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search.send_keys(word)
        search.send_keys(Keys.ENTER)
        time.sleep(10)
        download_path = path + word + ".png"
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').screenshot(download_path)
        time.sleep(2)
        driver.quit()


def convert_images():
    for file in os.listdir(path):
        f_img = path+file
        img = Image.open(f_img)
        img = img.resize((600,300))
        img.save(f_img)
