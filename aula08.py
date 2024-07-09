print("Exemplo range só com valor final")
list(range(5))
print(list(range(5)), "\n")

print("Exemplo com começo e fim")
list(range(2,12))
print(list(range(2,12)), "\n")

print("Exemplo com começo, fim e intervalo")
list(range(2,12,2))
print(list(range(2,12,2)), "\n")

print("Exemplo Break")
valor = 0
for valor in range(10):
    if valor == 5:
        break #break - para aqui!
    print("valor = " + str(valor))
print("Out of loop\n")

print("Exemplo Break")
var = 10
while var > 0:
    print("Valor atual:", var)
    var = var - 1
    if var == 5:
        break #break - para aqui!
print("Fim!\n")

print("Exemplo Break")
alunos = ["Silvia", "Tina", "Gil", "Davi", "Ryan", "Teco"]
for i in range(len(alunos)):
    print(alunos[i])
    if alunos[i] == "Davi":
        print("Achamos o Davi!")
        break #break - para aqui!
print("Loop terminou!\n")

print("Exemplo Continue")
valor = 0
for valor in range(10):
    if valor == 5:
        continue #continue - para aqui!
    print("Valor = " + str(valor))
print("Out of Loop\n")

print("Exemplo Pass")
valor = 0
for valor in range(10):
    if valor == 5:
        pass #pass here
    print("Valor = " + str(valor))
print("Out of Loop\n")

print("\n1)")
lista1 = []
var = 4
for i in range(18):
    if var % 2 == 0:
        lista1.append(var)
    var = var + 1
print(lista1)

print("\n2)")
nota = float(input("Digite uma nota de 0 a 10: "))
while nota < 0 or nota > 10:
    nota = float(input("Nota invalida, tente novamente: "))
print("Nota armazenada com sucesso!")

print("\n3)")
user = input("Digite o seu usuario: ")
senha = input("Digite a sua senha: ")
while senha == user:
    senha = input("Senha identica ao usuario, tente novamente: ")
print("Usuario e senha armazenados com sucesso!")

print("\n4)")
nome = input("Digite o seu nome: ")
while len(nome) <= 3:
    nome = input("Nome invalido, tente novamente: ")
idade = int(input("Digite a sua idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade invalida, tente novamente: "))
salario = float(input("Digite o seu salario: "))
while salario < 0:
    salario = float(input("Salario invalido, tente novamente: "))
sexo = input("Digite o seu sexo(F ou M): ")
while sexo != 'f' and sexo != 'm':
    sexo = input("Sexo invalido, tente novamente: ")
print("Estado Civil")
print("S - Solteiro(a)")
print("C - Casado(a)")
print("V - Viuvo(a)")
print("D - Divorciado(a)")
ecivil = input("Digite o seu Estado Civil: ")
while ecivil != 's' and ecivil != 'c' and ecivil != 'v' and ecivil != 'd':
    ecivil = input("Estado Civil invalido, tente novamente: ")
print("Informações armazenadas com sucesso, Obrigado!")

print("\n5)")
idade = []
sexo = []
maioridade = 0
homens = 0
mulheres = 0

while (1):
    idade.append(int(input("Digite a idade: ")))
    print("Digite o sexo")
    sexo.append(input("M para Mulher ou H para Homem: "))
    opcao = input("Deseja continuar(S/N): ")
    if opcao == 'N' or opcao == 'n':        
        break
for i in range(len(idade)):
    if idade[i] >= 18:
        maioridade += 1
        if sexo[i].lower() == 'h':
            homens += 1
        elif sexo[i].lower() == 'm':
            mulheres += 1
print("Maioridade:", maioridade, "pessoas com mais de 18 anos")
print("Homens:", homens)
print("Mulheres:", mulheres)

print("\n6)")
produto = []
valor = []

while (1):
    produto.append(input("Digite o nome do produto: "))
    valor.append(float(input("Digite o valor do produto: ")))
    opcao = input("Deseja continuar(S/N): ")
    if opcao == 'N' or opcao == 'n':        
        break
print("O produto mais barato é:", produto[valor.index(min(valor))])
print("O produto mais caro é:", produto[valor.index(max(valor))])
print("O valor total de sua lista de compras é:", sum(valor), "reais!")