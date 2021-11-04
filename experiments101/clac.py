print("                               ")
print("   🅱🅰🆂🅸🅲 🅲🅰🅻🅲🆄🅻🅰🆃🅾🆁   ")
while True:
    print("--------------------------")
    print("[1]: Add")        
    print("[2]: Subtract")           
    print("[3]: MUltiply")
    print("[4]: Divide")
    print("--------------------------")


    user = input("Choose ur opration 1/2/3/4 or press G to quit: ").lower()
    if user == 'g':
        break
    elif user == '1': 
        no1=int(input("Enter ur 1st no: "))
        no2=int(input("Enter ur 2st no: "))
        print("==>R̲e̲s̲u̲l̲t̲ = ", no1+no2)

    elif user == '2':
        no3=int(input("Enter ur 1st no:"))
        no4=int(input("Enter ur 2st no:"))
        print("==>R̲e̲s̲u̲l̲t̲ = ", no3-no4)

    elif user == '3':
        no5=int(input("Enter ur 1st no:"))
        no6=int(input("Enter ur 2st no:"))
        print("==>R̲e̲s̲u̲l̲t̲ = ", no5*no6)

    elif user == '4':
        no7=int(input("Enter ur 1st no:"))
        no8=int(input("Enter ur 2st no:"))
        print("==>R̲e̲s̲u̲l̲t̲ = ", no7/no8)
        

        