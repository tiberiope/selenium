from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


url = 'http://selenium.dunossauro.live/aula_05_a.html'
navegador = Firefox()

navegador.get(url)

div_1 = navegador.find_element(By.TAG_NAME, value='div')
print(div_1.text)

div_1 = navegador.find_element(By.ID, value='python')

print(div_1.find_element(By.TAG_NAME, value='p').text)