def binary(chislo):
    n=" "
    while chislo > 0: 
        n = str(chislo % 2) + n
        chislo = chislo // 2
    return (n)

def octal(chislo):
    n=" "
    while chislo > 0:
        n = str(chislo % 8) + n
        chislo = chislo // 8
    return (n)

chislo=int(input("Введите любое положительное число:"))
schislenie=int(input("Введите целевую систему счисления (2 или 8):"))

if schislenie == 2:
    print(binary(chislo))
elif schislenie== 8:
    print(octal(chislo))