# Importações
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import sleep
import random

import json
from pathlib import Path

# Se quiser agendar execução, descomenta essa parte e a do fim da página
#import schedule
# def buscarPrecos():


# Abrir o navegador
driver = webdriver.Chrome(
    executable_path=os.getcwd() + os.sep + 'chromedriver.exe')

# Pesquisar URL
driver.get('https://www.kabum.com.br/')

# Pesquisar por produto
sleep(random.randint(3, 5))
barraDePesquisa = driver.find_element_by_xpath(
    "//*[@id='input-busca']")

sleep(random.randint(3, 5))
barraDePesquisa.click()

sleep(random.randint(3, 5))
buscar_produto = input("Qual produto deseja buscar: ")
barraDePesquisa.send_keys(buscar_produto)

sleep(random.randint(3, 5))
barraDePesquisa.send_keys(Keys.ENTER)
sleep(random.randint(3, 5))

while True:
    # Extrair

    # - Titulo
    sleep(random.randint(3, 5))
    tituloDoProduto = driver.find_elements_by_xpath(
        "//*[@class='sc-kHOZwM brabbc sc-fHeRUh jwXwUJ nameCard']")

    # - Preços
    sleep(random.randint(3, 5))
    precoDoProduto = driver.find_elements_by_xpath(
        "//*[@class='sc-iNGGcK fTkZBN priceCard']")

    # Salvando informações em TEXT
    # O Arquivo será salvo com o nome do campo de busca. Ex: Pc Gamer.txt, Celular.txt
    for Titulo, Preco in zip(tituloDoProduto, precoDoProduto):
        with open(f'{buscar_produto}.txt', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f"{Titulo.text} - R${Preco.text}" + os.linesep)

    # Navegar para próxima página
    sleep(random.randint(3, 5))
    driver.execute_script(
        'window.scrollTo(0, document.body.scrollHeight);')
    botaoDeProximo = driver.find_element_by_xpath(
        "//*[@class='nextLink']")

    sleep(random.randint(3, 5))
    botaoDeProximo.click()


# Agendar execução

# schedule.every().days.at('10:00').do(buscarPrecos)

# while True:
#     schedule.run_pending()
#     sleep(1)
