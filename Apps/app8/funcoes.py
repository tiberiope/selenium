from email import header
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial


def preencher_tarefa(navegador, nome_tarefa, descricao_tarefa):

    elemento_nome = navegador.find_element(By.ID, value='todo-name')
    elemento_nome.send_keys(nome_tarefa)

    elemento_tarefa = navegador.find_element(By.ID, value='todo-desc')
    elemento_tarefa.send_keys(descricao_tarefa)

    wdw = WebDriverWait(navegador, 30, poll_frequency=5)
    wdw.until(partial(esperar_elemento, By.ID, 'todo-submit'), 'não conseguiu')   

    body = esperar_body(navegador)

    return body


def mudar_tarefa(navegador):

    wdw3 = WebDriverWait(navegador, 20, poll_frequency=4)
    wdw3.until(partial(esperar_body_header)) 

    botao = navegador.find_element(By.CSS_SELECTOR, value='[class*="btn btn-primary btn-ghost do"]')
    botao.click()


def esperar_header(webdriver):
    print('procurou header')

    header = webdriver.find_elements(By.TAG_NAME, value='header')
    if header:
        print('encontrou header')
        return not True
        
    return not False   


def esperar_body_header(webdriver):
    elems_body = webdriver.find_elements(By.CSS_SELECTOR, value='[class*="body"]')
    
    wdw = WebDriverWait(webdriver, 10, poll_frequency=1)
    retorno = wdw.until_not(partial(esperar_header))
            
    return not retorno


def esperar_body(webdriver2):
    elems_body = webdriver2.find_elements(By.CSS_SELECTOR, value='[class*="body"]') 

    try:
        for body in elems_body:
            if body.find_element(By.TAG_NAME, value='header'):

                return body
    except:
        return False


def esperar_elemento(by1, elemento1, webdriver):
    botao = webdriver.find_element(by1, value=elemento1)
    botao.click()

    wdw2 = WebDriverWait(webdriver, 4, poll_frequency=1)
    
    try:
        retorno = wdw2.until(partial(esperar_body))
    except:
        retorno = False

    return retorno
    
