n = int(input('n= '))
summa = 0
multiplication = 1
for i in range(1, (n + 1)):
    for k in range(1, (i*2+1)):
        multiplication *= (k+1)
    summa += multiplication
    multiplication = 1
    
print("Сумма дорівнює", summa)













