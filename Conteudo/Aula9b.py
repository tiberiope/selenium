from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def esperar_botao(webdriver):
    elementos = webdriver.find_elements(By.CSS_SELECTOR, value='button')
    print('tentando')
    return bool(elementos)


def esperar_sucesso(webdriver):
    elementos = webdriver.find_elements(By.CSS_SELECTOR, value='#finished')
    print('tentando 2')
    return bool(elementos)


url = 'https://selenium.dunossauro.live/aula_09_a.html'

navegador = Firefox()

wdw = WebDriverWait(navegador, 15, poll_frequency=0.5)
navegador.get(url)

wdw.until(esperar_botao, 'Não achou')

navegador.find_element(By.CSS_SELECTOR, value='button').click()

wdw.until(esperar_sucesso, 'Não achou 2')

sucesso = navegador.find_element(By.CSS_SELECTOR, value='#finished')

assert sucesso.text == 'Carregamento concluído'