print("\nA)", (30*5)+18-(15/3))
print("B)", (185/3)+(3**5)-100)
print("C)", (125/5)+12**2-(169/13)*10)

print("\n::Desafio 1::")
print("Faça o usuário inserir 2 números e apresente a soma,subtração,multiplicação e divisão dos números dados\n")
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

soma = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2

print("Soma: ", soma)
print("Subtracao: ", sub)
print("Multiplicao: ", mult)
print("Divisao: ", div)

print("\n::Desafio 2::")
print("Faça o usuário inserir um número. Mostre o antecessor e o sucessor desse número.\n")
n = int(input("Digite o numero a ser verificado: "))
print("O numero antecessor é: ", n-1)
print("O numero sucessor é: ", n+1)