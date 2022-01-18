# Importações
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import sleep
import random
import sqlite3
from csv import DictReader, DictWriter

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

    #################
    # Salvando dados no Banco
    with sqlite3.connect('produtos.db') as conexao:
        # criando conexão com o Db
        sql = conexao.cursor()

        # criando uma tabela
        sql.execute(
            'create table IF NOT EXISTS itens(titulo text, valor text);')

        for Titulo, Preco in zip(tituloDoProduto, precoDoProduto):
            # inserindo dados na tabela
            sql.execute('insert into itens (titulo, valor) values (?,?)', [
                        Titulo.text, Preco.text])

        conexao.commit()
    conexao.close()

    #################

    # Salvando informações em csv
    # with open(f'{buscar_produto}.csv', 'w', newline='', encoding='utf-8') as arquivo:
    #     label = ['Titulo do Produto', 'Valor do Produto']
    #     escritorCsv = DictWriter(arquivo, fieldnames=label)
    #     escritorCsv.writeheader()
    #     for Titulo, Preco in zip(tituloDoProduto, precoDoProduto):
    #         escritorCsv.writerow({
    #             'Titulo do Produto': Titulo.text,
    #             'Valor do Produto': Preco.text
    #         })

    # Navegar para próxima página
    sleep(random.randint(3, 5))
    driver.execute_script(
        'window.scrollTo(0, document.body.scrollHeight);')
    botaoDeProximo = driver.find_element_by_xpath(
        "//*[@class='nextLink']")

    sleep(random.randint(3, 5))
    botaoDeProximo.click()
