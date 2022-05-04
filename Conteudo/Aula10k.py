from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value

url = 'https://selenium.dunossauro.live/aula_10_d.html'

navegador = Firefox()

navegador.get(url)

wdw = WebDriverWait(navegador, 120)

locator = (By.TAG_NAME, 'h4')
locator_nome = (By.CSS_SELECTOR, 'input[name="nome"]')

wdw.until(text_to_be_present_in_element_value(locator_nome, 'disponível'))
navegador.find_element(*locator_nome).send_keys('Artur')

wdw.until(text_to_be_present_in_element_value(('css selector', 'input[name="email"]'), 'disponível'))
navegador.find_element(By.CSS_SELECTOR, value='input[name="email"]').send_keys('eu@eu.com')
