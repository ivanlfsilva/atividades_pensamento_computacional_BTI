num = int(input("Qual o N? "))
print("Digite os valores:")
lista = []
op = ["0", "1"]
resultado = 0
i = 1
for i in range(num):
    lista.append(int(input()))

op = int(input("Qual a op? "))
while op != 0 or op != 1:

    if op == 0 or op == 1:
        op = op
        break
    else:
        print("Opção invalida! digite 0 ou 1")
        op = int(input("Qual a op? "))

a = int(input("Qual o A "))
b = int(input("Qual o B "))
a=a-1
b=b-1
if op == 0:
    print(lista[a] , " + " , lista[b] , " = " , (lista[a] + lista[b]))
if op == 1:
    print(lista[a] , " * " , lista[b] , " = " , (lista[a] * lista[b]))