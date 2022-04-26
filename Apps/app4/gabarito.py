from selenium.webdriver import Firefox
from time import sleep
from urllib.parse import urlparse, parse_qsl
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.live/exercicio_04.html'

f = Firefox()

f.get(url)

sleep(10)

form = {
    'nome': f.find_element(By.NAME, value='nome'),
    'email': f.find_element(By.NAME, value='email'),
    'senha': f.find_element(By.NAME, value='senha'),
    'telefone': f.find_element(By.NAME, value='telefone'),
    'btn': f.find_element(By.NAME, value='btn')
}

form['nome'].send_keys('eduardo')
form['email'].send_keys('eduardo@eduardo.com')
form['senha'].send_keys('1q2w3e')
form['telefone'].send_keys('987654321')
form['btn'].click()


# -------------- parte 2
sleep(5)
dict_text_area = eval(f.find_element(By.TAG_NAME, value='textarea').text)

print(parse_qsl(urlparse(f.current_url).query))
dict_text_url = dict(parse_qsl(urlparse(f.current_url).query))

dict_text_url.pop('btn')


assert dict_text_area == dict_text_url