while True:
    print("1. ")
    print("2. ")
    print("3. ")
    print("4.Salir ")
    try:
        opcion=int(input("Ingrese una opcion"))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            print("")
        case 2:
            print("")
        case 3:
            print("")
        case 4:
            print("")
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Error, opcion invalida")