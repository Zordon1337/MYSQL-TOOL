import mysql.connector
import time
import os
from colorama import init
from colorama import Back
from termcolor import colored

init()


print(Back.BLUE + "enter your sql username")
user = input("")
print(Back.BLUE + "enter your sql password (if you don't have password leave it blank)")
password = input("")
print(Back.GREEN + "Note: you must manually replace new database name in create.py")
print(Back.GREEN + "if you replaced it already just wait 2 sec")
time.sleep(2)

mydb = mysql.connector.connect(
  host="localhost",
  user=(user),
  password=(password),
)

mycursor = mydb.cursor()

#change database name
mycursor.execute("CREATE DATABASE changemelol")

print(Back.GREEN + 'done you can close this now')
time.sleep(100)