from bs4 import BeautifulSoup
import requests
import random
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import csv
import matplotlib.pyplot as plt
import datetime

def ConvertNumber(short):
    short = short.lower()
    if "k" in short:
        short = int(round(float(short.replace("k", ""))) * 1000)
    elif "m" in short:
        short = int(round(float(short.replace("m", ""))) * 1000000)
    elif "," in short:
        short = int(short.replace(",", ""))
    return short

def ConvertTime(short):

    now = datetime.datetime.now()
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul",
              "aug", "sep", "oct", "nov", "dec"]

    if "h" in short:
        short = int(float(short.replace("h", "")) * 60)
    elif "m" in short and "mar" not in short and "may" not in short:
        short = int(short.replace("m", ""))
    elif "s" in short and "sep" not in short:
        short = 1
    else:
        
        day = int(short.split(" ")[1])
        
        for month in months:
            if month in short:
                post_month = month
        month_diff = now.month - (months.index(post_month)+1)
        day_diff = now.day - day
        day_diff = day_diff + (month_diff * 30)
        short = int(day_diff * 1440)
        
    return short

def PostTime(driver):
    
    post_time = driver.find_element_by_class_name(
        "time")

    post_time = ConvertTime(post_time.text.split("\n")[0].lower())
    
    return post_time

def Verified(driver):
    person = driver.find_element_by_class_name(
        "FullNameGroup")    
    name = person.text.split("\n")[0]
    if "Verified" in person.text:
        verified = 1
    else:
        verified = 0
    return verified

def LikeCommentRetweet(driver):
    comments = driver.find_element_by_class_name(
        "stream-item-footer")

    comments = comments.text.split("\n")
    if len(comments) == 3:
        comment = 0
        retweet = 0
        like = 0
    else:
        if comments[1] == "Retweet":
            comment = 0
        else:
            comment = int(ConvertNumber(comments[1]))
        if comments[3] == "Like":
            retweet = 0
        else:
            retweet = int(ConvertNumber(comments[3]))
        try:
            like = int(ConvertNumber(comments[5]))
        except:
            like = 0
    return comment, retweet, like

def Followers(driver):
    icon = driver.find_element_by_class_name(
        "stream-item-header")
    driver.implicitly_wait(10)
    icon = icon.find_element_by_tag_name('img')
    icon.click()
    driver.implicitly_wait(10)
    values = driver.find_elements_by_class_name(
        "ProfileNav-value")
    labels = follow = driver.find_elements_by_class_name(
        "ProfileNav-label")
    
    for i in range(len(labels)):
        if labels[i].text == "Followers":
            index = i

    followers = ConvertNumber(values[index].text)

    return followers

def getWord():
    with open("words.txt", "r") as f:
        words = f.readlines()
        word = words[random.randint(0, len(words)-1)].replace("\n", "")
    return word

def Save(data):
    
    with open('Train.csv', 'a', newline="") as myfile:
        wr = csv.writer(myfile)
        wr.writerows(data)
        
def getPostDetails():

    driver = webdriver.Firefox()

    data = []

    for i in range(10000):
        try:
            print(i)
            invalid = False
            driver.implicitly_wait(10)
            word = getWord()
            #https://twitter.com/search?l=en&q=%22hello%22&src=typd&lang=en-gb
            url = "https://twitter.com/search?l=en&q=%22" + word + "%22&src=typd&lang=en-gb"
            driver.get(url)

            post_time = PostTime(driver)

            if invalid == False:
                driver.implicitly_wait(10)
                verified = Verified(driver)
                comment, retweet, like = LikeCommentRetweet(driver)
                follower = Followers(driver)
            
                data.append([post_time, verified, comment, retweet, like, follower])

                if random.randint(0, 5) == 5:
                    print("Saving")
                    Save(data)
                    data = []
                        
                    
        except Exception as e: print(e)

    return data

data = getPostDetails()



    
