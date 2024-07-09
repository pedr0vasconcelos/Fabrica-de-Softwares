import math

print("1)")
nome1 = input("Digite o seu nome: ")
print("Seja bem-vindo,",nome1,"!")

print("\n2)")
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
raiz1 = math.sqrt(n1)
raiz2 = math.sqrt(n2)
print("Soma: ", n1+n2)
print("Subtração: ", n1-n2)
print("Resto: ", n1%n2)
print("Raiz do Primeiro número: ",raiz1)
print("Raiz do Segundo número: ", raiz2)

print("\n3)")
algo = input("Digite algo: ")
print("O que você digitou é do tipo: ", type(algo))

print("\n4)")
numero = int(input("Digite um numero qualquer: "))
print("Dobro:",  numero * 2)
print("Triplo:", numero * 3)
print("Raiz Quadrada:", math.sqrt(numero))

print("\n5)")
notas = []
for i in range(1, 4):
    nota = float(input("Digite a {}ª nota do aluno: ".format(i)))
    notas.append(nota)
media = sum(notas) / len(notas)
print("Aluno ficou com média:", media)

print("\n6)")
notas = []
for i in range(1, 4):
    nota = float(input("Digite a {}ª nota do aluno: ".format(i)))
    notas.append(nota)
produto = math.prod(notas)
mediaGeometrica = produto ** (1/len(notas))
print("Aluno ficou com média:", mediaGeometrica)

print("\n7)")
medida = float(input("Digite o valor em Metros a ser convertido: "))
print("KM: ", medida / 1000)
print("MM: ", medida * 1000)

print("\n8)")
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
imc = peso / (altura ** 2)
if(imc < 18.5):
    print("Você recebeu magreza como classificação de IMC")
elif(imc >= 18.5 and imc <= 24.9):
    print("Seu IMC está normal")
elif(imc >= 25 and imc <= 29.9):
    print("Você recebeu sobrepreso como classificação de IMC")
elif(imc >= 30 and imc <= 39.9):
    print("Você recebeu obesidade como classificação de IMC")

print("\n9)")
dinheiro = float(input("Digite o valor em reais a ser convertido: "))
print("Dolar: {:.2f}".format(dinheiro / 5.66))
print("Euros: {:.2f}".format(dinheiro / 6.09))

print("\n10)")
lado1 = float(input("Digite o comprimento da sala: "))
lado2 = float(input("Digite a largura da sala: "))
print("Sua sala tem ", lado1*lado2, "M²")

print("\n11)")
valor = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o desconto do produto: "))
print("Preço com desconto:", valor - (valor * (desconto / 100)))

print("\n12)")
salario = float(input("Digite o seu salario: "))
aumento = float(input("Digite a porcentagem de aumento: "))
novoSalario = salario + (salario * (aumento / 100))
print("Seu novo salario é:", novoSalario)
print("Você ganha: {:.2f}".format(novoSalario / 30), "por dia")

print("\n13)")
temperatura = float(input("Digite a temperatura em graus Celsius: "))
print("Fahrenheit:", (temperatura * 1.8) + 32)
print("Kelvin:", temperatura + 273.15)

print("\n14)")
dias = int(input("Digite quantidade de dias alugados: "))
kmRodado = int(input("Digite a quantidade de KM rodados: "))
total = (dias * 30) + (kmRodado * 0.8)
print("O aluguel do veiculo ficou num total de: R${:.2f} reais".format(total))