from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from json import load, loads


url = 'http://selenium.dunossauro.live/aula_05.html'
navegador = Firefox()

navegador.get(url)

sleep(10)

# Busca por ID do CSS.
a = navegador.find_element(By.CSS_SELECTOR, value='#grid')
print(a)

# Busca por CLASSE CSS.
b = navegador.find_element(By.CSS_SELECTOR, value='.components-grid')
print(b)

# Busca pela DIV da CLASSE components-grid CSS.
c = navegador.find_element(By.CSS_SELECTOR, value='div.components-grid')
print(c)