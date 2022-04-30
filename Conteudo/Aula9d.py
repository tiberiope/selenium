import selectors
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial


class EsperarElemento:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, webdriver):
        if webdriver.find_elements(*self.locator):
            return True
        return False

locator = (By.CSS_SELECTOR, 'button')
esperar_botao = EsperarElemento(locator)

url = 'https://selenium.dunossauro.live/aula_09_a.html'

navegador = Firefox()

wdw = WebDriverWait(navegador, 30, poll_frequency=0.5)
navegador.get(url)

wdw.until(esperar_botao, 'Não achou')

navegador.find_element(By.CSS_SELECTOR, value='button').click()

wdw.until(EsperarElemento(locator=('id', 'finished')), 'Não achou 2')

sucesso = navegador.find_element(By.CSS_SELECTOR, value='#finished')

assert sucesso.text == 'Carregamento concluído'