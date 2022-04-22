from urllib.parse import urlparse
from selenium.webdriver import Firefox
from time import sleep
import os
from paginas import pag0, pag1, pag2, pag3, pag4

url = 'https://selenium.dunossauro.live/exercicio_03.html'

navegador = Firefox()
navegador.get(url)

sleep(5)

pag0(navegador)
pag1(navegador)
sleep(15)
pag2(navegador)
pag3(navegador)
pag4(navegador)


    

sleep(5)

navegador.quit()
os._exit(0)