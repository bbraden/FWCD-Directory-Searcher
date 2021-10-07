from discord.message import PartialMessage
import discord
from discord.ext import commands
import selenium
from selenium import webdriver
import os
from time import sleep, time
import json
import requests
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver = "/Users/braden/fwcd1/chromedriver 3"
# os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

def search_dir():
    driver.get("https://fwcd.myschoolapp.com/app#login")

    try:
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, """//*[@id="Username"]""")
                                               ))
        username.send_keys('bradenbaker25')
            # username = driver.find_element_by_xpath("""//*[@id="Username"]""").send_keys('bradenbaker25')
    except:
        driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')

        # next button after username
    try:
        nextbtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="nextBtn"]""")
                                               ))
        nextbtn.click()
            # username = driver.find_element_by_xpath("""//*[@id="Username"]""").send_keys('bradenbaker25')
    except:
        driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')

        # password after next button
    try:
        password = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="Password"]""")
                                               ))
        password.send_keys('Cb575757')
            # username = driver.find_element_by_xpath("""//*[@id="Username"]""").send_keys('bradenbaker25')
    except:
        driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')

        # login button after password
    try:
            loginbtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="loginBtn"]""")
                                               ))
            loginbtn.click()
            # username = driver.find_element_by_xpath("""//*[@id="Username"]""").send_keys('bradenbaker25')
    except:
            driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')

        # get the directory
    sleep(4)
    driver.get('https://fwcd.myschoolapp.com/app/student#directory/1412')

        # searches for student
    try:
            searchbox1 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="search-text-box"]""")
                                               ))
            searchbox1.send_keys('braden')
    except:
            pass

        # search button for student lookup
    try:
            searchbtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="search-directory-button"]""")
                                               ))
            searchbtn.click()
    except:
            pass

        # gets person name
    try:
            personName1 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """//*[@id="directory-items-container"]/tbody/tr/td[2]/div[2]/h3""")
                                               ))
            personName = personName1.text
    except:
            pass

        # click more info button
    try:
            moreInfoBtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, """/html/body/div[2]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[1]/div/table/tbody/tr/td[2]/div[2]/div/div[1]""")
                                               ))
            moreInfoBtn.click()
    except:
            pass

        # wait for stuff to appear
    sleep(3)

    firstNameXPATH = """//*[@id="additional-container-content-5446639"]/div/table/tbody/tr[1]/td/div[1]/div[2]/h4"""
    firstEmailXPATH = """//*[@id="additional-container-content-3238044"]/div/table/tbody/tr[1]/td/div[2]/p[1]/a"""
    firstPhoneXPATH = """//*[@id="additional-container-content-3238044"]/div/table/tbody/tr[1]/td/div[2]/p[2]/a"""

    secondNameXPATH = """//*[@id="additional-container-content-5446639"]/div/table/tbody/tr[2]/td/div[1]/div[2]/h4"""
    secondEmailXPATH = """//*[@id="additional-container-content-3238044"]/div/table/tbody/tr[2]/td/div[2]/p[1]/a"""
    secondPhoneXPATH = """//*[@id="additional-container-content-5446639"]/div/table/tbody/tr[2]/td/div[2]/p[2]/a"""

    a = driver.find_element_by_xpath(
            """/html/body/div[2]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[
            1]/div/table/tbody/tr/td[2]/div[2]/div/div[3]/div/table/tbody/tr[1]/td""").text
    b = driver.find_element_by_xpath(
            """/html/body/div[2]/div/div[13]/div[1]/div/div[3]/div[1]/section/div[2]/div[2]/div[
            1]/div/table/tbody/tr/td[2]/div[2]/div/div[3]/div/table/tbody/tr[2]/td""").text

    personName = driver.find_element_by_xpath(
            """//*[@id="directory-items-container"]/tbody/tr/td[2]/div[2]/h3""").text
    img1 = driver.find_element_by_xpath("""//*[@id="directory-items-container"]/tbody/tr[1]/td[1]/div/img""")
    img = img1.get_attribute("src")

    my_string = personName
    splitted = my_string.split()

    first = splitted[0]
    second = splitted[1]
    third = splitted[2]

    name = (first + ' ' + second)
    print(my_string + name)
    # personEmail = (firstName + '.' + lastName + "@fwcd.com")

        
    sleep(2)
    driver.get("https://www.google.com/")
    driver.delete_all_cookies()