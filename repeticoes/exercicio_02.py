temp = 0
gastos_do_dia = -1
tot = 0
print("Informe os gastos do dia:")
while gastos_do_dia != 0:
    gastos_do_dia = float(input())
    if gastos_do_dia > tot:
        tot = gastos_do_dia


print("O seu maior gasto hoje foi R$ ", round(tot, 2))
