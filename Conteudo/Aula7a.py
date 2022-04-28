from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.by import By

navegador = Firefox()
url = 'http://selenium.dunossauro.live/aula_07_d.html'
navegador.get(url)
sleep(5)

input_texto = navegador.find_element(By.TAG_NAME, value='input')
span = navegador.find_element(By.TAG_NAME, value='span')
p = navegador.find_element(By.TAG_NAME, value='p')

input_texto.click()
assert 'está com foco' == span.text, 'não ok1'
span.click()
assert 'está sem foco' == span.text, 'não ok2'

assert p.text == '0', 'não ok3'
input_texto.send_keys('teste')
span.click()
assert p.text == '1', 'não ok4'

sleep(3)
navegador.quit()