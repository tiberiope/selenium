from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import url_changes

url = 'https://selenium.dunossauro.live/aula_10_c.html'

navegador = Firefox()

navegador.get(url)

wdw = WebDriverWait(navegador, 70)

link = navegador.find_element(By.CSS_SELECTOR, value='.body_b a')
link.click()

wdw.until(url_changes(url))

print(url, navegador.current_url)