from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import os

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

navegador = Firefox()
navegador.get(url)

sleep(5)

dici = {}

tag_h = navegador.find_element(by=By.TAG_NAME, value='h1')
dici[tag_h.text] = {}

tag_p = navegador.find_elements(by=By.TAG_NAME, value='p')

for elemento in tag_p:
    dici[tag_h.text][elemento.get_attribute('atributo')] = elemento.text

sleep(3)
print(dici)


sleep(1)
navegador.quit()

os._exit(0)