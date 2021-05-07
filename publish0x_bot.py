from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from bs4 import BeautifulSoup
import urllib.request
import re
from IPython.display import HTML
from PIL import Image
from io import BytesIO
import time
import pytesseract
import pyperclip
import keyboard
import sys
import os
from random import randrange


def slider_main():
    slider = browser.find_element_by_id("tipslider")
    # browser.execute_script('window.scrollBy(0, 5000)')  # x=0, y=500
    browser.execute_script("arguments[0].scrollIntoView();", slider)
    print("Scrolled to tip slider")

    time.sleep(2)
    try:
        slider.click()
    except ElementNotInteractableException:
        print("Element not interactable")
        for remaining in range(300, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("Tip cooldown #2: {:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rChecking for tip slider...            \n")
        slider.click()

    i = 60

    while i > 0:
        slider.send_keys(Keys.ARROW_LEFT)
        i -= 1

    print("Tip Slider moved left")
    print(">happymerchant.jpg")


article_num = 0
ref_link = "?a=WZdP1yqAeK"  # Leave it in to say thanks :)

dir_path = os.path.dirname(os.path.realpath(__file__))
linktxt = "links.txt"
driver_path = "chromedriver.exe"
brave_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

r = urllib.request.urlopen('https://www.publish0x.com/newposts').read()
soup = BeautifulSoup(r, "lxml")
type(soup)

first_time = 1

with open(linktxt, 'a') as f:
    f.truncate(0)
    for link in soup.find_all('a', {'class': "blogname"}):
        f.write(link.get('href') + '\n')
        print(link.get('href'))

with open(linktxt) as f:
    link_list = f.readlines()

option = webdriver.ChromeOptions()
option.binary_location = brave_path

browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
browser.get("https://www.publish0x.com/login")
print("Browser launched")

time.sleep(1)

#username = browser.find_element_by_xpath("/html/body/div[2]/main/div/div[2]/div/form/div[1]/div/input")
#username.send_keys("")
#password = browser.find_element_by_xpath("/html/body/div[2]/main/div/div[2]/div/form/div[2]/div/input")
#password.send_keys("")

input("Press Enter to continue...")

while article_num < 11:
    article_url = "https://www.publish0x.com" + link_list[article_num] + ref_link
    browser.get(article_url)

    if first_time != 1:
        for remaining in range(605, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("Tip cooldown: {:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rChecking for tip slider...            \n")

    try:
        slider_main()
    except:
        time.sleep(120)
        print("Timer not complete")
        slider_main()

    time.sleep(1)

    try:
        tip_button = browser.find_element_by_xpath("/html/body/div[2]/main/div/div[8]/div/div/div/div/div[3]/button")
        tip_button.click()
    except:
        try:
            tip_button = browser.find_element_by_xpath(
                "/html/body/div[2]/main/div/div[8]/div/div[1]/form/div/div[3]/button")
            tip_button.click()
        except:
            tip_button = browser.find_element_by_xpath(
                "/html/body/div[2]/main/div/div[8]/div/div[2]/form/div/div[3]/button")
            tip_button.click()

    print("Tip submitted")

    article_num = article_num + 1

    first_time = 0

    #for remaining in range(600, 0, -1):
    #    sys.stdout.write("\r")
    #    sys.stdout.write("Tip cooldown: {:2d} seconds remaining.".format(remaining))
    #    sys.stdout.flush()
    #    time.sleep(1)







