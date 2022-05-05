from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from time import sleep

navegador = Firefox()

url = 'http://selenium.dunossauro.live/aula_11_a'

navegador.get(url)
sleep(10)

navegador.find_element(By.ID, value='alert').click()

alerta = Alert(navegador)

sleep(3)

alerta.accept()

sleep(3)

navegador.find_element(By.ID, value='prompt').click()

alerta.send_keys('Artur')
sleep(3)
alerta.accept()

#-------------------------------

wdw = WebDriverWait(navegador, 30)

sleep(3)
navegador.find_element(By.ID, value='alertd').click()
wdw.until(alert_is_present())
sleep(3)
alerta.accept()