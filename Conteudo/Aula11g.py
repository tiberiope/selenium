from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import new_window_is_opened, number_of_windows_to_be
from time import sleep

navegador = Firefox()

url = 'http://selenium.dunossauro.live/aula_11_b'

wdw = WebDriverWait(navegador, 10)

navegador.get(url)
sleep(3)

navegador.execute_script('window.open("")')

sleep(3)

wdw.until(new_window_is_opened(navegador.window_handles))

wdw.until(number_of_windows_to_be(4), 'falhou')

navegador.switch_to.window(navegador.window_handles[-1])

sleep(3)

navegador.get('https://www.google.com')