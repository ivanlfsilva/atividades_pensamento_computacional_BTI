num = int(input("Digite um número: "))
fatorial = 1
if num <= 0:
    print("O numero deve ser maior que 0.")
else:
        for c in range(1, num + 1):
            fatorial *= c

        print("Resultado do fatorial: ", fatorial)