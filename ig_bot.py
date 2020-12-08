import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import random


# initialize driver

driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')

def login(username_, password_):
    driver.get('https://www.instagram.com/')

    # accepting the cookies
    try:
        cookies_accept= driver.find_element_by_xpath('//button[text()="Accept"]')
        cookies_accept.click()
        time.sleep(1)
    except:
        pass

    username = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')

    username.click()
    username.send_keys(username_)
    time.sleep(1)

    password.click()
    password.send_keys(password_)
    time.sleep(1)

    log_in=driver.find_element_by_xpath('//div[text()="Log In"]')
    log_in.click()
    time.sleep(4)

    # credential storage
    try:
        credentials= driver.find_element_by_xpath('//button[text()="Not Now"]')
        credentials.click()
        time.sleep(1)
    except:
        pass

    #  notifications
    try:
        notifications = driver.find_element_by_xpath('//button[text()="Not Now"]')
        notifications.click()
        time.sleep(1)
    except:
        pass

def follow_like_comment(number):
    profiles_list=['duck._lover', 'rabbit._lover']
    comments=['so cute!', 'cutie', 'very sweet!', 'nice!', 'love it', 'looks very special']

    for i in range (len(profiles_list)): # 2 pages

        search_1 = driver.find_element_by_xpath('//span[text()="Search"]')
        search_1.click()
        time.sleep(1)

        search_2 = driver.find_element_by_xpath('//input[@placeholder="Search"]')
        search_2.send_keys(profiles_list[i])

        count = 0
        while count <3:
            search_2.send_keys(Keys.ENTER)
            count +=1 # count = count +1
            time.sleep(1)

        # follow
        follow = driver.find_element_by_xpath('//button[text()="Follow"]')
        follow.click()
        time.sleep(2)

        # first media element
        media_element = driver.find_element_by_xpath('//div[@class="eLAPa"]')
        media_element.click()
        time.sleep(2)

        for k in range (number):
            # like
            like = driver.find_element_by_xpath('//button[@class="wpO6b "]//*[@aria-label="Like"]')
            like.click()
            time.sleep(1)
            # comment
            comment_1 = driver.find_element_by_xpath('//div[@class="RxpZH"]')
            comment_1.click()
            time.sleep(1)

            comment_2 = driver.find_element_by_class_name('Ypffh')
            comment_2.send_keys(random.choice(comments))
            time.sleep(1)
            # post
            post = driver.find_element_by_xpath('//button[text()="Post"]')
            post.click()
            time.sleep(1)
            # click on next media element
            next_button = driver.find_element_by_xpath('//a[text()="Next"]')
            next_button.click()
            time.sleep(1)

        close = driver.find_element_by_xpath('//*[@aria-label="Close"]')
        close.click()



# function call
login('testuseraccount24', 'testuser')
follow_like_comment(3)
