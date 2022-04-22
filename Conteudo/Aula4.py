from urllib.parse import urlparse
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
import os     

url = 'https://selenium.dunossauro.live/aula_04.html'

navegador = Firefox()
navegador.get(url)
link = []
lista_aula = {}
sleep(5)


def find_link(elemento, link, lista_aula):
    a = elemento.find_elements(by=By.TAG_NAME, value='a')

    for item in a:
        if 'Aula' in item.text:
            lista_aula[item.text] = item.get_attribute('href')

        if item.get_attribute('href') not in link:
            if item.text == 'Exercício 3':
                exercicio3 = item

            link.append(item.get_attribute('href'))

    return exercicio3
    

def find_by_tag(navegador, tag, link, lista_aula):

    elemento = navegador.find_element(by=By.TAG_NAME, value=tag)
    
    #for elemento in elementos:
    exercicio3 = find_link(elemento, link, lista_aula)
        #break

    return exercicio3
    

exercicio3 = find_by_tag(navegador, 'div', link, lista_aula)

#for item in elementos_a:
for item_chave in lista_aula.keys():
    print(item_chave + ': ' + lista_aula[item_chave])
 

print(len(link))
print(len(lista_aula))

exercicio3.click()
sleep(3)
navegador.back()

#print(elementos_a)
#---------
#x = urlparse(navegador.current_url)

#url_nova = x.scheme + '://' + x.netloc + x.path
#print(url_nova)
#---------

#navegador = Firefox()
#navegador.get(url_nova)
#sleep(3)

#print(navegador.title)
#navegador.refresh()

sleep(3)

navegador.quit()
sleep(2)

os._exit(0)
