lista_nomes = []
numero_nomes = int(input("Quantos nomes? "))

for i in range(numero_nomes):
    lista_nomes.append(str(input()))

lista_nomes.reverse()
for nome in lista_nomes:
    print(nome)
