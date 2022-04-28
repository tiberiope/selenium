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

# Procura o exatamente igual.
a = navegador.find_elements(By.CSS_SELECTOR, value='[class="form-group"]')
print(len(a))

# Procura por classe com a ocorrência de form-group.
a = navegador.find_elements(By.CSS_SELECTOR, value='[class*="form-group"]')
print(len(a))

# Procura por type terminado em t.
a = navegador.find_elements(By.CSS_SELECTOR, value='[type$="t"]')
print(len(a))

nome = navegador.find_element(By.CSS_SELECTOR, value='[type="text"]')
print('aqui ' + nome.get_attribute('id'))
senha = navegador.find_element(By.CSS_SELECTOR, value='[type="password"]')
btn = navegador.find_element(By.CSS_SELECTOR, value='[type="submit"]')

a = navegador.find_elements(By.CSS_SELECTOR, value='label, input')

print(len(a))

# pega as tags BR que estiverem no mesmo nível que div (irmãos).
a = navegador.find_elements(By.CSS_SELECTOR, value='div + br')
print(len(a))

# pega as tags DIV que estiverem no mesmo nível de H2 (irmãos).
a = navegador.find_elements(By.CSS_SELECTOR, value='h2 ~ div')
print(len(a))

# pega as tags br filhos da tag div (filhos).
a = navegador.find_elements(By.CSS_SELECTOR, value='div > br')
print(len(a))

# pega as tags br descendentes da tag form (descendentes).
a = navegador.find_elements(By.CSS_SELECTOR, value='form br')
print(len(a))

nome.send_keys('Artur')
senha.send_keys('abcd')
sleep(3)
btn.click()
