# import os
# import requests
# os.environ["PATH"] += ";D:/programming/chrome_driver/chromedriver-win64"
# url = "https://akharinkhabar.ir/sport"
# response = requests.get(url)
#
# print(response.text)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

all_news_dict = []

url = "https://akharinkhabar.ir/"

for group in ["sport", "cinema", "money"]:

    driver = webdriver.Chrome()
    driver.get(f'{url}/{group}')

    # print(driver.find_element(By.TAG_NAME('article')))
    # print(driver.find_elements(By.CLASS_NAME("rectangle_container__rBE5L")))



    # #id
    # .class
    # tag


    news_list = driver.find_elements(By.CSS_SELECTOR,".rectangle_container__rBE5L")
    for news in news_list:
        my_list = news.text.split("\n")
        news_dict = {
            "group": my_list[0],
            "time": my_list[2],
            "time": my_list[3],
            "like": my_list[4],
            "comments": my_list[5],
            "view": my_list[6],
        }
        all_news_dict.append(news_dict)

    driver.close()

import pandas as pd

df = pd.DataFrame(all_news_dict)
df.to_excel("news.xlsx", index=False)