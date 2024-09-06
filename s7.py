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

# all_news_dict = []
#
# url = "https://akharinkhabar.ir/"
#
# for group in ["sport", "cinema", "money"]:
#
#     driver = webdriver.Chrome()
#     driver.get(f'{url}/{group}')
#
#     # print(driver.find_element(By.TAG_NAME('article')))
#     # print(driver.find_elements(By.CLASS_NAME("rectangle_container__rBE5L")))
#
#
#
#     # #id
#     # .class
#     # tag
#
#
#     news_list = driver.find_elements(By.CSS_SELECTOR,".rectangle_container__rBE5L")
#     for news in news_list:
#         my_list = news.text.split("\n")
#         news_dict = {
#             "group": my_list[0],
#             "time": my_list[2],
#             "time": my_list[3],
#             "like": my_list[4],
#             "comments": my_list[5],
#             "view": my_list[6],
#         }
#         all_news_dict.append(news_dict)
#
#     driver.close()
#
# import pandas as pd
#
# df = pd.DataFrame(all_news_dict)
# df.to_excel("news.xlsx", index=False)


from datetime import datetime,timedelta
import pandas as pd
import numpy as np

# df = pd.read_excel('news.xlsx')



# df["time"] = df["time"].str.replace("دقیقه پیش", "")
# df["time"] = df['time'].str.replace("-", "")
# df["time"] = df["time"].str.strip()
#
# df["time"] = pd.to_numeric(df["time"])


# df["like_count"] = df['like'].apply(lambda lk: float(lk.replace('K', "")) * 1000 if "K" in lk else float(lk))


# print(df)
# print(df.info)

# from hazm import *
#
# # text = "در دیدارهای دیگر امروز بحرین میزبانش، استرالیا، را یک بر صفر شکست داد تا خالق اولین شگفتی باشد. کره‌جنوبی در خانه با فلسطین مساوی کرد و داد هوادارانش را درآورد. ژاپن، اما، در نخستین دیدارش توانست با اقتدار کامل ۷ بر صفر چین را با سرمربی‌گری برانکو ایوانکوویچ شکست دهد؛ نتیجه‌ای که رسانه‌های چین را به‌سرعت‌ برآشفت."
#
# normalizer = Normalizer()


# norm_text = normalizer.normalize(text)
# print(norm_text)
#
# sentences = sent_tokenize(norm_text)
# words = word_tokenize(norm_text)
#
# cleaned_word = [word for word in words if word not in stopwords_list()]
# print(words)
# print(cleaned_word)
#
# stemmer = Stemmer()
#
# for word in cleaned_word:
#     print(word, stemmer.stem(word))

# lemmatizer = Lemmatizer()
# for word in cleaned_word:
#     print(word, lemmatizer.lemmatize(word))

# tagger = POSTagger(model="pos_tagger.model")
# for sentence in sentences:
#     print(tagger.tag(word_tokenize(sentence)))


# from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
#
# count_vectorizer = CountVectorizer()
# count_vector = count_vectorizer.fit_transform(cleaned_word)
# print(count_vector)
#
#
# tfidf_vectorizer = TfidfVectorizer()
# tfidf_vector = tfidf_vectorizer.fit_transform(cleaned_word)
# print(tfidf_vector)
#
#
# from sklearn.preprocessing import OneHotEncoder, LabelEncoder
# text = "man ali man reza shoma"
# words = np.array(text.split("")).reshape(-1, 1)
# encoder = LabelEncoder()
# print(encoder.fit_transform(words))
#
# one_hot_encoder = OneHotEncoder()
# print(one_hot_encoder.fit_transform(words))


# import pandas as pd
#
# X = np.arange(1, 100).reshape(-1,1)
# weights = np.array([50,1,2,3,4,5]).reshape(-1, 1)
#
#
# df = pd.DataFrame(X)
#
# my_list = list(df.rolling(5).mean())
#
# for item in my_list:
#     if len(item) == 5:
#         print(item.values * weights)



# import pandas as pd
#
# X = np.arange(1, 100).reshape(-1,1)
# weights = np.array([50,1,2,3,4,5]).reshape(-1, 1)
#
#
# df = pd.DataFrame(X)
#
# my_list = list(df.rolling(5).mean())
#
# for item in my_list:
#     if len(item) == 5:
#         print(item.values * weights)


