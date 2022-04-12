abeceda = 'qwertzuiopasdfghjklyxcvbnm'
file = open("tabulka_pocetnosti.txt","r",encoding="UTF-8")
text = file.read()
none = []
for pismeno in abeceda:
    pocet = 0
    for znak in text:
        if pismeno == znak.lower():
            pocet += 1
    file.close()
    print(f"{pismeno}:{pocet}")
