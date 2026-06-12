# Importaçoes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
import json

ARQUIVO_JSON = "D:\telegram.json"
# Acesso aos dados do telegram via JSON
with open(ARQUIVO_JSON, "r") as arquivo: # abre o json e le ele, dando um apelido de arquivo
    dados = json.load(arquivo) # carrega todas as informaçoes do arquivo

TOKEN = dados ["token"]
CHAT_ID = dados ["chat_id"]

# Abrir navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL do produto
url = "https://www.amazon.com.br/Insta360-desempenho-aprimorado-atualizadas-substitu%C3%ADveis/dp/B0F3P4G8SY"

# Exibir a página
driver.get(url)

# Aguardar carregamento da página
time.sleep(5)

# Informações para coletar os dados
inteiro = driver.find_element(By.CLASS_NAME, "a-price-whole").text
decimal = driver.find_element(By.CLASS_NAME,"a-price-fraction").text

# Remoção de caracteres
inteiro = inteiro.replace(".","").replace(",","")

# Concatenar as variaveis
preco = float(f"{inteiro}.{decimal}")

# Condição para notificar o preço
if preco <= 3200:
    mensagem = (
        f"O preço desejado foi alcançado!!\n"
        f"O preço do produto é: {preco:.2f}\n"
        f"{url}"
    ) 
    resposta = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": mensagem
        }
    )
    print(f"Status da mensagem: {resposta.status_code}")
    print(f"Erro: {resposta.text}")
    print("Pesquisa realizada com sucesso!")

# Fechar aplicação
driver.quit()