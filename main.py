"""
* Módulo 20 - Pesquisando no Google com Python
* Criado por Marcos Fabricio Sizanosky
* Professor: Jefferson Santos
* Data criação: 02/06/2021
  Programa em Python 3 para realizar pesquisas no Google.
"""
from googlesearch import search
print("Hello World!")

#  Cabeçalho.
titulo = "Pesquisa Google - Python"
print(f'\n{"*" * len(titulo) + 10 * "*"}')
print(f"++++ {titulo} ++++")
print(f'{"*" * len(titulo) + 10 * "*"}\n')

#  Entrada usuário.
palavra_pesquisa = input("O que você deseja pesquisar no Google hoje? ")
print(palavra_pesquisa)

#  Atribui o retorno(lista) da pesquisa a uma variável.
#  Parâmetros possíveis para a função - search(query, tld='com', lang='en', tbs='0', safe='off', num=10, start=0,
#            stop=None, pause=2.0, country='', extra_params=None,
#            user_agent=None, verify_ssl=True)

lista_urls = search(palavra_pesquisa, tld='com.br', stop=10, pause=2.0, verify_ssl=False)
#  Objeto iterável.
print(lista_urls)
print()
print("++++ Resultados mais relevantes(10) ++++")
#  Percorre uma lista e imprime os resultados na tela.
for link in lista_urls:
    print(link)
