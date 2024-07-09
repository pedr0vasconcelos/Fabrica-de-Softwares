print("\n1)Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo")
dia = input("Que dia é hoje? ")
if dia == 'domingo' or dia == 'sabado':
    print("Hoje é dia de descanso!")
else:
    print("Você precisa trabalhar!")

print("\n2) Faça um programa que peça a altura e o peso da pessoa. Calcule o IMC e diga se a pessoa está normal, sobrepeso, obesidade,etc")
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
imc = peso/(altura**2)

if(imc < 18.5):
    print("Você recebeu magreza como classificação de IMC")
elif(imc >= 18.5 and imc <= 24.9):
    print("Seu IMC está normal")
elif(imc >= 25 and imc <= 29.9):
    print("Você recebeu sobrepreso como classificação de IMC")
elif(imc >= 30 and imc <= 39.9):
    print("Você recebeu obesidade como classificação de IMC")
else:
    print("Seu IMC está em obesidade grave. Recomendado procurar ajuda médica")

print("\n3)Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:")
n1 = float(input("Digite o primeira nota: "))
n2 = float(input("Digite o segunda nota: "))
media = (n1+n2)/2

if media == 10:
    print("Sua média é", media,"Aprovado com Distinção!")
elif media >= 7:
    print("Sua média é", media,"Aprovado!")
else :
    print("Sua média é", media,"Reprovado!")

print("\n4)Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem Bom Dia!, Boa Tarde! ou Boa Noite! ou Valor Inválido!, conforme o caso.")

print("M - Matutino")
print("V - Vespertino")
print("N - Noturno")
turno = input("Digite a tecla correpondente ao seu turno: ")

if turno == 'm':
    print("Bom Dia!")
elif turno == 'v':
    print("Boa tarde!")
elif turno == 'n':
    print("Boa noite!")
else :
    print("Tecla invalida!")

print("\n5)Faça um programa que peça um número ao usuário. O programa deve indicar se o número é ímpar ou par.")
numero = int(input("Digite um número a ser verificado: "))
if numero % 2 == 0:
    print("O número é par!")
else :
    print("O número é ímpar!")

print("\n6)Faça um programa que lê as duas notas parciais obtidas por um aluno numa \ndisciplina ao longo de um semestre, e calcule a sua média. \nA atribuição de conceitos obedece à tabela abaixo:")
x1 = float(input("Digite o primeira nota: "))
x2 = float(input("Digite o segunda nota: "))
media = (x1+x2)/2

if media >= 9.1 and media <= 10.0:
    print("Você recebeu o conceito A! Está aprovado")
elif media >= 7.5 and media <= 9.0:
    print("Você recebeu o conceito B! Está aprovado")
elif media >= 6.1 and media <= 7.5:
    print("Você recebeu o conceito C! Está aprovado")
elif media >= 4.1 and media <= 6.0:
    print("Você recebeu o conceito D! Está reprovado")
else:
    print("Você recebeu o conceito E! Está reprovado")

print("\nDESAFIO - Você fará um programa de radar eletrônico.\nPergunte a velocidade do carro. Se a velocidade for menor ou igual a 80km/h, o usuário receberá a seguinte mensagem: “Boa viagem!!Você está dentro do limite de velocidade!”. Se a velocidade for maior do que 80 km/h, escreva: Você se encontra acima do limite de 80km/h. Foguete não tem ré mas tem multa. Apresente a multa do indivíduo em reais. O aviso de multa deverá ser escrito em vermelho.A multa é calculada somando 10 reais para cada km acima dos 80.")

speed = int(input("Digite a sua velocidade: "))
multa = (speed-80)*10


if speed <= 80:
    print("Boa viagem!!Você está dentro do limite de velocidade!")
else:
    print("Você se encontra acima do limite de 80km/h. Foguete não tem ré mas tem multa")
    print("Sua multa é de R$", multa, "reais!")