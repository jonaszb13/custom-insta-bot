import os, json, random, threading, requests, time, instagrapi, traceback, os, pymongo, subprocess, time; 
from tabnanny import check
from instagrapi import Client
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

__PROGRAMID__ = "c2JedU7LcPNfkW8H9yPVAFjTuPxeJh9"
__VERSION__ = "1.1"

config = json.loads(open("./config.json", "r", encoding="utf-8").read())
proxies = open("./proxies.txt", "+r", encoding="utf-8").read().splitlines()

class color:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET_ALL = "\033[0m"
    BLUE = '\033[96m'



def get_user():
    print("user")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://simpliers.com/de/gewinnspiel/instagram")

    time.sleep(1)

    link = driver.find_element(By.NAME, "url[]")
    link.send_keys(send_link)

    time.sleep(1)

    banner = driver.find_element(By.CLASS_NAME, "d-block.text-center.animate__animated.animate__pulse.animate__infinite.mt-8")
    banner.click()

    time.sleep(5)

    search = driver.find_element(By.ID, "cekilisBaslat")
    search.submit()

    time.sleep(30)

    backdrop = driver.find_element(By.CLASS_NAME, "count-unique-users-button")
    backdrop.click()

    time.sleep(5)

    comments = driver.find_element(By.ID, "katilimcilariGorBtn")
    comments.click()

    time.sleep(5)

    rows = driver.find_elements(By.XPATH, "//div[@class='d-flex justify-content-between align-items-center']")
    limit = 0
    with open('usernames.txt', 'w') as f:
        f.close()

    for row in rows:
        limit +=1
        results = row.find_element(By.XPATH, ".//span[@class='comment-username h5 mb-0']")
        if "0 : 0" not in results.text:
            if limit < 120:
                print(limit)
                print(results.text)
                with open('usernames.txt', 'a') as f:
                    f.write(results.text)
                    f.write('\n')
            else:
                print("all usernames collected")

    time.sleep(10)

    driver.quit()

    start(config["script_settings"]["threading"])

    return 0;



def user_handler():
    print("handler")

    with open("./usernames.txt", encoding="utf-8") as f:
        lines = f.readlines()
        tokens = []
        for splines in lines:
            hdr = splines.split("\n")[0]
            tokens.append(hdr)
    return tokens


def send_dm(username, password, proxy, userdm, messageText, count, i):
    try:
        username = username
        password = password

        cl = Client()
        if config["script_settings"]["use_proxy"]:
            cl.set_proxy(proxy["https"])
        cl.login(username, password)
        userid = cl.user_id_from_username(userdm)
        #print(userid)
        for x in range(0,count):
            a = cl.direct_send(messageText, [int(userid)])
            print(f"{color.GREEN}[{i}] {color.RESET_ALL}Message succesfully sent to {color.GREEN}@{userdm} {color.RESET_ALL}with {color.GREEN}@{username}{color.RESET_ALL}.")
            print("15 second timeout")
    except Exception as err:
        print(f"{color.RED}[{i}]{color.RESET_ALL} An error occured when sending message to {color.RED}@{userdm} {color.RESET_ALL}account. Passing. ERROR: {err}")
        #traceback.print_exc()
        pass


def start(thread):
    print("start")
    count = 0

    try:
        tx = []

                    
        for id, user_name in enumerate(user_handler()):
            time.sleep(15)
            print("sending message...")

            if config["script_settings"]["use_proxy"]:
                                
                if threading.active_count() <= thread:
                    mT = threading.Thread(target=send_dm, args=(send_username, send_password, pp, user_name, send_text_message, config["script_settings"]["message_amount"],id+1))
                    #send_dm(config["instagram_settings"]["username"],config["instagram_settings"]["password"], random.choice(working_proxies), user_name, config["instagram_settings"]["text_message"])
                    mT.daemon = True
                    mT.start()
                    tx.append(mT)
                    count += 1
            else:
                if threading.active_count() <= thread:
                    mT = threading.Thread(target=send_dm, args=(send_username, send_password, None, user_name, send_text_message, config["script_settings"]["message_amount"],id+1))
                    #send_dm(config["instagram_settings"]["username"],config["instagram_settings"]["password"], random.choice(working_proxies), user_name, config["instagram_settings"]["text_message"])
                    mT.daemon = True
                    mT.start()
                    tx.append(mT)
                    count += 1
            
            if count == 15:
                print("3 hour timeout")
                time.sleep(10800)
                print("start messaging 15 more people before next timeout")
        
        for t in tx:
            t.join(75)
    except Exception as e:
        traceback.print_exc()
        pass


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    check = [True]
    if check[0]:   
        print(f"{color.GREEN}[+] License correct program starting... {color.RESET_ALL}")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        print(fr"""{color.GREEN}

    Press any key to start the script...
    {color.RESET_ALL}    """)
        input("....")
        send_username = input("sending acc username: ")
        send_password = input("sending acc password: ")
        send_text_message = input("sending message: ")

        send_link = input("insta post link: ")

        try:
            get_user()
            input("....")
        except:
            traceback.print_exc()
            input(".....")
    else:
        print(f"{color.RED}[-] {check[1]} {color.RESET_ALL}")
        input("....")
