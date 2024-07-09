import time
import random
import os
import time
from getpass import getpass

print("1)")
n1 = float(input("Digite a primeira nota: "))
while n1 < 0 or n1 > 10:
    n1 = float(input("Nota invalida, tente novamente: "))
print("Nota armazenadas com sucesso!")

print("\n2)")
usuario = input("Digite o seu usuario: ")
senha = getpass("Digite a sua senha: ")
while usuario == senha:
    senha = getpass("Senha identica ao usuario, tente novamente: ")
print("Informações armazenadas com sucesso!")

print("\n3)")
nome = input("Digite o seu nome: ")
while len(nome) <= 3:
    nome = input("Nome invalido, tente novamente: ")
idade = int(input("Digite a sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade invalida, tente novamente: "))
salario = float(input("Digite o seu salario: "))
while salario < 0:
    salario = float(input("Salario invalido, tente novamente: "))
sexo = input("Digite o seu sexo: (F ou M)")
while sexo != 'F' and sexo != 'f' and sexo != 'M' and sexo != 'm':
    sexo = input("Sexo invalido, tente novamente: ")
print("Informações armazenadas com sucesso!")

print("\n4)")
preco4 = 1.99
for quantidade in range(1, 51):
    total = quantidade * preco4
    print("Quantidade:", quantidade, "Preço:", total)

print("\n5)")
preco5 = float(input("Digite o valor do Pão: "))
for quantidade in range(1, 51):
    total = quantidade * preco5
    print("Quantidade:", quantidade, "Preço: {:.2f}".format(total))

print("\n6)")
produto = []
valor = []
opcao = 's'
def menu():    
    print("1 - Listar Produtos")    
    print("0 - Finalizar Compra")
    print("9 - Encerrar Expediente")
while (1):    
    while (opcao == 's' or opcao == 'S'):
        produto.append(input("Digite o nome do produto: "))
        valor.append(float(input("Digite o valor do produto: ")))    
        opcao = input("Deseja continuar registrando? (S/N)")
    menu()
    opcao = input("Opção: ")
    if opcao == '1':
        for i in range(len(produto)):
            print("Produto:", produto[i], " - Valor:", valor[i])
    
    elif opcao == '0':        
            total = sum(valor)                        
            dinheiro = float(input("Digite o valor que deseja usar: "))
            for i in range(len(produto)):
                print("Produto:", produto[i], "- Valor:", valor[i])
            print("Total: R${:.2f}".format(total))
            print("Dinheiro: R${:.2f}".format(dinheiro))
            print("Troco: R${:.2f}".format(dinheiro-total))
            opcao = 's'
            print("Proxima compra em 10 segundos!")
            time.sleep(10)
            os.system('cls')          
    elif opcao == '9':
        print("Te vejo Amanhã!")
        break

print("\n7)")
parcelas = 0
juros = 0
valor_parcela = 0

divida = int(input("Informe o valor de sua divida: "))

print("Valor da Dívida - Juros - Quantidade de Parcelas - Valor da Parcela", )
for parcelas in [1, 3, 6, 9, 12]:
    if parcelas == 3:
        juros = 10
    if parcelas > 3:
        juros += 5
    juros_aplicado = (divida + (divida * juros)/100) - divida
    valor_parcela = (divida + (divida * juros)/100) / parcelas 
    print("R$", divida + (divida * juros)/100, "      - ", "{:.2f}".format(juros_aplicado), "          - ",  parcelas, "           - ", "{:.2f}".format(valor_parcela))

print("\n8)")
produto = ['Cachorro Quente', 'Bauru Simples', 'Bauru Simples']
valor = []
total = 0

def menu():
    print("   Produto        Código  Preço")
    print("Cachorro Quente   - 100 - R$1,20")
    print("Bauru Simples     - 101 - R$1,30")
    print("Bauru com Ovo     - 102 - R$1,50")
    print("Hamburger         - 103 - R$1,20")
    print("Cheeseburguer     - 104 - R$1,30")
    print("Cheeseburguer     - 104 - R$1,30")
    print("Refrigerante      - 105 - R$1,00")
    print("Finalizar Compra  - Digite 0\n")

