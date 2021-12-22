# Importações
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# Sequencia lógica:

# Abrir o navegador
driver = webdriver.Chrome(
    executable_path=os.getcwd() + os.sep + 'chromedriver.exe')

# Pesquisar URL
driver.get('https://www.mercadolivre.com.br')

# Pesquisar por produto
barraDePesquisa = driver.find_element_by_xpath(
    "//input[@class='nav-search-input']")
barraDePesquisa.click()
barraDePesquisa.send_keys('Pc Gamer')
barraDePesquisa.send_keys(Keys.ENTER)

# Extrair
#   - Titulo
pcGamerTitulo = driver.find_elements_by_xpath(
    "//h2[@class='ui-search-item__title ui-search-item__group__element']")

#   - Preços
pcGamerPreco = driver.find_elements_by_xpath(
    "//div[@class='ui-search-price ui-search-price--size-medium ui-search-item__group__element']//span[@class='price-tag ui-search-price__part']//span[@class='price-tag-amount']//span[@class='price-tag-fraction']")

for pcs in pcGamerTitulo:
    for precos in pcGamerPreco:
        print(f"{pcs.text}: R${precos.text}")
        if pcs and precos == 10:
            break


# //div[@class='ui-search-price ui-search-price--size-medium ui-search-item__group__element']
# //span[@class='price-tag-fraction']

# Navegar para próxima página
# Agendar execução
