# -*- coding: utf-8 -*-
"""Aula07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Iq1VAcOa9VsnExqts9Dtoz_v6zGSsGyv
"""

def saudacao():
    print("Olá,")
    print("Mundo!")

for i in range(5):
    if i < 3:
        print("Menor que 3")
    else:
        print("Igual ou maior que 3")

import random as r
numero_aleatorio = r.random()
print(numero_aleatorio)

import pandas as pd
pd.__version__ # Verifica a versão atual importada

contador = 1
while contador <= 50:
  print("Contador -", contador)
  contador += 3

for x in range (15,2,-3):
  print("contador -", x)

senha_correta = "123"
chances = 3

while chances > 0:
  senha = input("Digite uma senha: ")
  if senha == senha_correta:
      print("Pode acessar.")
      break
  else:
    chances -= 1
    print("Senha errada.")

  if chances == 0:
    print("Acabaram suas tentativas.")

senha_correta2 = "123"
senha1 = input("Digite sua senha: ")
if senha1 == senha_correta2:
 print("Pode acessar.")
else:
  senha2 = input("A senha digitada estava incorreta, digite sua senha novamente: ")
  if senha2 == senha_correta2:
    print("Pode acessar")
  else:
    senha3 = input("Senha incorreta, última tentativa antes de seu acesso ser bloqueado, digite sua senha: ")
    if senha3 == senha_correta2:
      print("Pode acessar.")
    else:
      print("Você digitou a senha errada três vezes, seu acesso foi bloqueado!")

# **Exercício 1: Contagem regressiva simples**
# Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".
contador = 10
while contador >= 1:
  print(contador)
  contador -= 1
  if contador == 0:
    print("Fogo!")

# **Exercício 2: Soma de números pares**
# Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.
usuario = input("Digite um numero inteiro positivo: ")
int_usuario = int(usuario)
numeros = list(range(2,int_usuario+1,2))
soma = sum(numeros)
print(soma)

# **Exercício 3: Tabuada de multiplicação**
# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
usuario = input("Digite um numero inteiro: ")
int_usuario = int(usuario)
resumo = print("O resultado da tabuada do número inserido ("+usuario+") é: ")
mult1 = print(int_usuario*1)
mult2 = print(int_usuario*2)
mult3 = print(int_usuario*3)
mult4 = print(int_usuario*4)
mult5 = print(int_usuario*5)
mult6 = print(int_usuario*6)
mult7 = print(int_usuario*7)
mult8 = print(int_usuario*8)
mult9 = print(int_usuario*9)
mult10 = print(int_usuario*10)

# **Exercício 3: Tabuada de multiplicação**
# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
usuario = input("Digite um numero inteiro: ")
int_usuario = int(usuario)
resumo = print("O resultado da tabuada do número inserido ("+usuario+") é: ")
multiplicador = 1
while multiplicador < 11:
  print(int_usuario*multiplicador)
  multiplicador += 1

# **Exercício 4: Números ímpares reversos**
# Exiba uma contagem regressiva de números ímpares de 99 a 1.
numeros = range(99,0,-2)
lista = list(numeros)
print(lista)

# **Teste o Random:**

import random as r

#1 - Crie um número aleatório de 10, 5
numero = r.random()
print(numero)

#2 - Crie 3 números aleatórios
number1 = r.randint(1,25)
number2 = r.randint(1,25)
number3 = r.randint(1,25)
print("Os 3 números aleatórios gerados foram: " + str(number1) + ", " + str(number2) + ", " + str(number3))

#3 - Crie um número aleatório entre 10 e 30 utilize o range()
number4 = r.randrange(10,30)
print(number4)