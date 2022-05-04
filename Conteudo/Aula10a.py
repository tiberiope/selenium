from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep
 
url = 'https://selenium.dunossauro.live/aula_10_a.html'

navegador = Firefox()

navegador.get(url)

locator = (By.CSS_SELECTOR, '#request')
wdw = WebDriverWait(navegador, 30)

wdw.until(presence_of_element_located(locator))

navegador.find_element(*locator).click()

print('apareceu!')

sleep(3)

navegador.quit()