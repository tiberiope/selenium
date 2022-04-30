from selenium.webdriver import Firefox
import funcoes
from time import sleep

url = 'https://selenium.dunossauro.live/exercicio_10.html'
navegador = Firefox()
navegador.get(url)



nome_tarefa = 'Fazer a barba.'
descricao_tarefa = 'Fazer a barba pela manhã, no sábado.'
funcoes.preencher_tarefa(navegador, nome_tarefa, descricao_tarefa)
sleep(2)
print('1')
funcoes.mudar_tarefa(navegador)
sleep(2)
print('2')
funcoes.mudar_tarefa(navegador)
sleep(2)
print('3')
funcoes.mudar_tarefa(navegador)
sleep(2)
print('4')
funcoes.mudar_tarefa(navegador)
sleep(2)
print('5')
funcoes.mudar_tarefa(navegador)

