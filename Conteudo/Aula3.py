from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import os

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

navegador = Firefox()
navegador.get(url)

sleep(5)

a = navegador.find_element(by=By.TAG_NAME, value='a')
p = navegador.find_element(by=By.TAG_NAME, value='p')

click = 0

p = navegador.find_elements(by=By.TAG_NAME, value='p')
print(f'click número: {click} e P = {p[-1].text}' )
print(f'Os valores são iguais? {p[-1].text == str(a.click)}')

for click in range(1, 10):
    a.click()
    p = navegador.find_elements(by=By.TAG_NAME, value='p')
    print(f'click número: {click} e P = {p[-1].text}' )
    print(f'Os valores são iguais? {p[-1].text == str(click)}')

p = navegador.find_elements(by=By.TAG_NAME, value='p')    

#print(f'texto de p é: {p.text}')
#print('texto de a é: ' + a.text)

x = p[-1]
print('P final: ' + x.text)
print('Tamanho de P: ' + str(len(p)))

sleep(1)
navegador.quit()

os._exit(0)