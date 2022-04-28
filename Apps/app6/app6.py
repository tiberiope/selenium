from mailbox import NotEmptyError
from selenium.webdriver import Firefox
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import AbstractEventListener, EventFiringWebDriver

class Escuta(AbstractEventListener):
    def before_click(self, element, envolve):
        try:
            print(element.text)
        except:
            print('era o botão.')

        #if element.id != 'btn':
         #   print(element.text)
    
    def after_click(self, element, envolve):
        try:
            print(element.text)
        except:
            print('era o botão.')

        #if element.id != 'btn':
         #   print(element.text)
        

url = 'https://selenium.dunossauro.live/exercicio_07.html'
navegador = Firefox()

envolve = EventFiringWebDriver(navegador, Escuta())
envolve.get(url)

sleep(5)

lnome = envolve.find_element(By.ID, value='lnome')
nome = envolve.find_element(By.NAME, value='nome')
lemail = envolve.find_element(By.ID, value='lemail')
email = envolve.find_element(By.NAME, value='email')
lsenha = envolve.find_element(By.ID, value='lsenha')
senha = envolve.find_element(By.NAME, value='senha')
enviar = envolve.find_element(By.NAME, value='btn')

lnome.click()
nome.send_keys('Artur')
sleep(2)
lemail.click()
email.send_keys('eu@gmail.com')
sleep(2)
lsenha.click()
senha.send_keys('abcd')
sleep(2)
enviar.click()



sleep(3)
navegador.quit()