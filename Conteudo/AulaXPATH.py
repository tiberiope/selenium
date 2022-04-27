from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from pprint import pprint

# página de consulta: https://devhints.io/xpath

with open("aulaXPATH.html") as f:
    content = f.read()

from parsel import Selector

response = Selector(text=content)

# print(response.get()) printa todo o conteudo da variável response.

# pega o title dentro de html e de head.
pprint(response.xpath('/html/head/title').getall())

# pega todos os titles do documento.
pprint(response.xpath('//title').getall())
print('-----')
pprint(response.xpath('//h1').getall())

# retorna a tag que está exatamente abaixo.
pprint(response.xpath('//ul/*').getall())
print('-----')
# retorna todas as tags que estão abaixo.
pprint(response.xpath('//ul//*').getall())
print('-----')

pprint(response.xpath('//ol/li[2]').getall())
print('-----')

pprint(response.xpath('(//ol/li)[2]').getall())
print('-----')

pprint(response.xpath('//ol[1]/li[2]').getall())
print('-----')

pprint(response.xpath('//h1/text()').getall())
print('-----')

pprint(response.xpath('//ul[2]/li[3]//text()').getall())
print('-----')

pprint(response.xpath('//link/@href').getall())
print('-----')

pprint(response.xpath('//h1[@data-section]').getall())
print('-----')

pprint(response.xpath("//li[contains(text(), ' de ')]").getall())
print('-----')

pprint(response.xpath("//li[contains(., 'leite')]").getall())
print('-----')

pprint(response.xpath("//li[not(contains(., ' de '))]").getall())
print('-----')

pprint(response.xpath("//tr[not(th)]").getall())
print('-----')

pprint(response.xpath("//span[@data-qtde>='2']").getall())
print('-----')

pprint(response.xpath("//h1[@data-section='ingredients']/parent::div//li").getall())
print('-----')

pprint(response.xpath("//h1[@data-section='ingredients']/following-sibling::ul/li").getall())
print('-----')

pprint(response.xpath("//h2[contains(text(), 'Pudim')]/following-sibling::ul").getall())
print('-----')

pprint(response.xpath("//h1[@data-section='ingredients']/ancestor::html/head/title").getall())
print('-----')

pprint(response.xpath("//h2[contains(text(), 'Pudim') and contains(./preceding-sibling::h1/@data-section, 'ingredients')]").getall())
print('-----')

pprint(response.xpath("//h2[contains(text(), 'Pudim') and contains(./preceding-sibling::h1/@data-section, 'ingredients')]/following-sibling::ul/li").getall())
print('-----')

navegador = Firefox()

navegador.get("https://rennerocha.github.io/xpath/")

navegador.find_elements_by_xpath('//h2')
print([x.text for x in navegador.find_elements_by_xpath("//h2")])
print('-----')

x = navegador.find_elements_by_xpath('//h2')

for y in x:
    print(y.text)
print('-----')
a = navegador.find_elements(By.XPATH, value="//h1[@data-section!='ingredients']")

for b in a:
    print(b.text)