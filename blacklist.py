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



def blacklist():
    a = open("users.txt", "r+")
    userslist = a.readlines()


    b = open("blacklist.txt", "r+")
    currentlist = b.readlines()
    b.close()

    newlist = userslist

    for i in newlist[:]:
        for n in currentlist:
            if i == n:
                newlist.remove(i)

    a.truncate(0) 
    a.close()

    if not newlist:
      print("No new users to send.")     


    a = open("users.txt", "w")

    for i in range(len(newlist)):
        xx = int(i + 1)
        print( str(xx) + " " + newlist[i])

    exclusions = input("Which users to exclude(enter numbers): ")
    os.system('clear')
    excludelist = re.findall(r"[\w']+", exclusions)
    excludelist.sort(key=int)
    excludelist.reverse()

    g = open("blacklist.txt", "a")

    for rr in excludelist:
        for rb in newlist:
            rx = int(rr) - 1
            if rb == newlist[rx]:
                g.write(rb)

    g.close()


    for i in excludelist:
        zz = int(i) - 1

        del newlist[zz]

    for l in newlist:
        a.write(l)
        
    a.close()
