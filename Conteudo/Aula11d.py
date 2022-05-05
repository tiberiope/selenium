from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from time import sleep

navegador = Chrome()

url = 'http://selenium.dunossauro.live/aula_11_b'

navegador.get(url)
sleep(40)

navegador.find_element(By.ID, value='popup').click()
print('clicou')
sleep(15)

def find_window(content: str):
    winds = navegador.window_handles
    for window in winds:
        sleep(2)
        navegador.switch_to.window(window)
        if content in navegador.page_source.lower():
            break

find_window('popup')

