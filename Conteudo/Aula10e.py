from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of

url = 'https://selenium.dunossauro.live/aula_10_b.html'

navegador = Firefox()

navegador.get(url)

wdw = WebDriverWait(navegador, 70)

element = navegador.find_element(By.TAG_NAME, value='button')

try:
    wdw.until(staleness_of(element))
except:
    print('botão não clicável apesar de ' + str(element.is_enabled()))

element.click()

p = navegador.find_element(By.TAG_NAME, value='p')

assert 'quei' in p.text