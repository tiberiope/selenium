from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial


def esperar_elemento(by, elemento, webdriver):
    elementos = webdriver.find_elements(by, value=elemento)
    print(f'tentando encontrar: {elemento}. by: {by}.')
    return bool(elementos)


esperar_botao = partial(esperar_elemento, By.CSS_SELECTOR, 'button')

url = 'https://selenium.dunossauro.live/aula_09_a.html'

navegador = Firefox()

wdw = WebDriverWait(navegador, 30, poll_frequency=0.5)
navegador.get(url)

wdw.until(esperar_botao, 'Não achou')

navegador.find_element(By.CSS_SELECTOR, value='button').click()

wdw.until(partial(esperar_elemento, By.ID, 'finished'), 'Não achou 2')

sucesso = navegador.find_element(By.CSS_SELECTOR, value='#finished')

assert sucesso.text == 'Carregamento concluído'