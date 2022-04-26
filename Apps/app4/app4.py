from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from transforma_url import transforma_url
from json import load, loads

url = 'https://selenium.dunossauro.live/exercicio_04.html'
navegador = Firefox()

navegador.get(url)

def preencher_formulario(navegador, nome, email, senha, telefone):
    navegador.find_element(By.NAME, value='nome').send_keys(nome)
    navegador.find_element(By.NAME, value='email').send_keys(email)
    navegador.find_element(By.NAME, value='senha').send_keys(senha)
    navegador.find_element(By.NAME, value='telefone').send_keys(telefone)
    navegador.find_element(By.NAME, value='btn').click()

sleep(10)
preencher_formulario(navegador, 'Artur', 'eu@eu.com', 'abcd', '987654321')
sleep(5)

resultado = navegador.find_element(By.TAG_NAME, value='textarea').text
resultado = resultado.replace('\'', "\"")
resultado = loads(resultado)

url_parse = urlparse(navegador.current_url)
url_resultado = transforma_url(url_parse.query)

assert url_resultado == resultado

navegador.quit()