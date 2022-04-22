from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
import os

url = 'https://selenium.dunossauro.live/aula_04_a.html'

navegador = Firefox()
navegador.get(url)

lista_n_ordenada = navegador.find_element(by=By.TAG_NAME, value='ul')
lis = lista_n_ordenada.find_elements(by=By.TAG_NAME, value='li')

print(lis[0].text)

sleep(5)



sleep(1)
navegador.quit()
os._exit(0)