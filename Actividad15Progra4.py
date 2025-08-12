from datetime import datetime
import time
def cargando(segundos=2):
    print("Por Favor espere...Cargando")
    time.sleep(segundos)
    print("Exitoso...")
while True:
    print("********Menu*********")
    print(":::::::::::::::::::::")
    print("1. Ingreso de datos")
    print("2. Mostrar datos")
    print("3. Actulizar Edad")
    print("4. Eliminar datos")
    print("5. Salir")
    print("::::::::::::::::::::")

    try:
        opcion=int(input("Binvenido a Nuestro sistema en linea Porfavor Ingrese una opcion: "))
        cargando(2)
    except ValueError:
        print("Error, Ingrese un entero")
    match opcion:
        case 1:
            print("***Ingreso de datos***")
            while True:
                nombre = input("Ingrese su nombre y apellido (ejem: Juan Perez): ").strip()
                if nombre == "":
                    print("El nombre no puede estar vacío.")
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
                    if edad <= 0 or edad > 100:
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
            cargando(2)
        case 2:
            print("***Mostara Datos***")
            print(f"Nombre completo: {datos[0]}")
            print(f"Edad: {datos[1]}")
            print(f"Fecha de nacimiento: {datos[2]}")
        case 3:
            print("***Actualizar la edad***")
            while True:
                edadIngresada = input("Ingrese su nueva edad: ")
                if not edadIngresada.isdigit():
                    print("La edad debe ser un número entero positivo.")
                else:
                    edad = int(edadIngresada)
                    if edad <= 0 or edad > 120:
                        print("La edad debe estar entre 1 y 100.")
                    else:
                        datos[1] = edad
                        print("Exitoso...Se actualizo su edad")
                        break
        case 4:
            print("***Eliminar***")
            while True:
                confirmar = input("Está seguro que desea eliminar los datos (s/n): ").lower()
                if confirmar in ('s','n'):
                    break
                else:
                    print("Por favor ingrese 's' para sí o 'n' para no.")
            if confirmar == 's':
                datos.clear()
                print("Datos eliminados.")
            else:
                print("No re Eliminaron los datis.")
        case 5:
            print("Saliendo...")
            break
        case _:
            print("Error, opcion invalida")