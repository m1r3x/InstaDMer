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


def cleanup():
        t = open("users.txt", "r+")
        newuserslist = t.readlines()
        

        g = open("blacklist.txt", "a")
        for i in newuserslist:
            g.write(i)
        g.close()
        
        t.truncate(0)
        t.close
        sys.exit()
        
