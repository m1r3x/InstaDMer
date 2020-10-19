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
from mymessage import mymessage
from login import login
from grabfollowers import grabfollowers
from blacklist import blacklist
from sendmessage import sendmessage
from cleanup import cleanup
from art import art
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

os.system('clear')
art()

username = input("Enter your instagram username: ")
os.system('clear')
art()

password = getpass("Enter your instagram password: ")
os.system('clear')
art()

page = input("Grab followers from?(enter username): ")
os.system('clear')
art()

x = mymessage()

os.system('clear')
art()

chrome_options = Options()
chrome_options.add_argument("--headless")

browser = webdriver.Chrome()

login(username,password,browser)


grabfollowers(page,2,browser)

blacklist()

sendmessage(browser,x)

cleanup()

browser.quit()



