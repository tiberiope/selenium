from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial


class EsperarElemento:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, webdriver):
        elementos = webdriver.find_elements(*self.locator)
        if elementos:
            return 'unclick' in elementos[0].get_attribute('class')
        return False


def esperar_elemento(by, elemento, webdriver):
    if webdriver.find_elements(by, elemento):
        return True
    return False


locator = (By.CSS_SELECTOR, 'button')
esperar_botao = EsperarElemento(locator)

url = 'https://selenium.dunossauro.live/aula_09.html'

navegador = Firefox()

wdw = WebDriverWait(navegador, 30, poll_frequency=0.5)
navegador.get(url)

wdw.until_not(esperar_botao, 'Não achou')

navegador.find_element(By.CSS_SELECTOR, value='button').click()

wdw.until(partial(esperar_elemento, 'id', 'finished'), 'Não achou 2')

sucesso = navegador.find_element(By.CSS_SELECTOR, value='#finished')

assert sucesso.text == 'Carregamento concluído'