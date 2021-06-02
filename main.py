"""
* Módulo 20 - Pesquisando no Google com Python
* Criado por Marcos Fabricio Sizanosky
* Professor: Jefferson Santos
* Data criação: 02/06/2021
  Programa em Python 3 para realizar pesquisas no Google.
"""
from googlesearch import search

palavras_pesquisa = input("O que você deseja pesquisar no Google hoje? ")

lista_urls = search(palavras_pesquisa, tld="com.br", lang="pt", stop=10, pause=2)

print(lista_urls)

for link in lista_urls:
    print(link)
