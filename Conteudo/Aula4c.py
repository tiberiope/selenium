from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
import os

def find_by_text(navegador, tag, text):
    elementos = navegador.find_elements(by=By.TAG_NAME, value=tag)

    for elemento in elementos:
        if elemento.text == text:

            return elemento

url = 'https://selenium.dunossauro.live/aula_04_b.html'

navegador = Firefox()
navegador.get(url)

sleep(1)

# Também funciona: for texto in ['um', 'dois', 'tres', 'quatro']:

nomes_das_caixas = ['um', 'dois', 'tres', 'quatro']

for nome in nomes_das_caixas:

    find_by_text(navegador, 'div', nome).click()
    sleep(0.5)

for nome in nomes_das_caixas:
    navegador.back()
    sleep(0.5)

for nome in nomes_das_caixas:
    navegador.forward()
    sleep(0.5)

sleep(1.5)
navegador.quit()
os._exit(0)