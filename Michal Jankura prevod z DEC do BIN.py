cislo = int(input("Zadjte číslo v 10ej sústave : "))
pocet = int(input("Zadajte počet bajtov : "))
bin = ""

while cislo > 0:
    bin += str(cislo%2)
    cislo = cislo//2
nula = (8*pocet)-len(bin)
bin1 = bin + nula*str(0)
kod = ""
for i in range(pocet):
    if i < len(bin)//8 + 1:
        kod +=  bin1[i:(i+8)]+" "
    else:
        kod = 8*str(0) + " "
binar = kod[::-1]
print(binar)