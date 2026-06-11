# importaçoes

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time

# acesso do telegram
TOKEN = "https://api.telegram.org/bot8313858074:AAH48LHPhbVcU9dUobQFULDJyIywYEFrUk4/getUpdates"

CHAT_ID = "1919804153"

# url's produtos
produtos = [
    {
        "url" : "https://www.amazon.com.br/Echo-Dot-4%C2%AA-gera%C3%A7%C3%A3o-Cor-Azul/dp/B09B8QFYZ2",
        "valor_desejado" : 450
    },

    {
        "url" : "https://www.amazon.com.br/Insta360-desempenho-aprimorado-atualizadas-substitu%C3%ADveis/dp/B0F3P4G8SY",
        "valor_desejado" : 3200
    }
]

# driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# loop para percorrer toda a lista de url's e trata o valor desejado
for produto in produtos:
    driver.get(produto["url"])

    # aguardar carregamento da página
    time.sleep(5)

    inteiro = driver.find_element(By.CLASS_NAME, "a-price-whole").text
    decimal = driver.find_element(By.CLASS_NAME,"a-price-fraction").text

    # remoção de caracteres
    inteiro = inteiro.replace(".","").replace(",","")

    # concatenar as variaveis
    preco = float(f"{inteiro}.{decimal}")

    # condição para notificar o preço
    if preco <= produto["valor_desejado"]:
        mensagem = (
            f"O preço desejado foi alcançado!!\n"
            f"O preço do produto é: {preco:.2f}\n"
            f"{produto['url']}"
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

# fechar aplicação
driver.quit()