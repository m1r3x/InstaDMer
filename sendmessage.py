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
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


def sendmessage(browser,message):
    usersfile = open('users.txt','r+')
    users = usersfile.readlines()

    n = 0


    while n < len(users):    
        user = users[n]
        
        browser.get('https://www.instagram.com/direct/new')

        
        if n == 0:
            try:
                notification_button = WebDriverWait(browser, 5).until( 
        EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]"))
        )
                notification_button.click()

                search_input = browser.find_element_by_css_selector("input[placeholder='Search...']")
                search_input.send_keys(user)

                sleep(4)

                image_button = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[1]")
                image_button.click()
                
                
                next_button = WebDriverWait(browser, 5).until( 
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[2]/div/button"))
        )
                next_button.click()
                
                message_input = WebDriverWait(browser, 5).until( 
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea"))
        )
        
                message_input.send_keys(message)

                send_button = WebDriverWait(browser, 5).until( 
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button"))
        )
                send_button.click()
                
                
            
                n = n + 1
                     
            except:
                
                print("It looks like you are blocked by Instagram. Please try again later.")
                browser.quit()
                exit()
            
            
        else:
            try:
                sleep(10)
                
                search_input = browser.find_element_by_css_selector("input[placeholder='Search...']")
                search_input.send_keys(user)

                sleep(4)

                image_button = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[2]/div[1]")
                image_button.click()
                
                
                next_button = WebDriverWait(browser, 5).until( 
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[2]/div/button"))
        )
                next_button.click()
                
                message_input = WebDriverWait(browser, 5).until( 
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea"))
        )
        
                message_input.send_keys(message)

                send_button = WebDriverWait(browser, 5).until( 
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button"))
        )
                send_button.click()
                
                
            
                n = n + 1
            
            except:
            
                ll = open("blacklist.txt", "a")

                a = n
                
                ym = 0
                
                while ym < a:
                    d = users[ym]
                    ll.write(d)
                    ym = ym + 1
                ll.close()
                
                z = 0
                while z < a:
                    users.pop(0)
                    z = z + 1
                    
                usersfile.truncate(0)
                usersfile.close()
                
                usersfile = open('users.txt','r+')
                for qq in users:
                    usersfile.write(qq)
                usersfile.close()
                
                print("It looks like you are blocked by Instagram. Please try again later.")
                exit()   
            
    sleep(1)

