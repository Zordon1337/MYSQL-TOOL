import mysql.connector
from colorama import init
from colorama import Back
from termcolor import colored
import time
import os

init()

print("enter your sql username")
user = input("")
print("enter your sql password (if you don't have password leave it blank)")
password = input("")
print("enter your database name")
database = input("")

mydb = mysql.connector.connect(
  host="localhost",
  user=(user),
  password=(password),
  database=(database)
)
mycursor = mydb.cursor()

print(Back.RED + "note: you must manually change tables in insert.py otherwise it will won't work")
print(Back.RED + "if you replaced it already just wait 2 sec")
time.sleep(2)
#change here
sql = "INSERT INTO players (id, username) VALUES (%s, %s)"
val = ("2", "Zordon")
mycursor.execute(sql, val)

mydb.commit()

print(Back.RED + "done you can close this now")

time.sleep(100)