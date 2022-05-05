from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

navegador = Firefox()

url = 'http://selenium.dunossauro.live/aula_11_a'

navegador.get(url)
sleep(10)

navegador.find_element(By.ID, value='alert').click()

alerta = navegador.switch_to.alert

sleep(3)

alerta.accept()