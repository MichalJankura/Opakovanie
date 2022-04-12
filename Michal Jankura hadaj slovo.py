import random

def hadaj():
    pokus = 0
    sz = list(slovo)
    slovo2 = (slovo[0] + "." * (len(slovo) - 2) + slovo[-1])
    sz2 = list(slovo2)
    print(slovo2)
    final = (len(slovo)-2)
    while final > 0:
        pismeno = input("zadaj písmeno: ")
        for p in sz:
            if p == pismeno:
                    final -=1
                    ind = sz.index(p)
                    sz2.pop(ind)
                    sz2.insert(ind,pismeno)
                    text = "".join(str(x) for x in sz2)
                    print(text)

file =open("slova.txt","r",encoding="UTF-8")
slova = file.readlines()
slovo = random.choice(slova)

hadaj()