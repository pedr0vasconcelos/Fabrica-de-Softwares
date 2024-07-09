import time
import random
"""
def quadrado(n):
    return n ** 2
print("O número 13 elevado ao quadrado é", quadrado(13))

def quociente_resto(x, y):
    quociente = x // y
    resto = x % y
    return (quociente, resto)
print("Quociente e resto", quociente_resto(18, 5))
print("Esse print aparece de forma imediata")
#time.sleep(5)
print("Esse print aparece depois de 5 segundos")
x = random.random() #Numero aleatorio float
print(x)
x = random.randint(1, 10) #Numero aleatorio inteiro
print(x)
y = random.randrange(0, 100, 3) #aleatorio de 0 a 100 divisivel por 3
print(y)
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
print(random.choice(lista))
random.shuffle(lista)
print(lista)
"""
print("\n1 e 2)")
lista = []
for i in range(5):
    lista.append(input("Digite um nome: "))
print("A pessoa sorteada foi:", random.choice(lista))
random.shuffle(lista)
print("A ordem da apresentação sera:", lista)

print("\n3)")
x = random.randint(1, 10)
sorteio = int(input("Adivinhe o número de 1 a 10: "))
if sorteio == x:
    time.sleep(5)
    print("Você acertou!")
else:
    time.sleep(5)
    print("Você errou! O número sorteado foi", x)

print("\n4)")
computador = random.randint(1, 3)
def jogo(n):
    if n == computador:
        return "Empate!"
    elif n == 1 and computador == 2:
        return "Você Ganhou!, Computador escolheu Pedra!"
    elif n == 1 and computador == 3:
        return "Você Perdeu!, Computador escolheu Tesoura!"
    elif n == 2 and computador == 1:
        return "Você Perdeu!, Computador escolheu Papel!"
    elif n == 2 and computador == 3:
        return "Você Ganhou!, Computador escolheu Tesoura!"
    elif n == 3 and computador == 1:
        return "Você Ganhou!, Computador escolheu Papel"
    elif n == 3 and computador == 2:
        return "Você Perdeu!, Computador escolheu Pedra!"
while (1):
    print("1 - Papel")
    print("2 - Pedra")
    print("3 - Tesoura")
    jogador = int(input("Escolha sua jogada: "))
    print(jogo(jogador))
    opcao = input("Deseja continuar(S/N): ")
    if opcao == 'N' or opcao == 'n':        
        break
print("Até a próxima!")

print("\n5)")
produto = []
valor = []
while (1):
    produto.append(input("Digite o nome do produto: "))
    valor.append(float(input("Digite o valor do produto: ")))
    opcao = input("Deseja continuar adicionando produtos?(S/N): ")
    if opcao == 'N' or opcao == 'n':        
        break
print("O produto mais barato é:", produto[valor.index(min(valor))])
print("O produto mais caro é:", produto[valor.index(max(valor))])
print("O valor total de sua lista de compras é:", sum(valor), "reais!")
