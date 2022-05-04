from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of

url = 'https://selenium.dunossauro.live/aula_10_b.html'

navegador = Firefox()

navegador.get(url)

wdw = WebDriverWait(navegador, 60)

wdw.until(visibility_of(navegador.find_element(By.TAG_NAME, value='h1')), 'h1 não encontrado.')

print("disponível")