
sexo = (input("1)\nDigite H para homem e M para mulher: "))
altura = float(input("Digite a sua altura: "))
idealh = (72.7 * altura) - 58
idealm = (62.1 * altura) - 44.7
if sexo == 'h':
    print("Seu peso ideal é: ", idealh)
if sexo == 'm':
    print("Seu peso ideal é: ", idealm)

n1 = float(input("\n2)\nDigite a primeira nota: "))
while(n1 < 0):
    n1 = float(input("\nNota invalida, tente novamente: "))
n2 = float(input("Digite a segunda nota: "))
while(n2 < 0):
    n2 = float(input("\nNota invalida, tente novamente: "))
n3 = float(input("Digite a terceira nota: "))
while(n3 < 0):
    n3 = float(input("\nNota invalida, tente novamente: "))
media = ((n1 * 1) + (n2 * 1) + (n3 * 2)) / 4
if media > 6:
    print("Média: ", media, "\nVocê foi Aprovado!")
else:
    print("Média: ", media, "\nVocê foi Reprovado!")

print("\n3)")
def menu3():
    print("*** Menu de Operacoes ***")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("*************************")
menu3()
opcao = int(input("Digite a opção desejada: "))
while (opcao < 1 or opcao > 4):
    menu3()
    opcao = int(input("Opcao invalida, tente novamente: "))
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
match opcao:
    case 1:
        print("O resultado da sua Soma é: ", n1+n2)
    case 2:
        print("O resultado da sua Subtração é: ", n1-n2)
    case 3:
        print("O resultado da sua Multiplicação é: ", n1*n2)
    case 4:
        print("O resultado da sua Dvisão é: ", n1/n2)

print("\n4)")
numero = int(input("Digite um numero: "))
match (numero % 3 == 0, numero % 5 == 0):
    case [True, True]:
        print("O seu numero é divisivel por 3 e 5!")
    case [True, False]:
        print("O seu numero é divisivel somente por 3!")
    case [False, False]:
        print("O seu numero não é divisivel por 3 e 5!")
    case [False, True]:
        print("O seu numero é divisivel somente por 5!")

print("\n5)")
l1 = int(input("Digite o valor do primeiro lado: "))
l2 = int(input("Digite o valor do segundo lado: "))
l3 = int(input("Digite o valor do terceiro lado: "))
match (l1 == l2, l1 == l3):
    case [True, True]:
        print("O seu triangulo é equilatero")
    case [True, False]:
        print("O seu triangulo é isosceles")
    case [False, False]:
        print("O seu triangulo é escaleno")

print("\n6)")
def menu6():
    print("*** Escolha a opção ***")
    print("1 - Soma de 2 números.")
    print("2- Diferença entre 2 números (maior pelo menor).")
    print("3- Produto entre 2 números.")
    print("4- Divisão entre 2 números (o denominador não pode ser zero).")
    print("*****************************")
menu6()
opcao = int(input("Opção: "))
while (opcao < 1 or opcao > 4):
    menu6()
    opcao = int(input("Opção invalida, tente novamente: "))
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
match opcao:
    case 1:
        print("O resultado da sua Soma é:", n1+n2)
    case 2:
        print("O resultado da sua Subtração é:", n1-n2)
    case 3:
        print("O resultado da sua Multiplicação é:", n1*n2)
    case 4:
        print("O resultado da sua Dvisão é:", n1/n2)

print("\n7)")
idade = int(input("Digite a sua idade: "))
temposervico = int(input("Digite o tempo de serviço: "))
if idade >= 65 or temposervico >= 30 or idade >= 60 and temposervico >= 25:
    print("Você pode se aposentar!")
else:
    print("Você NÁO pode se aposentar!")

print("\n8)")
def menu8():
    print("*** Tabela de Imposto ***")
    print("1 - MG 7%")
    print("2 - SP 12%")
    print("3 - RJ 15%")
    print("4 - MS 8%")
    print("*************************")
menu8()
opcao = int(input("Digite o estado destino: "))
while (opcao < 1 or opcao > 4):
    menu8()
    opcao = int(input("Opção invalida, tente novamente: "))
valor = int(input("Digite o valor do produto: "))
match opcao:
    case 1:
        print("Em MG, o seu produto com imposto ficou em R$", valor + (valor * 0.07), "reais")
    case 2:
        print("Em SP, o seu produto com imposto ficou em R$", valor + (valor * 0.12), "reais")
    case 3:
        print("Em RJ, o seu produto com imposto ficou em R$", valor + (valor * 0.15), "reais")
    case 4:
        print("Em MS, o seu produto com imposto ficou em R$", valor + (valor * 0.08), "reais")

print("\n9)")
distancia = float(input("Digite a distancia em Km: "))
litros = float(input("Digite os litros de gasolina consumidos: "))
consumo = distancia / litros
match (consumo > 14, consumo <= 14 and consumo >= 8, consumo < 8):
    case [True, False, False]:
        print("Economico")
    case [False, True, False]:
        print("Bom")
    case [False, False, True]:
        print("Gastão")

