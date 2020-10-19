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


def mymessage():
    print("Enter your message(hit 'enter' twice to submit): ")

    buffer = []
    while True:
        print("> ", end="")
        line = input()
        if line == '':
            break
        buffer.append(line)
    message = "\n".join(buffer)
    return message
    

