from selenium import webdriver
import matplotlib.pyplot as plt
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.google.com.tr/?hl=tr')
time.sleep(2)

search = browser.find_element(By.XPATH,'//*[@id="APjFqb"]')
search.click()
search.send_keys("imdb")
search.send_keys(Keys.ENTER)
time.sleep(2)

imdb = browser.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/a')
imdb.click()
time.sleep(2)

menu = browser.find_element(By.XPATH,'//*[@id="imdbHeader-navDrawerOpen"]')
menu.click()
time.sleep(2)

top_films = browser.find_element(By.XPATH,'//*[@id="imdbHeader-navDrawer"]/div/div[2]/div/div[1]/span/div/div/ul/a[2]')
top_films.click()
time.sleep(2)



with open("top250filmvalue.txt", "a") as f:
    for x in range(1,251):
        film_values = browser.find_element(By.XPATH,f'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[{x}]/div[2]/div/div/div[1]/a')
        film_ratings = browser.find_element(By.XPATH,f'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[{x}]/div[2]/div/div/span/div/span')
        f.write(film_values.text + " " + film_ratings.text + "\n")
    time.sleep(5)



menu2 = browser.find_element(By.XPATH,'//*[@id="imdbHeader-navDrawerOpen"]')
menu2.click()
time.sleep(2)

top_series = browser.find_element(By.XPATH,'//*[@id="imdbHeader-navDrawer"]/div/div[2]/div/div[2]/div[1]/span/div/div/ul/a[2]')
top_series.click()
time.sleep(2)

with open("top250seriesvalue.txt", "a") as f:
    for x in range(1,251):
        film_values = browser.find_element(By.XPATH,f'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[{x}]/div[2]/div/div/div[1]/a')
        #series_rating = browser.find_element(By.XPATH,f'//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/li[{x}]/div[2]/div/div/span/div/span')
        f.write(film_values.text + "\n")
    time.sleep(5)


film_names = []
film_ratings = []

with open("top250filmvalue.txt", "r") as f:
    for line in f:
        film_name, film_rating = line.rsplit(" ", 1)
        film_names.append(film_name)
        film_ratings.append(float(film_rating))

plt.figure(figsize=(10, 8))
plt.barh(film_names, film_ratings, color='skyblue')
plt.xlabel('Rating')
plt.ylabel('Film')
plt.title('Top 250 IMDb Filmlerinin Ratingleri')
plt.tight_layout()

plt.gca().invert_yaxis()
plt.subplots_adjust(left=0.25)
plt.xticks(range(11))

plt.show()
time.sleep(5)

