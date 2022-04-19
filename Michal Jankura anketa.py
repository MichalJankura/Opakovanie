import tkinter
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()

with open("anketa.txt","r",encoding="UTF-8") as file:
    subor = file.readlines()

ano = 0
nie = 0
mozno = 0
volba = int(input(f"Zadaj 1 pre ANO  \nZadaj 2 pre NIE  \nZadaj 3 pre MOZNO\nTvoja volba == "))

if volba == 1:
    ano += 1
elif volba == 2:
    nie += 1
else:
    mozno += 1

for hlas in subor[1:]:
    za_ano, za_nie, za_mozno = subor[1].split()
    hlas_za_ano = int(za_ano)
    hlas_za_nie = int(za_nie)
    hlas_za_mozno = int(za_mozno)
    ano += hlas_za_ano
    nie += hlas_za_nie
    mozno += hlas_za_mozno

moznosti = {ano:"ANO",nie:"NIE",mozno:"MOZNO"}
najviac_hlasov = max(ano,nie,mozno)
print(f"Najviac hlasov za možnosť {moznosti.get(max(moznosti))} je {najviac_hlasov}")

canvas.create_text(200,25,text=subor[0],font="Arial 13")
canvas.create_text(70,70,text=(f"1.) ANO {ano}\n2.) NIE {nie}\n3.) MOZNO {mozno}"),font="Arial 15")

# farba = ""
# if ano or nie or mozno is True in max(ano,nie,mozno):
#     farba = "green"
# elif ano or nie or mozno is not True in max(ano,nie,mozno):
#     farba = "red"
canvas.create_line(140,70,140+nie*10,70,fill = farba,width= 20,tags="ano")
canvas.create_line(140,50,140+ano*10,50,fill = farba,width= 20,tags="nie")
canvas.create_line(140,90,140+mozno*10,90,fill = farba,width= 20,tags="mozno")

canvas.mainloop()

with open("anketa.txt","w",encoding="UTF-8") as file:
    file.write(subor[0]+str(ano)+" "+str(nie)+" "+str(mozno))
    file.close()