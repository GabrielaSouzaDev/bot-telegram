# Autor: Gabriela Souza
# Projeto bot de telegram com raspagem de dados


# Passos

# Capturar a info
# Só me notifique se chegar na minha condição


# importações
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

# informações do telegram
TOKEN = 'SEU TOKEN DO BOT'
CHAT_ID = 'SEU CHAT ID'

# url do site
url = "https://www.americanas.com.br/cadeira-presidente-escritorio-giratoria-apoio-de-cabeca-fox-office-preta-46a--174100j5898vn118/p"
# driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url) # mostra as informações da url

time.sleep(5) # tempo que a tela do ecommerce fica aberta

# classe dinamica
preco = driver.find_element(
    By.CSS_SELECTOR, "[class*='ProductPrice_productPrice']").text # raspa os dados da classe
    # By.CSS_SELECTOR -> seleciona classe com css dinamico
    # By.CLASS_NAME -> seleciona classe estatica

# exibir os resultados
print(preco)

mensagem = f"preço encontrado: {preco}\n{url}"

requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": mensagem
    })

driver.quit()