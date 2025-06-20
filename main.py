from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://exemplo.com")
input_box = driver.find_element(By.NAME, "q")
input_box.send_keys("ChatGPT")
input_box.submit()
