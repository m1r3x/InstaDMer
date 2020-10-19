#!/usr/bin/env python3
import sys
import os
import readline
import fileinput
from time import sleep
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
import re
from selenium.common.exceptions import NoSuchElementException    
    
    
    
def grabfollowers(page,t,browser):    
    
    
    browser.get('https://www.instagram.com/' + page)

    browser.implicitly_wait(4)
    try:
        usernotfound = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/p/a")
        print("Account with username " + '"{}"'.format(page) + " does not exist.")
        browser.quit()
        sys.exit()
    except NoSuchElementException:
        pass
    
    try:
    
        followers_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers_button.click()

        browser.implicitly_wait(3)

        fBody  = browser.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll < t: # scroll time
            browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            sleep(1)
            scroll += 1
                    
        browser.implicitly_wait(3)

        i = browser.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")

        victims=[]
        for y in i:
            temp = y.get_attribute("title")
            victims.append(temp)
                    
        f=open('users.txt','a+')
        for ele in victims:
            f.write(ele+'\n')
        f.close()

        
    except NoSuchElementException:
        print("Account with username " + '"{}"'.format(page) + " is private.")
        browser.quit()
        sys.exit()       

            
