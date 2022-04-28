from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver


class Escuta(AbstractEventListener):
    def before_click(self, elemento, webdriver):
        print(webdriver.find_element(By.TAG_NAME, value='span').text)
        print('antes do click')

    def after_click(self, elemento, webdriver):
        print(webdriver.find_element(By.TAG_NAME, value='span').text)
        print('depois do click')


navegador = Firefox()
rapi_nav = EventFiringWebDriver(navegador, Escuta())
url = 'http://selenium.dunossauro.live/aula_07_d.html'
rapi_nav.get(url)
sleep(5)

input_texto = rapi_nav.find_element(By.TAG_NAME, value='input')
span = rapi_nav.find_element(By.TAG_NAME, value='span')
p = rapi_nav.find_element(By.TAG_NAME, value='p')

input_texto.click()

sleep(3)

rapi_nav.quit()