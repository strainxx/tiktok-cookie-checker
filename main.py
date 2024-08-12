import json
import random
import time
from typing import List
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from tools import prprint
import os

print("-- strnq tiktok checker --")

tturl = "https://www.tiktok.com/?lang=en"
page_url = "header-more-menu-icon"

stats = "css-mgke3u-DivNumber"

def parse_cookie(filename: str):
    raw_cook = ""
    with open(filename) as cookie:
        raw_cook = cookie.read()
        cookies = json.loads(raw_cook)
    normcookies = []
    for cookie in cookies:
        normcookies.append({"name": cookie["name"], "value": cookie["value"]})
    # print(normcookies)
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    with webdriver.Firefox(options=options) as driver:
        # prprint.rnprint("Webdriver loaded")
        driver.get(tturl)
        # input("Press Enter to get cookies")
        
        for cookie in normcookies:
            driver.add_cookie(cookie)

        prprint.rnprint("Cookies loaded!")
        time.sleep(4)
        driver.refresh()
        # prprint.rnprint("Refreshing page")
        time.sleep(4)
        pr_el = driver.find_element(By.ID, page_url)
        ActionChains(driver).move_to_element(pr_el).pause(1).perform()
        time.sleep(0.3)
        pr_link = driver.find_element(By.CLASS_NAME, "exws2ct3")
        href = pr_link.get_attribute("href")
        driver.get(href)
        time.sleep(4)
        name = driver.find_element(By.CLASS_NAME, "e1457k4r8").text
        checked = driver.find_elements(By.CLASS_NAME, stats)
        prprint.rnprint(f"Account: {name}")
        followers = checked[1].text.split()[0]
        likes =checked[2].text.split()[0]
        with open(f"./res/~strnqchecker~ {followers} F - {likes} L | {name}.json", "w") as f:
            f.write(raw_cook)

if __name__=="__main__":
    cookies = os.listdir("./cookies")
    for c in cookies:
    # print(cookies)
        try:
            parse_cookie("./cookies/"+c)
        except Exception as e:
            prprint.rnprint("Invalid cookie:", c)