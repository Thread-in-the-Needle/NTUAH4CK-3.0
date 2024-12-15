#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep



class Bot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("disable-infobars")
        
        proxy = "127.0.0.1:8080"
        proxy={
            "httpProxy": proxy,
            "ftpProxy": proxy,
            "sslProxy": proxy,
            "noProxy": None,
            "proxyType": "manual",
            "class": "org.openqa.selenium.Proxy",
            "autodetect": False
        }
        chrome_options.set_capability("proxy",proxy)
        chrome_options.set_capability("goog:loggingPrefs", {  # old: loggingPrefs
    "browser": "ALL"})
        self.driver = webdriver.Chrome(options=chrome_options)
        
        
    def visit(self, url):
        # self.driver.get("http://127.0.0.1:1337/")

        self.driver.set_page_load_timeout(10)  # Timeout in seconds
        self.driver.get(url)
        
        sleep(5)

    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    import sys
    url=sys.argv[1]
    bot=Bot()
    bot.visit(url)
    bot.close() 
