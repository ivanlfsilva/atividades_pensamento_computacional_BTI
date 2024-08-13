num_testes = int(input("Quantidade de casos de teste: "))
i = 0
resposta = ""
for i in range(i, num_testes):
    PA = int(input("População A: "))
    PB = int(input("População B: "))
    G1 = float(input("Crescimento A: "))
    G2 = float(input("Crescimento B: "))
    i += 4

    anos = 0
    while PA <= PB:
        PA += PA * (G1 / 100)
        PB += PB * (G2 / 100)
        anos += 1

        if anos > 100:
            print("Time Limit Exceeded")
            break
    resposta += "Total de anos: " + str(anos) + " anos\n"


print(resposta)
