from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.by import By

navegador = Firefox()
url = 'http://selenium.dunossauro.live/aula_06_a.html'
navegador.get(url)
sleep(5)

# Busca por TAG.
# navegador.find_element(By.CSS_SELECTOR, value='input').send_keys('Artur')

'''
Operadores:
= deve ser exatamente igual.
*= deve ocorrer em.
|= deve ser exatamente ou iniciar.
^= iniciado em.
$= terminado em.
~= um deve ser exatamente igual.
'''

a = navegador.find_elements(By.CSS_SELECTOR, value='div.form-group')
print(len(a))

a = navegador.find_elements(By.CSS_SELECTOR, value='div.form-group + br')
print(len(a))

a = navegador.find_elements(By.CSS_SELECTOR, value='div.form-group > br')[1].get_attribute('id')
print(a)