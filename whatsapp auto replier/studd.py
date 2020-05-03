from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome('chromedriver')

driver.maximize_window()

driver.get("https://www.youtube.com/")

wait = WebDriverWait(driver, 600)

inpuinputArea = driver.find_element_by_name("search_query")
inpuinputArea.send_keys('red velvet bad boy')
inpuinputArea.send_keys(Keys.ENTER)

time.sleep(2)

driver.find_element_by_id("video-title").click()



