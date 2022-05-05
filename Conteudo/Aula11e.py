from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from time import sleep

navegador = Chrome()

url = 'http://selenium.dunossauro.live/aula_11_c'

navegador.get(url)
sleep(3)

print('Janelas: ' + str(len(navegador.window_handles)))
navegador.find_element(By.TAG_NAME, value='button').click()

sleep(3)

print('Janelas: ' + str(len(navegador.window_handles)))

