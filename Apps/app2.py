from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
import os


url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

navegador = Firefox()
navegador.get(url)

sleep(5)

tag_p = navegador.find_elements(by=By.TAG_NAME, value='p')
ult_p = tag_p[-1].text

num_p = [int(cont)for cont in ult_p.split() if cont.isdigit()]
num_v = num_p[0]

valor_click = -1
tag_a = navegador.find_element(by=By.TAG_NAME, value='a')

while num_v != valor_click:
    
    tag_a.click()
    tag_p = navegador.find_elements(by=By.TAG_NAME, value='p')
    try:
        valor_click = int(tag_p[-1].text)
    except:
        print(tag_p[-1].text)
        valor_click = num_v

sleep(3)
navegador.quit()
os._exit(0)
