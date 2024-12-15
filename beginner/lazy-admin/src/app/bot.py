#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,os
from random import choices
FLAG = open('flag.txt','r').read().strip()


class Bot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--window-size=1920x1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        
        
    def visit(self, url):
        self.driver.get("http://127.0.0.1:1337/")

        self.driver.add_cookie({
            "name": "flag",
            "value": FLAG,
            "httponly": False
        })
        self.driver.set_page_load_timeout(5)  # Timeout in seconds
        self.driver.get(url)
        print(f"Visited {url}")

    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    import sys
    url=sys.argv[1]
    bot=Bot()
    bot.visit(url)
    bot.close() 
