import random

lista = []

"""Item está servindo como variavel temporaria
para atribuir o valor a lista"""

print("\n1) Vamos fazer uma lista de compras. Peça ao usuário 3 produtos, coloque em uma lista e mostre a lista final em um print. (batata,leite e pão)\n")
item = str(input("Digite o primeiro produto: "))
lista.append(item)
item = str(input("Digite o segundo produto: "))
lista.append(item)
item = str(input("Digite o terceiro produto: "))
lista.append(item)

print(lista)

print("\n2) Adicione mais produto à lista sem apagá-la. Adicione: banana,chocolate,cenoura,ervilha,café,sucrilhos,arroz,vinagre,salgadinho e pimenta.")
lista.append('banana')
lista.append('chocolate')
lista.append('cenoura')
lista.append('ervilha')
lista.append('café')
lista.append('sucrilhos')
lista.append('arroz')
lista.append('vinagre')
lista.append('salgadinho')
lista.append('pimenta')
print(lista)

print("\n3) Você é estranho. Não consegue ficar sem colocar a lista em ordem alfabética. Faça isso então.")
lista.sort()
print(lista)

print("\n4) Você é a Dory. Esqueceu se colocou pinhão e cenoura na sua lista. Verifique se estão lá.")
print("Pinhão está na lista?", 'pinhão' in lista)
print("Cenoura está na lista?", 'cenoura' in lista)

print("\n5) Crie uma lista com: 3 strings, 4 números inteiros, 3 números float, duas listas aninhadas.")
lista5 = ['eu', 'tu', 'ele', 1, 2, 3, 4, 5.0, 6.0, 7.0, [8], [9]]
print(lista5)

print("\n6) Crie uma lista com: 2 strings, 3 números inteiros, 2 números float, sendo que os elementos devem ser dados pelo usuário e impressos no final com um print.")
lista6 = []

item = str(input("Digite a primeira String: "))
lista6.append(item)
item = str(input("Digite a segunda String: "))
lista6.append(item)
item = int(input("Digite o primeiro Inteiro: "))
lista6.append(item)
item = int(input("Digite o segundo Inteiro: "))
lista6.append(item)
item = int(input("Digite o terceiro Inteiro: "))
lista6.append(item)
item = float(input("Digite o primeiro Float: "))
lista6.append(item)
item = float(input("Digite o segundo Float: "))
lista6.append(item)
print(lista6)

print("\n7) Faça uma lista com os números a seguir e verifique : 5,4,8,9,6,54,52,68,102,48,201,55,60,31,4,50,8,4,33,123,87,66,2,4,82,102,44,6,32,26,4,14,25")
lista7 = [5,4,8,9,6,54,52,68,102,48,201,55,60,31,4,50,8,4,33,123,87,66,2,4,82,102,44,6,32,26,4,14,25]

print("\nA) Verifique se há o número 23 na lista")
print("O número 23 aparece", lista7.count(23), "vezes na lista")

print("\nB) Quantas vezes o número 4 aparece?")
print("O número 4 aparece", lista7.count(4), "vezes na lista")

print("\nC) Coloque a lista em ordem crescente")
lista7.sort()
print(lista7)

print("\nD) Coloque a lista em ordem decrescente")
lista7.sort(reverse=True)
print(lista7)

print("\nE) Verique a quantidade total de números")
print("A lista tem", len(lista7), "números")

print("\nF) Verifique a soma dos números")
print("O total da soma da lista é", sum(lista7))

print("\nG) Mostre o valor máximo e o valor mínimo")
print("O maior valor da lista é", max(lista7), "e o valor minimo é", min(lista7))

print("\nH) Sorteie uma número aleatório da lista e imprima com print")
print("Número sorteado: ", random.choice(lista7))