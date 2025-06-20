from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://olymptrade.com/platform")

email = "marcoskaua951426873@gmail.com"
senha = "marcosxerecabosal"
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
    print("Login enviado, aguardando confirmação...")
    # Aguarda um elemento que só aparece após o login (exemplo: botão de logout)
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-test='logout']"))
        )
        print("Login realizado com sucesso!")
    except Exception:
        print("Login pode não ter sido realizado. Verifique as credenciais ou possíveis mudanças na página.")
except Exception as e:
    print("Não foi possível localizar os campos de e-mail ou senha:", e)
finally:
    input("Pressione Enter para fechar o navegador...")
    driver.quit()

