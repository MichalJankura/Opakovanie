def zmen (text, znak):
    for znak in znaky:
        for i in range(len(text)):
            if znak == text[i]:
                text = text[:i] + "_" + text[i+1:]
    return text

file = open("vybrane_slova.txt","r",encoding="UTF-8")
diktat = file.read()
znaky = "yýiíYIÍÝ"

print(f"všetky písmená:{len(diktat)}")
print()

for pismeno in znaky:
    pocet = 0
    for znak in diktat.lower():
        if pismeno == znak:
            pocet += 1
    if pocet > 0:
        print(f"{pismeno}: {pocet}")
    else:
        print("", end = "")

print(zmen(diktat,znaky))


