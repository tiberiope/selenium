from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element_value

url = 'https://selenium.dunossauro.live/exercicio_11.html'

navegador = Firefox()

navegador.get(url)

wdw = WebDriverWait(navegador, 120)

locator = (By.TAG_NAME, 'h4')
locator_nome = (By.CSS_SELECTOR, 'input[name="nome"]')

wdw.until(text_to_be_present_in_element_value(locator_nome, 'disponível'))
navegador.find_element(*locator_nome).send_keys('Artur')

wdw.until(text_to_be_present_in_element_value(('css selector', 'input[name="email"]'), 'disponível'))
navegador.find_element(By.CSS_SELECTOR, value='input[name="email"]').send_keys('eu@eu.com')

wdw.until(text_to_be_present_in_element_value(('css selector', 'input[name="c_email"]'), 'disponível'))
navegador.find_element(By.CSS_SELECTOR, value='input[name="c_email"]').send_keys('eu@eu.com')

wdw.until(text_to_be_present_in_element_value(('css selector', 'input[name="senha"]'), 'disponível'))
navegador.find_element(By.CSS_SELECTOR, value='input[name="senha"]').send_keys('abcd')

wdw.until(text_to_be_present_in_element_value(('css selector', 'input[name="c_senha"]'), 'disponível'))
navegador.find_element(By.CSS_SELECTOR, value='input[name="c_senha"]').send_keys('abcd')

wdw.until(text_to_be_present_in_element_value(('css selector', 'input[name="button"]'), 'disponível'))
navegador.find_element(By.CSS_SELECTOR, value='input[name="button"]').click()