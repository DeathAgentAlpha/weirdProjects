from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

import time,random

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

english_words = load_words()
# demo print
randomWord = ""
randomInt = random.randrange(0,len(english_words))
counter = 0
for x in english_words:
    if(counter == randomInt):
        randomWord = x
        break
    counter+=1

randomWord = randomWord[1:-2]

# randomWord1 = ""
# randomInt = random.randrange(0,len(english_words))
# counter = 0
# for x in english_words:
#     if(counter == randomInt):
#         randomWord1 = x
#         break
#     counter+=1

# randomWord1 = randomWord1[1:-2]


driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.youtube.com/")

wait = WebDriverWait(driver, 600)

inpuinputArea = driver.find_element_by_name("search_query")
inpuinputArea.send_keys(randomWord+" music")
inpuinputArea.send_keys(Keys.ENTER)

time.sleep(5) #because this fucking peice of shit doesn't wait for the page to load

driver.find_element_by_id("video-title").click()



