# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:12:52 2022

@author: agarw
"""

import random as ran

#Data:
l = list("abcdefghijklmnopqrstuvwxyz")
lc = list(("abcdefghijklmnopqrstuvwxyz").upper())
sc = list("!@#$%^&*")
num = list("1234567890")
ml = l+sc+num+lc



#Funtions:

def randomiser(n):
    pwd =[]
    for i in range(n):
        pwd.append(ran.choice(ml))
    print("".join(pwd))

def noncusran(req):
    choicel = []
    pwd =[]
    for i in list(req):
        if i == "c":
            choicel = choicel + l
        elif i == "n":
            choicel = choicel + num
        elif i == "s":
            choicel = choicel + sc
        elif i == "C":
            choicel = choicel + lc
    for i in range(n):    
        pwd.append(ran.choice(choicel))
    print("".join(pwd))

def cusran(seq):
    pwd =[]
    for i in seq:
        if i == "c":
            pwd.append(ran.choice(l))
        elif i == "n":
            pwd.append(ran.choice(num))
        elif i == "s":
            pwd.append(ran.choice(sc))
        elif i == "C":
            pwd.append(ran.choice(lc))
        else: 
            pwd.append(i)
    print("".join(pwd))
    
    
#Main Program:    
    
n = int(input("Enter password length: "))
rf = input("If you want a totally randomized password, enter y else, if you want to remove certain type of characters, enter n")
    
if rf == "y":
    randomiser(n)
else:
    print("Enter c for letter, n for number, s for special character, C for capital letter, without space or if you want a totally custom password, enter 'custom'")
    req = input("Enter Requirements: ")
    if req != "custom":
        noncusran(req)
    else:
        print("Enter password sequence (c for letter, n for number, s for special character, C for capital letter):\n ")
        print("For example: if you want first 4 characters to be lowercase letters and last 4 to be numbers, type: ccccnnnn ")
        while True:
            seq = list(input(""))
            if len(seq) != n:
                print("Error: Enter sequence length as password length")
            else: 
                break
        cusran(seq)
