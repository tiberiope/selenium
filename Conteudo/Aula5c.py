from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


url = 'http://selenium.dunossauro.live/aula_05_c.html'
navegador = Firefox()

navegador.get(url)

def melhor_filme(navegador, filme, email, telefone):

    navegador.find_element(By.NAME, value='filme').send_keys(filme)
    navegador.find_element(By.NAME, value='email').send_keys(email)
    navegador.find_element(By.NAME, value='telefone').send_keys(telefone)
    navegador.find_element(By.NAME, value='enviar').click()

melhor_filme(navegador, 'parasita', 'eu@eu.eu', '08133390518')
