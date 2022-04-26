from json import load, loads

x = 'nome=Artur&email=eu%40eu.com&senha=abcd&telefone=987654321&btn=Enviar%21'

def transforma_url(url):
    url = url.replace('&', '\", \"')
    url = url.replace('=', '\" : \"')
    url = url.replace('%40', '@')
    url = '{\"' + url + '\"}'
    dic_resultado = loads(url)

    del dic_resultado['btn']

    return dic_resultado
