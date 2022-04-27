from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


url = 'http://selenium.dunossauro.live/aula_05_b.html'
navegador = Firefox()

navegador.get(url)

topico = navegador.find_element(By.CLASS_NAME, value='topico')

print(topico.find_element(By.TAG_NAME, value='h1').text)

linguagens = navegador.find_elements(By.CLASS_NAME, value='linguagens')
print(linguagens[2].text)

for linguagem in linguagens:
    print(linguagem.find_element(By.TAG_NAME, value='h2').text)