print("\n10)")
idade = int(input("Digite a sua idade: "))
match (idade >= 6 and idade <= 8, idade >= 9 and idade <= 10, idade >= 11 and idade <= 12, idade >= 13 and idade <= 14, idade >= 15 and idade <= 16, idade >= 16 and idade <= 19, idade < 6 or idade > 19):
    case [True, False, False, False, False, False, False]:
        print("Está classificado(a) como Pre-Mirim")
    case [False, True, False, False, False, False, False]:
        print("Está classificado(a) como Mirim")
    case [False, False, True, False, False, False, False]:
        print("Está classificado(a) como Petiz")
    case [False, False, False, True, False, False, False]:
        print("Está classificado(a) como Infantil")
    case [False, False, False, False, True, False, False]:
        print("Está classificado(a) como Juvenil")
    case [False, False, False, False, False, True, False]:
        print("Está classificado(a) como Junior")
    case [False, False, False, False, False, False, True]:
        print("Fora da faixa etaria, favor procurar os Organizadores")

print("\n11)")
def menu11():
    print("*********** Cardápio ***********")
    print("111 - Hot Dog - R$ 6,00")
    print("112 - X - Burguer - R$ 10,00")
    print("113 - X - Tudo - R$ 16,00")
    print("114 - Espetinho - R$ 8,00")
    print("115 - Fritas - R$ 12,00")
    print("116 - Refrigerante - R$ 5,00")
    print("117 - Suco - R$ 8,00")
    print("*******************************")
menu11()
opcao = int(input("Digite o numero do seu pedido: "))
while (opcao != 111 and opcao and 112 and opcao != 114 and opcao != 115 and opcao != 116 and opcao != 117):
    menu11()
    opcao = int(input("Opção invalida, tente novamente: "))
quantidade = int(input("Digite a quantidade: "))
match opcao:
    case 111:
        print("O valor a ser pago é:", quantidade * 6, "reais!")
    case 112:
        print("O valor a ser pago é:", quantidade * 10, "reais!")
    case 113:
        print("O valor a ser pago é:", quantidade * 16, "reais!")
    case 114:
        print("O valor a ser pago é:", quantidade * 8, "reais!")
    case 115:
        print("O valor a ser pago é:", quantidade * 12, "reais!")
    case 116:
        print("O valor a ser pago é:", quantidade * 5, "reais!")
    case 117:
        print("O valor a ser pago é:", quantidade * 8, "reais!")

print("\n12)")
preco = float(input("Digite o preço antigo: "))
if preco <= 50:
    print("Seu produto sofreu aumento de 5%. O novo preço é:", preco + (preco * 0.05), "reais")
elif preco > 50 and preco <= 100:
    print("Seu produto sofreu aumento de 10%. O novo preço é:", preco + (preco * 0.10), "reais")
elif preco > 100:
    print("Seu produto sofreu aumento de 15%. O novo preço é:", preco + (preco * 0.15), "reais")
match (preco <= 80, preco > 80 and preco <= 120, preco > 120 and preco <= 200, preco > 200):
    case [True, False, False, False]:
        print("Produto Barato!")
    case [False, True, False, False]:
        print("Produto Normal!")
    case [False, False, True, False]:
        print("Produto Caro!")
    case [False, False, False, True]:
        print("Produto Muito Caro!")

print("\n13)")
salario = float(input("Digite o valor do seu salário: "))
temposervico = int(input("Digite o tempo de serviço em meses: "))
temposervico = temposervico / 12
if salario <= 500:
    print("Seu salário com reajuste é:", salario + (salario * 0.25), "reais")
elif salario <= 1000:
    print("Seu salário com reajuste é:", salario + (salario * 0.20), "reais")
elif salario <= 1500:
    print("Seu salário com reajuste é:", salario + (salario * 0.15), "reais")
elif salario <= 2000:
    print("Seu salário com reajuste é:", salario + (salario * 0.10), "reais")
elif salario > 2000:
    print("Seu salário atual é:", salario, "e não sofreu reajuste")
match (temposervico <= 1, temposervico > 1 and temposervico <= 3, temposervico > 4 and temposervico <= 6, temposervico > 7 and temposervico <= 10, temposervico > 10):
    case [True, False, False, False, False]:
        print("Pelo seu tempo de serviço, ainda não podemos lhe dar um bonus:")
    case [False, True, False, False, False]:
        print("Pelo seu tempo de serviço, você recebeu um bonus de R$ 100,00 reais, seu salário agora é", salario + 100, "reais")
    case [False, False, True, False, False]:
        print("Pelo seu tempo de serviço, você recebeu um bonus de R$ 200,00 reais, seu salário agora é", salario + 200, "reais")
    case [False, False, False, True, False]:
        print("Pelo seu tempo de serviço, você recebeu um bonus de R$ 300,00 reais, seu salário agora é", salario + 300, "reais")
    case [False, False, False, False, True]:
        print("Pelo seu tempo de serviço, você recebeu um bonus de R$ 500,00 reais, seu salário agora é", salario + 500, "reais")