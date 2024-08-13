num_testes = int(input("Quantidade de casos de teste: "))
i = 0
resposta = ""
for i in range(i, num_testes):
    caso_de_testes = input("Caso de teste: ")
    separador = caso_de_testes.split()
    x = int(separador[0])
    y = int(separador[1])
    contador = 0
    soma = 0
    while contador < y:
        if x % 2 != 0:
            soma += x
            contador += 1
        x += 1
    resposta += "Soma dos Y numeros ímpares a partir de X: " + str(soma) + "\n"


print(resposta)
