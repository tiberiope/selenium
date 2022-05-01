from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial

url = 'https://selenium.dunossauro.live/exercicio_09.html'
navegador = Firefox()
navegador.get(url)
navegador.implicitly_wait(15)

def esperar_elemento(by1, elemento1, webdriver):
    botao = webdriver.find_element(by1, value=elemento1)
    
    try:
        botao.click()
    except:
        pass

    return botao

wdw = WebDriverWait(navegador, 60, poll_frequency=0.01)

fim = wdw.until(partial(esperar_elemento, By.CSS_SELECTOR, '[class*="selenium"]'), "timeout")

if fim:
    print('Conseguiu: ' + fim.get_attribute('class'))