# -*- coding: utf-8 -*-
"""
Created on Thu May 25 18:20:32 2023

@author: jurod
"""

#importação do bando de dados
import pandas as pd

#ler o arquivo do Excel
dados_excel = pd.read_excel(r"C:\Users\Fatec\Downloads\filmes-dataset.xlsx")


print("Filmes:")

#acessando a coluna específica dos gêneros pelo número do índice
g = 0
while g < 17:
    nome_coluna = dados_excel.iloc[:, g]
    g += 1
    for valor in nome_coluna:
        if not pd.isna(valor): 
            print(valor) 
    print()
    
    
print("Tamanho das Colunas de Gêneros:")
    
for coluna in dados_excel.columns:
    if dados_excel[coluna].count() > 0:
        print("Coluna:", coluna)
        print("Tamanho:", dados_excel[coluna].count())
        print()

#calculo das probabilidades
total_elementos = 0
for coluna in dados_excel.columns:
    if dados_excel[coluna].count() > 0: 
        total_elementos += dados_excel[coluna].count() 
print("Valor total: ", total_elementos) 
print()

probabilidades = []
for coluna in dados_excel.columns:
    if dados_excel[coluna].count() > 0:
        p = dados_excel[coluna].count() / total_elementos
        probabilidades.append(p)
        print(f"Probabilidades: {p:.3f}") 
print()


#cálculo da entropia

import math

def calcular_entropia(probabilidades):
    entropia = 0
    for p in probabilidades:
        entropia += p * math.log2(p)
    entropia = -entropia
    return entropia

entropia_resultante = calcular_entropia(probabilidades)
print(f"Entropia: {entropia_resultante:.2f}")

#entropia máxima

entropia_máx = math.log2(17)
print(f"Entropia máxima: {entropia_máx:.2f} ")