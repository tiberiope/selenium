from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from json import load, loads


url = 'http://selenium.dunossauro.live/aula_05.html'
navegador = Firefox()

navegador.get(url)

def preenche_form(navegador, nome, email, senha, telefone):
    navegador.find_element(By.NAME, value='nome').send_keys(nome)
    navegador.find_element(By.NAME, value='email').send_keys(email)
    navegador.find_element(By.NAME, value='senha').send_keys(senha)
    navegador.find_element(By.NAME, value='telefone').send_keys(telefone)
    sleep(5)
    navegador.find_element(By.NAME, value='btn').click()

sleep(5)

estrutura = {
    'nome': 'Artur',
    'email': 'eu@eu.com',
    'senha': 'abcd',
    'telefone': '987654321'
}

preenche_form(navegador, **estrutura)
sleep(3)

# loads(resultado.text.replace('\'', "\""))
resultado = navegador.find_element(By.ID, value='result').text
resultado = resultado.replace('\'', "\"")
print(resultado)
dic_resultado = loads(resultado)
print(dic_resultado)


assert dic_resultado == estrutura