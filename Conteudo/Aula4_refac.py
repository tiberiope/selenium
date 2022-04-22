from urllib.parse import urlparse
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
import os     
from pprint import pprint

url = 'https://selenium.dunossauro.live/aula_04.html'

navegador = Firefox()
navegador.get(url)
link = {}
lista_aula = {}
sleep(5)

hrefs = navegador.find_elements(by=By.TAG_NAME, value='a')

for item in hrefs:
    if 'Aula' in item.text:
        lista_aula[item.text] = item.get_attribute('href')

    if item.get_attribute('href') not in link:
        link[item.text] = item.get_attribute('href')

        if item.text == 'Exercício 3':
            exercicio3 = item


#for item_chave in lista_aula.keys():
#    print(item_chave + ': ' + lista_aula[item_chave])
pprint(lista_aula) 

print(len(link))
print(len(lista_aula))

exercicio3.click()
sleep(3)
navegador.back()
sleep(1)
navegador.get(link['Exercício 3'])
sleep(3)
navegador.back()


sleep(2)

navegador.quit()
os._exit(0)