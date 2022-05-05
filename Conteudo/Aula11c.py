from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from time import sleep

navegador = Firefox()

url = 'http://selenium.dunossauro.live/aula_11_b'

navegador.get(url)
sleep(10)

navegador.current_window_handle # id da janela atual.
winds = navegador.window_handles # ids de todas as janelas.

def find_window(url: str):
    for window in winds:
        sleep(2)
        navegador.switch_to.window(window)
        if url in navegador.current_url:
            break

find_window('selenium.dunossauro')