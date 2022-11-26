import random

import sys
import os


class ATM:
    def __init__(self):
        id = 0


print("-------------------------------------------------------------")
print("--------------------Welcome to the MonkePal------------------")
print("------------------------Sign in/Sign up----------------------")
print("-------------------------------------------------------------")
print("Enter a number: ")
print("1. Sign in")
print("2. I don`t have an account")
print("Any. Exit")
print("-------------------------------------------------------------")

choose = input("Choose your action: ")

while True:
    if choose == "1":
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')
        print("-----------------------MonkePal--------------------------")
        print("------------------------Sign in--------------------------")
        accName = input("Input your login: ")
        accPass = input("Input your password: ")

    elif choose == "2":
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')
        print("-----------------------MonkePal--------------------------")
        print("------------------------Sign in--------------------------")
        accName = input("Input your login: ")
        accPass = input("Input your password: ")

    else:
        break

print("-------------------------------------------------------------")
print("System closed. Thank You")