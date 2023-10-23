import requests
from bs4 import BeautifulSoup

url_base='https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto voce deseja?')


response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})
contador = 0
for produto in produtos:
    titulo = produto.find('h2', attrs={'class':'ui-search-item__title' })
    link = produto.find('a',attrs={'class': 'ui-search-link'})

    real = produto.find('span',attrs={'class','andes-money-amount__fraction'})
    centavos = produto.find('span',attrs={'class','andes-money-amount__cents andes-money-amount__cents--superscript-24'})
    
    #print(produto.prettify())
    print('Titulo produto:',titulo.text)
    print('Link Produto:',link['href'] )

    if(centavos):
        print('Valor do Produto: R$', real.text +','+ centavos.text)
    else:
        print('Valor do Produto: R$', real.text)
    contador+=1

    print('\n\n')
print(f'total de produtos visualizados:{contador}')