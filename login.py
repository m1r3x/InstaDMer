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



def login(username,password,browser):


    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com/')


    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")


    username_input.send_keys(username)
    password_input.send_keys(password)
    browser.implicitly_wait(1)
    

    try:
    
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        browser.implicitly_wait(4)
        
    except:
        print("Your credentials are wrong.")
        browser.quit()
        sys.exit()
        

    try:
        
        wrongpassword = browser.find_element_by_xpath("//*[@id='slfErrorAlert']")
        print("Your credentials are wrong.")
        browser.quit()
        sys.exit()
        
    except:
        pass
    
     
    
    
    
    
