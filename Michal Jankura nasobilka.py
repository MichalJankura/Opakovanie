try:
    od = int(input("Od :  "))
    do = int(input("Do :  "))
    for i in range(od,do+1):
        print(i,end=" - ")
        for j in range(od,do+1):
            print(i*j," ",end = "")
        print("")

except ValueError:
    print("Nečiselná hodnota")
