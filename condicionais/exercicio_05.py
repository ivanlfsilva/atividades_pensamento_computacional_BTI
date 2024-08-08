num_01 = float(input("Medida viga 1 "))
num_02 = float(input("Medida viga 2 "))
num_03 = float(input("Medida viga 3 "))

if num_01 < num_03:
    num_01, num_03 = num_03, num_01
if num_01 < num_02:
    num_01, num_02 = num_02, num_01
if num_02 < num_03:
    num_02, num_03 = num_03, num_02

a = num_01
b = num_02
c = num_03

if a <= 0 or b <= 0 or c <= 0:
    print("Digite um valor maior que 0")
else:

    if a >= (b + c):
        print("NAO FORMA TRIANGULO")
    else:
        if a ** 2 == ((b ** 2) + (c ** 2)):
            print("TRIANGULO RETANGULO")
        if (a ** 2) > ((b ** 2) + (c ** 2)):
            print("TRIANGULO OBTUSANGULO")
        if a ** 2 < ((b ** 2) + (c ** 2)):
            print("TRIANGULO ACUTANGULO")
        if a == b == c:
            print("TRIANGULO EQUILATERO")
        elif  a == b or a == c or b == c:
            print("TRIANGULO ISOSCELES")

