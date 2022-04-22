from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox


def busca_tags(navegador, tag):

    elementos = navegador.find_elements(By.TAG_NAME, value=tag)
    return elementos
        

def busca_texto(elementos, texto):

    for elemento in elementos:
        if elemento.text == texto:
            return elemento



