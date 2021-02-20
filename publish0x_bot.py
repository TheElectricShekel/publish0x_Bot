from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
from io import BytesIO
import time
import pytesseract
import pyperclip
import keyboard
import sys
from random import randrange


driver_path = "chromedriver.exe"
brave_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
#option.add_argument("--incognito")
#option.add_argument("--headless")

ref_link = "?a=WZdP1yqAeK"

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
print("Browser launched")

browser.get("https://www.publish0x.com/login")

input("Press Enter to continue...")

time.sleep(1)

timer_count = 0

xpath_1 = "/html/body/div[3]/main/div/div[1]/div["
article_num = 1
xpath_2 = "]/div[2]/a/img"

while timer_count < 10:
    browser.get("https://www.publish0x.com/newposts")
    print("Navigated to New Posts")

    while article_num < 10:
        try:
            print("Checking for ad overlay")
            ad_check = browser.find_element_by_xpath("/html/body/div[5]/span")
            ad_check.click()
            print("Ads closed")
        except NoSuchElementException:
            print("No Ads found")
            #pass

        try:
            article_xpath = xpath_1+str(article_num)+xpath_2
            article = browser.find_element_by_xpath(article_xpath)
            article.click()
            article_click = "Clicked article #"
            print(article_click+str(article_num))

            time.sleep(2)

            url = browser.current_url
            ref_url = url + ref_link
            print("URL amended: "+ref_url)
            browser.get(ref_url)
            time.sleep(2)

        except NoSuchElementException:
            browser.get("https://www.publish0x.com/newposts")
            time.sleep(1)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            view_more = browser.find_element_by_xpath("/html/body/div[3]/main/div/div[2]/div/button")
            view_more.click()

            time.sleep(3)

            article_xpath = xpath_1 + str(article_num) + xpath_2
            article = browser.find_element_by_xpath(article_xpath)
            article.click()
            article_click = "Clicked article #"
            print(article_click + str(article_num))

            time.sleep(2)

            url = browser.current_url
            ref_url = url + ref_link
            print("URL amended: " + ref_url)
            browser.get(ref_url)
            time.sleep(2)

        try:
            slider = browser.find_element_by_xpath("/html/body/div[3]/main/div/div[8]/div/div[1]/form/div/div[2]/input")
            #browser.execute_script('window.scrollBy(0, 5000)')  # x=0, y=500
            browser.execute_script("arguments[0].scrollIntoView();", slider)

            print("Scrolled to tip slider")

            time.sleep(2)

            slider.click()
            i = 60

            while i > 0:
                slider.send_keys(Keys.ARROW_LEFT)
                i -= 1

            print("Tip Slider moved left")
            print(">happymerchant.jpg")

            time.sleep(1)

            tip_button = browser.find_element_by_xpath("/html/body/div[3]/main/div/div[8]/div/div[1]/form/div/div[3]/button")
            tip_button.click()

            print("Tip submitted")
            timer_count = 0

            if article_num > 1:
                articles_read = " articles read"
            else:
                articles_read = " article read"

            print(str(article_num)+articles_read)

            article_num += 1

            print("Waiting for tip reset:")

            for remaining in range(600, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\rComplete!            \n")

        except NoSuchElementException:
            print("Timer found on page")
            print("Next article")
            article_num += 1
            timer_count += 1
            if timer_count == 9:
                time.sleep(600)
            pass

    while article_num >= 10:
        try:
            print("Checking for ad overlay")
            ad_check = browser.find_element_by_xpath("/html/body/div[5]/span")
            ad_check.click()
            print("Ads closed")
        except NoSuchElementException:
            print("No Ads found")
            # pass

        try:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            article_xpath = xpath_1 + str(article_num) + xpath_2
            article = browser.find_element_by_xpath(article_xpath)
            article.click()
            article_click = "Clicked article #"
            print(article_click + str(article_num))

            time.sleep(2)

            url = browser.current_url
            ref_url = url + ref_link
            print("URL amended: " + ref_url)
            browser.get(ref_url)
            time.sleep(2)

        except NoSuchElementException:
            view_more = browser.find_element_by_xpath("/html/body/div[3]/main/div/div[2]/div/button")
            view_more.click()

            time.sleep(3)

            article_xpath = xpath_1 + str(article_num) + xpath_2
            article = browser.find_element_by_xpath(article_xpath)
            article.click()
            article_click = "Clicked article #"
            print(article_click + str(article_num))

            time.sleep(2)

            url = browser.current_url
            ref_url = url + ref_link
            print("URL amended: " + ref_url)
            browser.get(ref_url)
            time.sleep(2)

        try:
            slider = browser.find_element_by_xpath("/html/body/div[3]/main/div/div[8]/div/div[1]/form/div/div[2]/input")
            # browser.execute_script('window.scrollBy(0, 5000)')  # x=0, y=500
            browser.execute_script("arguments[0].scrollIntoView();", slider)

            print("Scrolled to tip slider")

            time.sleep(2)

            slider.click()
            i = 60

            while i > 0:
                slider.send_keys(Keys.ARROW_LEFT)
                i -= 1

            print("Tip Slider moved left")
            print(">happymerchant.jpg")

            time.sleep(1)

            tip_button = browser.find_element_by_xpath(
                "/html/body/div[3]/main/div/div[8]/div/div[1]/form/div/div[3]/button")
            tip_button.click()

            print("Tip submitted")
            timer_count = 0

            if article_num > 1:
                articles_read = " articles read"
            else:
                articles_read = " article read"

            print(str(article_num) + articles_read)

            article_num += 1

            print("Waiting for tip reset:")

            for remaining in range(600, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\rComplete!            \n")

        except NoSuchElementException:
            print("Timer found on page")
            print("Next article")
            article_num += 1
            timer_count += 1
            if timer_count == 9:
                time.sleep(600)
            pass

    #time.sleep(600)

print("Maximum amount of daily tips given")
print("Exit: Success")



