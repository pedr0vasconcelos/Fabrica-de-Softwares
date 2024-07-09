def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Mova o disco 1 da {source} para {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Mova o disco {n} da {source} para {target}")
    hanoi(n-1, auxiliary, target, source)

def main():
    try:
        n = int(input("Digite a quantidade de discos: "))
        if n <= 0:
            print("Por favor, insira um número inteiro positivo.")
            return
        print("Solução para a Torre de Hanói com", n, "discos:")
        hanoi(n, 'Haste 1', 'Haste 3', 'Haste 2')
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()