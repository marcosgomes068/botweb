from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://olymptrade.com/platform")

email = "programador042006@gmail.com"
senha = "programador042006"
try:
    email_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    senha_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    email_input.send_keys(email)
    senha_input.send_keys(senha)
    senha_input.send_keys(u'\ue007')
except Exception as e:
    print("Não foi possível localizar os campos de e-mail ou senha:", e)

