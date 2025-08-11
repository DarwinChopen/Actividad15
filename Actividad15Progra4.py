from datetime import datetime
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
            nombre = input("Ingrese su nombre y apellido (ejem: Juan Perez): ").strip()
            if nombre == "":
                print("El nombre no puede estar vacío, por favor Ingrese un Numero entero.")
            elif len(nombre.split()) < 2:
                print("Debe ingresar al menos un nombre y un apellido.")
            else:
                break
            while True:
                edadIngresada = input("Ingrese su edad: ")
                if not edadIngresada.isdigit():
                    print("La edad debe ser un número entero Positivo.")
                else:
                    edad = int(edadIngresada)
                    if edad <= 0 or edad > 120:
                        print("La edad debe estar entre 1 y 100.")
                    else:
                        break
            while True:
                fechanac = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ").strip()
                try:
                    convertirFecha = datetime.strptime(fechanac, "%d/%m/%Y")
                    hoy = datetime.now()
                    if convertirFecha> hoy:
                        print("La fecha no puede ser en el futuro")
                    elif convertirFecha.year < 1925:
                        print("El año debe ser mayor o igual a 1925")
                    else:
                        break
                except ValueError:
                    print("Dato Invalido por favor Use el formato dd/mm/aaaa.")
            datos = [nombre, edad, fechanac]
            print("Exitoso...Datos ingresados correctamente:")
        case 2:
            print("Mostara Datos")
            print(f"Nombre completo: {datos[0]}")
            print(f"Edad: {datos[1]}")
            print(f"Fecha de nacimiento: {datos[2]}")
        case 3:
            print("")
        case 4:
            print("")
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Error, opcion invalida")