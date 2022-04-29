from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from pywinauto import keyboard


url = 'https://selenium.dunossauro.live/aula_08_a'
navegador = Firefox()
navegador.get(url)
sleep(5)

texto = 'Artur'

# hi-level
elemento = navegador.find_element(By.NAME, value='texto')

# low-level
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys
ac = ActionChains(navegador)

ac.move_to_element(elemento)
ac.click(elemento)

def digita_com_shift(key):
    ac.key_down(key)

    for letra in texto:
        ac.key_down(letra)
        ac.key_up(letra)

    ac.key_up(key)

def digita_com_caps(key):

    for letra in texto:

        keyboard.send_keys('{CAPSLOCK down}' '{VK_SHIFT down}' + letra)
    
    keyboard.send_keys('{CAPSLOCK up}' '{VK_SHIFT up}')
    keyboard.send_keys('{CAPSLOCK down}')
    keyboard.send_keys('{CAPSLOCK up}')


digita_com_shift(Keys.SHIFT)
ac.perform()


sleep(3)
digita_com_caps(Keys.SHIFT)

ac.perform()

