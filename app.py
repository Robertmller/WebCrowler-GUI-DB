# Importações
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import sleep
import random
#import schedule

# Se quiser agendar execução, transforma essa parte em função
# def buscarPrecos():

# Sequencia lógica:

# Abrir o navegador
driver = webdriver.Chrome(
    executable_path=os.getcwd() + os.sep + 'chromedriver.exe')

# Pesquisar URL
driver.get('https://www.mercadolivre.com.br')

# Pesquisar por produto
sleep(random.randint(3, 5))
barraDePesquisa = driver.find_element_by_xpath(
    "//input[@class='nav-search-input']")

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
        "//h2[@class='ui-search-item__title ui-search-item__group__element']")

    # - Preços
    sleep(random.randint(3, 5))
    precoDoProduto = driver.find_elements_by_xpath(
        "//div[@class='ui-search-price ui-search-price--size-medium ui-search-item__group__element']//span[@class='price-tag ui-search-price__part']//span[@class='price-tag-amount']//span[@class='price-tag-fraction']")

    # Salvando informações em TEXT
    for Titulo, Preco in zip(tituloDoProduto, precoDoProduto):
        with open('produtos.txt', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f"{Titulo.text} - R${Preco.text}" + os.linesep)

    # Navegar para próxima página
    sleep(random.randint(3, 5))
    driver.execute_script(
        'window.scrollTo(0, document.body.scrollHeight);')
    botaoDeProximo = driver.find_element_by_xpath(
        "//li[@class='andes-pagination__button andes-pagination__button--next']")

    sleep(random.randint(3, 5))
    botaoDeProximo.click()


# Agendar execução

# schedule.every().days.at('10:00').do(buscarPrecos)

# while True:
#     schedule.run_pending()
#     sleep(1)
