from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
import os

def find_by_text(navegador, tag, text):
    elementos = navegador.find_elements(by=By.TAG_NAME, value=tag)

    for elemento in elementos:
        if elemento.text == text:

            return elemento
        
def find_by_href(navegador, link):
    elementos = navegador.find_elements(by=By.TAG_NAME, value='a')
    for elemento in elementos:
        if link in elemento.get_attribute('href'):

            return elemento
        

url = 'https://selenium.dunossauro.live/aula_04_a.html'

navegador = Firefox()
navegador.get(url)

sleep(3)

elemento_li = find_by_text(navegador, 'li', 'Item 2')
elemento_a = find_by_href(navegador, 'ddg')

print(elemento_li.text)
print('Link do ' + elemento_a.text + ' é: ' + elemento_a.get_attribute('href'))


sleep(3)
navegador.quit()
os._exit(0)