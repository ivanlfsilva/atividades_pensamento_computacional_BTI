temp = 0
gastos_do_dia = -1
tot = 0
print("Informe os gastos do dia:")
while gastos_do_dia != 0:
    gastos_do_dia = float(input())
    if gastos_do_dia > tot:
        tot = gastos_do_dia


text = "O seu maior gasto do dia foi R$ {:.2f}"
print(text.format(tot))
