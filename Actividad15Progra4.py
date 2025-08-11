while True:
    print("1. Ingreso de datos")
    print("2. Mostrar datos")
    print("3. ")
    print("4.Salir ")
    try:
        opcion=int(input("Ingrese una opcion"))
    except ValueError:
        print("Ingrese un entero")
    match opcion:
        case 1:
            print("Ingreso de datos")
            nombre=input("Ingrese un nombre y u apellido(ejem, Juan Perez) ")
            edad=int(input("Ingrese su edad: "))
            fechanac=int("Ingrese su fecha de nacimineto... dd/mm/aaaa")



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