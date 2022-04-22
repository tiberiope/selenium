import funcoes
from time import sleep
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

# Pag 0:
def pag0(navegador):
    elementos_a = funcoes.busca_tags(navegador, 'a')
    elemento_a = funcoes.busca_texto(elementos_a, 'Começar por aqui')
    elemento_a.click()

# Pag 1:
def pag1(navegador):
    sleep(3)
    elemento_main = funcoes.busca_tags(navegador, 'main')
    elementos_p = funcoes.busca_tags(elemento_main[0], 'p')
    elementos_a = funcoes.busca_tags(elemento_main[0], 'a')

    numeros = [int(num)for num in elementos_p[1].text.split() if num.isdigit()]
    mult = (numeros[0] * numeros[1])

    texto = funcoes.busca_texto(elementos_p, 'contrário')

    if not texto:
        for elem_tag in elementos_a:
            if int(elem_tag.text) != mult:
                elem_tag.click()
                sleep(15)
                break
    else:
        for elem_tag in elementos_a:
            if int(elem_tag.text) == mult:
                elem_tag.click()
                break

# Pag 2:
def pag2(navegador):
    titulo = navegador.title
    elementos_a = funcoes.busca_tags(navegador, 'a')

    for elemento_a in elementos_a:
        if elemento_a.text == titulo:
            elemento_a.click()
            break

def pag3(navegador):
    sleep(1)
    url = urlparse(navegador.current_url)
    
    elementos_a = funcoes.busca_tags(navegador, 'a')
    
    for elemento_a in elementos_a:
        if elemento_a.text in url.path:
            elemento_a.click()
            break

def pag4(navegador):
    sleep(3)
    navegador.refresh()
    

    