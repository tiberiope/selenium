from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_any_elements_located

url = 'https://selenium.dunossauro.live/aula_10_b.html'

navegador = Firefox()

navegador.get(url)

wdw = WebDriverWait(navegador, 60)

locator = (By.TAG_NAME, 'h1')

wdw.until(visibility_of_any_elements_located(locator), 'h1 não foi encontrado')

print("disponível")