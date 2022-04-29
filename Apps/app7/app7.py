from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from pywinauto import keyboard


url = 'https://selenium.dunossauro.live/caixinha'
navegador = Firefox()
navegador.get(url)
sleep(2)

# hi-level
caixa = navegador.find_element(By.ID, value='caixa')
span = navegador.find_element(By.TAG_NAME, value='span')

# low-level
# https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys
ac = ActionChains(navegador)

cores = set()

def add_cor():
    dic = span.text
    dic = dic.replace("\"", "")
    dic = dic.replace(" ", "")
    dic = dic.replace("{", "")
    dic = dic.replace("}", "")
    dic = dict(subString.split(":") for subString in dic.split(","))
    
    cores.add(dic['cor'])

def caixinha_colorida(key1 = None, key2 = None):

    if key1:
        ac.key_down(key1)
    
    if key2:
        ac.key_down(key2)
    
    ac.move_to_element(span)
    ac.perform()
    ac.pause(1)
    add_cor()

    ac.move_to_element(caixa)
    ac.perform()
    ac.pause(1)
    add_cor()

    ac.double_click(caixa)
    ac.perform()
    ac.pause(3)
    add_cor()

    ac.click(caixa)
    ac.perform()
    ac.pause(1)
    add_cor()

    ac.context_click(caixa)
    ac.perform()
    ac.pause(1)
    add_cor()

    ac.move_to_element(span)
    ac.perform()
    ac.pause(1)
    add_cor()

    if key1:
        ac.key_up(key1)

    if key2:
        ac.key_up(key2)

key_enviada1 = ''
key_enviada2 = ''

caixinha_colorida(Keys.CONTROL, key_enviada2)
caixinha_colorida(Keys.SHIFT, key_enviada2)
caixinha_colorida(Keys.SHIFT, Keys.CONTROL)
caixinha_colorida('', '')

print(cores)
