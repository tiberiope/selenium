from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from time import sleep

navegador = Firefox()

url = 'http://selenium.dunossauro.live/aula_11_c'

navegador.get(url)
sleep(3)

navegador.execute_script('window.open("_blank")')
navegador.switch_to.window(navegador.window_handles[-1])

sleep(3)

navegador.get('https://www.google.com')



