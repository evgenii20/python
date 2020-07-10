from sys import argv

par1, par2, par3 = argv[1:]

print("Количество отработанных часов: ", par1)
print("Сумма оплаты труда за час: ", par2)
print("Размер премии: ", par3)
pay = float(par1) * float(par2) + float(par3)
print("Размер заработной платы составил: ", pay)
