import requests
import re
import time
import asyncio
from os import system, name 
from time import sleep 

def clear(): 
  

    if name == 'nt': 
        _ = system('cls') 

    else: 
        _ = system('clear') 

logo = "   _____                   _        _____                         \n  / ____|                 | |      |  __ \                        \n | |  __  ___   ___   __ _| | ___  | |__) |_ _ _ __ ___  ___ _ __ \n | | |_ |/ _ \ / _ \ / _` | |/ _ \ |  ___/ _` | '__/ __|/ _ \ '__|\n | |__| | (_) | (_) | (_| | |  __/ | |  | (_| | |  \__ \  __/ |   \n  \_____|\___/ \___/ \__, |_|\___| |_|   \__,_|_|  |___/\___|_|   \n                      __/ |                                       \n                     |___/                                        \n"
clear()
print(logo)
print("Developpé par AndroneDev (www.androne.dev)")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("Utilisation des dorks du fichier \"dorks.txt\"")
print("Nombre de pages Google a chercher par dorks ?")
nbpage = int(input())
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("Chargement ..")


# functions :
async def runsearch(query, pagestart):
    r = requests.get('https://www.google.com/search?q=' +
                     query + "&start=" + str(pagestart))
    results = re.findall(
        "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", r.text)
    for result in results:
        if not "google" in result:
            time.sleep(.1)
            print(result)
            with open("urls.txt", "a") as myfile:
                myfile.write(result + "\n")


# start


print("Started ! : %s" % time.ctime())

with open("./dorks.txt") as f:
    content = f.readlines()
    for line in content:
        for n in range(nbpage):
            start = 10*n
            asyncio.run(runsearch(line, start))

            time.sleep(3)


time.sleep(5)
print("End : %s" % time.ctime())
input()