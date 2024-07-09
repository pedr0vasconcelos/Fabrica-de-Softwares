import math

print("\n1) Faça um programa que peça um número qualquer e diga se ele é um número par ou ímpar.")
n1 = int(input("Digite o número a ser verificado: "))
if n1 % 2 == 0:
    print("O seu número é par!")
else:
    print("O seu número é impar!")

print("\n2) Peça ao usuário 5 valores e diga qual é o maior e qual é o menor deles.")
lista2 = []
contador = 0
while (contador < 5):
    item = int(input("Digite um número: "))
    lista2.append(item)
    contador = contador + 1
print("O maior número é", max(lista2), "e o menor número é", min(lista2))

print("\n3) Peça ao usuário um número e indique se o número é par ou ímpar, se é divisível por 5 ou por 10.")
n3 = int(input("Digite o número a ser verificado: "))
if n3 % 2 == 0 and n3 % 10 == 0:
    print("O seu número é par e divisivel por 10")
elif n3 % 2 == 0:
    print("O seu número é par!")
if n3 % 2 != 0:
    print("O seu número é impar")
if n3 % 5 == 0:
    print("O seu número é divisivel por 5")

aux = 0
print("\n4) Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.")
while aux != 1:
    n4 = int(input("Digite um número: "))
    if n4 > 0:
        print("A raiz quadrada de {} é {}".format(n4, math.sqrt(n4)))
        aux = aux + 1
    else:
        print("O seu número é invalido") 

print("\n5) Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.")
nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0:
    nota1 = float(input("Primeira nota invalida, tente novamente: "))
nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0:
    nota2 = float(input("Segunda nota invalida, tente novamente: "))
media = (nota1 + nota2)/2
print("Sua media é", media)

print("\n6) Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo nâo concedido, caso contrário imprima: Empréstimo concedido")
salario = float(input("Digite o seu salario: "))
emprestimo = int(input("Digite o valor para emprestimo: "))
aux = salario * 0.2
while emprestimo > aux:
    emprestimo = int(input("Emprestimo não concedido, tente novamente: "))
print("Emprestimo concedido!")