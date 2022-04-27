from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.by import By

navegador = Firefox()
url = 'http://selenium.dunossauro.live/exercicio_05.html'
navegador.get(url)
sleep(5)

nome_form = navegador.find_element(By.CSS_SELECTOR, value='header span').text

while 'Mentira' not in nome_form:
    formulario = navegador.find_element(By.CSS_SELECTOR, value='[class*=' + nome_form + ']')

    formulario.find_element(By.CSS_SELECTOR, value='[name="nome"]').send_keys('Artur')
    formulario.find_element(By.CSS_SELECTOR, value='[name="senha"]').send_keys('abcd')
    sleep(3)
    formulario.find_element(By.CSS_SELECTOR, value='[name="' + nome_form + '"]').click()
    sleep(3)
    nome_form = navegador.find_element(By.CSS_SELECTOR, value='header span').text

sleep(3)
navegador.quit()