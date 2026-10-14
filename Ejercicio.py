
vehiculos = [["", "", "", 0, 0, 0] for i in range(30)]
cantidad = 0


def pedir_dia(mensaje):
    while True:
        try:
            dia = int(input(mensaje))
            if 1 <= dia <= 31:
                return dia
            print("El día debe estar entre 1 y 31.")
        except ValueError:
            print("Ingrese un número válido.")


while True:
    print("\n--- TALLER DE VEHÍCULOS ---")
    print("1. Registrar ingreso")
    print("2. Registrar salida (vehículo reparado)")
    print("3. Reporte de vehículos reparados")
    print("4. Reporte de todos los vehículos")
    print("5. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        if cantidad == 30:
            print("No se pueden registrar más de 30 vehículos.")
            continue

        placa = input("Placa: ").strip().upper().replace(" ", "").replace("-", "")
        if not placa:
            print("La placa no puede estar vacía.")
            continue

        repetida = False
        for i in range(cantidad):
            if vehiculos[i][0] == placa:
                repetida = True
                break

        if repetida:
            print("Esta placa ya está registrada.")
            continue

        propietario = input("Nombre del propietario: ").strip()
        celular = input("Número de celular: ").strip()
        if not propietario or not celular or not celular.isdigit():
            print("Ingrese un nombre y un celular numérico válidos.")
            continue

        ingreso = pedir_dia("Día de ingreso (1-31): ")
        vehiculos[cantidad] = [placa, propietario, celular, ingreso, 0, 0]
        cantidad += 1
        print("Vehículo registrado correctamente. Placa:", placa)

    elif opcion == "2":
        print("\n--- VEHÍCULOS PENDIENTES DE SALIDA ---")
        pendientes = 0
        for i in range(cantidad):
            if vehiculos[i][4] == 0:
                print("Placa:", vehiculos[i][0], "| Propietario:", vehiculos[i][1])
                pendientes += 1

        if pendientes == 0:
            print("No hay vehículos pendientes de salida.")
            continue

        placa = input("Placa del vehículo reparado: ").strip().upper().replace(" ", "").replace("-", "")
        posicion = -1
        for i in range(cantidad):
            if vehiculos[i][0] == placa:
                posicion = i
                break

        if posicion == -1:
            print("No se encontró esa placa. Revise la lista anterior.")
        elif vehiculos[posicion][4] != 0:
            print("Este vehículo ya tiene registrada su salida.")
        else:
            salida = pedir_dia("Día de salida (1-31): ")
            while salida < vehiculos[posicion][3]:
                print("La salida no puede ser anterior al ingreso.")
                salida = pedir_dia("Día de salida (1-31): ")

            vehiculos[posicion][4] = salida
            vehiculos[posicion][5] = salida - vehiculos[posicion][3]
            print("¡Reparación terminada y salida registrada!")
            print("Días en el taller:", vehiculos[posicion][5])

    elif opcion == "3":
        terminados = 0
        print("\n--- VEHÍCULOS REPARADOS ---")
        for i in range(cantidad):
            if vehiculos[i][4] != 0:
                print("Placa:", vehiculos[i][0], "| Días:", vehiculos[i][5])
                terminados += 1
        print("Total de vehículos reparados:", terminados)

    elif opcion == "4":
        print("\n--- TODOS LOS VEHÍCULOS ---")
        for i in range(cantidad):
            print("Placa:", vehiculos[i][0],
                  "| Propietario:", vehiculos[i][1],
                  "| Celular:", vehiculos[i][2])
        print("Total de vehículos ingresados:", cantidad)

    elif opcion == "5":
        print("Aplicación cerrada.")
        break

    else:
        print("Opción incorrecta. Intente nuevamente.")



            