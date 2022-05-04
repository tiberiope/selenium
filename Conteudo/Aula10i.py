from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support.expected_conditions import url_contains, url_matches, title_is, title_contains

url = 'https://selenium.dunossauro.live/aula_10_c.html'

navegador = Firefox()

navegador.get(url)

wdw = WebDriverWait(navegador, 10)

links = navegador.find_elements(By.CSS_SELECTOR, value='.body_b a')
links[1].click()

wdw.until(url_contains('selenium'))

wdw.until(url_matches('http.*live'))

sleep(3)

navegador.back()
sleep(1)
navegador.refresh()
sleep(3)

wdw.until(title_contains('Aula'))
try:
    wdw.until(title_is('selenium'))
except:
    print('diferente')

print(url, navegador.current_url)

navegador.quit()