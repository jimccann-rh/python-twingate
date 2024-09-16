#!/usr/bin/env python3

import csv
import subprocess
import os
import random
import string
import re
import secrets
import json
import argparse
import time

#Twingate-CLI

logintenat = os.environ["TG_TENANT"]
loginapi = os.environ["TG_API"]


loginoutput = subprocess.check_output('python3 ./tgcli.py auth login -t ' + logintenat + ' -a ' + loginapi, shell=True)
session = loginoutput.decode("utf-8").split(":")[1].strip()
print(f"Session created: {session}")

#datainput = ["python3", "./tgcli.py", "-s", session, "-f", "csv", "account", "list"]
#datainput = ["python3", "./tgcli.py", "-s", session, "-f", "csv", "user", "list"]
datainput = ["python3", "./tgcli.py", "-s", session, "-f", "csv", "user", "list"]
print(datainput)
data = subprocess.check_output(datainput, encoding='UTF-8')

lines = data.splitlines()
header = lines[0]
lines = lines[1:-1]
#print(header)
data = "\n".join(lines)


#data = re.findall("PENDING", data, re.MULTILINE)

def search_and_print(text, search_term):
  """Searches for a given search term in a text and prints the whole line containing it.

  Args:
    text: The text to search.
    search_term: The term to search for.
  """

  pattern = r".*{}.*".format(re.escape(search_term))
  matches = re.findall(pattern, text, re.MULTILINE)
  return matches
  if matches:
    print("Found matches:")
    for match in matches:
      print(match)
  else:
    print("No matches found.")

#search_and_print(data, "PENDING")

data2 = search_and_print(data, "PENDING")

print("USERS STILL PENDING")
print(data2)


parser = argparse.ArgumentParser()
parser.add_argument("--deleteuserspending", default="no", help="Removing pending users")
args = parser.parse_args()

if args.deleteuserspending == "YES":
  print(f"These users to be removed from Twingate {logintenat}")
  for data in data2:
    userid = data.split(",")[0]
    emailid = data.split(",")[3]
    print(f"user to be removed {userid} {emailid}")
    time.sleep(10)
    useremoved = ["python3", "./tgcli.py", "-s", session, "user", "delete", "-i", userid ]
    subprocess.call(useremoved)
    print(useremoved)




animals = ['BlueFly', 'BlackEel', 'RedBoa', 'BlackBat', 'BlackBoa', 'OrangeFox', 'OrangeApe', 'GreenApe', 'WhiteApe', 'PurpleElk', 'RedCow', 'GreenFox', 'YellowFox', 'PinkBoa', 'YellowElk', 'PinkFox', 'GreenBoa', 'RedBat', 'PurpleApe', 'OrangeBat', 'YellowEel', 'OrangeYak', 'RedDog', 'PinkEel', 'PurpleBat', 'OrangeElk', 'BlueBoa', 'OrangeEel', 'GreenCat', 'WhiteDog', 'OrangeCat', 'BlueCat', 'YellowCat', 'GreenCow', 'BlackYak', 'RedCat', 'WhiteFox']

# Print the list
#for animal in animals:
#   subprocess.call(["python3", "./tgcli.py", "auth", "logout", "-s", animal])

subprocess.call(["python3", "./tgcli.py", "auth", "logout", "-s", session])


