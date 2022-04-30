from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.live/aula_09_a.html'

navegador = Firefox()
navegador.get(url)
navegador.implicitly_wait(15)

botao = navegador.find_element(By.CSS_SELECTOR, value='button')
botao.click()

sucesso = navegador.find_element(By.CSS_SELECTOR, value='#finished')
assert sucesso.text == 'Carregamento concluído'