opcao = 's'
while (opcao == 's' or opcao == 'S'):
    menu()    
    opcao = input("Digite a opção desejada: ")    
    match opcao:
        case '100':
            quantidade = int(input("Digite a quantidade do produto: "))
            total = total + (quantidade * 1.20)
            print("Pedido:", quantidade,"x Cachorro-Quentes, ficou em: R$", total, "reais")
            opcao = input("Deseja continuar comprando? (S/N)")
        case '101':
            quantidade = int(input("Digite a quantidade do produto: "))
            total = total + (quantidade * 1.30)
            print("Pedido:", quantidade,"x Bauru Simples, ficou em: R$", total, "reais")
            opcao = input("Deseja continuar comprando? (S/N)")
        case '102':
            quantidade = int(input("Digite a quantidade do produto: "))
            total = total + (quantidade * 1.50)
            print("Pedido:", quantidade,"x Bauru com Ovo, ficou em: R$", total, "reais")
            opcao = input("Deseja continuar comprando? (S/N)")
        case '103':
            quantidade = int(input("Digite a quantidade do produto: "))
            total = total + (quantidade * 1.20)
            print("Pedido:", quantidade,"x Hamburgers, ficou em: R$", total, "reais")
            opcao = input("Deseja continuar comprando? (S/N)")
        case '104': 
            quantidade = int(input("Digite a quantidade do produto: "))
            total = total + (quantidade * 1.30)
            print("Pedido:", quantidade,"x Cheeseburgers, ficou em: R$", total, "reais")
            opcao = input("Deseja continuar comprando? (S/N)")
        case '105':
            quantidade = int(input("Digite a quantidade do produto: "))
            total = total + (quantidade * 1.00)
            print("Pedido:", quantidade,"x Refrigerantes, ficou em: R$", total, "reais")
            opcao = input("Deseja continuar comprando? (S/N)")
        case '0':            
            break
print("Seu pedido ficou em: R$", total, "reais")

print("\n9)")

aluno_notas = []
aluno = []
gabarito = ['a', 'b', 'c', 'a', 'd', 'e', 'e', 'd', 'c', 'a']
nota = 0
verificador = 's'

while (verificador == 's'):
    for i in range(10):
        aluno.append(input("Digite a sua resposta para Questão: "))
        #while (aluno[i] != 'a' and aluno[i] != 'b' and aluno[i] != 'c' and aluno[i] != 'd' and aluno[i] != 'e'):
            #aluno.append(input("Resposta invalida, tente novamente: "))                
    for i in range(10):
        if aluno[i] == gabarito[i]:
            nota = nota + 1
    aluno_notas.append(nota)
    nota = 0        
    verificador = input("Outro aluno deseja utilizar o sistema? (S/N)")      
    for i in range(10):
        aluno.pop()

media = sum(aluno_notas) / len(aluno_notas)
print("A maior nota foi:", max(aluno_notas))
print("A menor nota foi:", min(aluno_notas))
print("Notas de todos os alunos:", aluno_notas)
print("Sistema foi utilizado por:", len(aluno_notas), "alunos!")
print("Soma de todas as notas:", sum(aluno_notas))
print("A media da turma: {:.2f}".format(media))

print("\n10)")
saltos = []
verificador = 's'

while (verificador == 's'):
    atleta = input("Digite o nome do atleta: ")
    for i in range(5):
        if len(atleta) <= 3:
            verificador = 'n'
            break            
        saltos.append(float(input("Digite a distancia do seu salto: ")))
    verificador = input("Deseja continuar? (S/N)")

print("Atleta: ", atleta[0])
print("Primeiro Salto: ", saltos[0], "m")
print("Segundo Salto: ", saltos[1], "m")
print("Terceiro Salto: ", saltos[2], "m")
print("Quarto Salto: ", saltos[3], "m")
print("Quinto Salto: ", saltos[4], "m")
print("Melhor Salto: ", max(saltos), "m")
print("Pior Salto: ", min(saltos), "m")

saltos.remove(min(saltos))
saltos.remove(max(saltos))

media = sum(saltos) / len(saltos)

print("A media dos saltos do atleta foi: {:.2f} metros".format(media))