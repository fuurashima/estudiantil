def insertar_empleado(diccionario_empleado,rut,nombre,apellido,depto,sbase):
    diccionario_empleado[rut] = (nombre,apellido,depto,sbase)
    return diccionario_empleado
def insertar_empleado_dpto(diccionario_depto,rut,nombre,apellido,depto,sbase):
    if depto not in diccionario_depto:
        diccionario_depto[depto] = {}
    diccionario_depto[depto][rut] = (nombre,apellido,depto,sbase)
    return diccionario_depto
def actualizar_empleado_sbase(diccionario_empleado, diccionario_depto, rut, new_sbase):
    datos_empleado = diccionario_empleado[rut]
    diccionario_empleado[rut] = (datos_empleado[0], datos_empleado[1], datos_empleado[2], new_sbase)
    diccionario_depto[datos_empleado[2]][rut] = (datos_empleado[0], datos_empleado[1], datos_empleado[2], new_sbase)


print("\n\n\t El Mejor Servicio")
#Listas
diccionario_empleado = {}
diccionario_depatamentos = {}
lista2 = []

opc = 0
while opc != 6:
    print("\n\n 1.- Ingreso de Cliente Manualmente: ")
    print("\n\n 2.- Consulta Departamentos: ")
    print("\n\n 3.- Llenar lista de Empleados automáticamente: ")
    print("\n\n 4.- Actualizar sueldo base sobre Rut: ")
    print("\n\n 5.- Llenar una lista y averiguar el promedio,mayor y menor ")
    print("\n\n 6.- Salir")
    opc = int(input("Ingrese Opcion: "))

    if opc == 1:
        rut = input("\n\t Ingrese RUT: ")
        nombre = input("\n\t Ingrese Nombre: ")
        apellido = input("\n\t Ingrese Apellido: ")
        depto = input("\n\t Ingrese Depto: ")
        sbase = input("\n\t Ingrese Sueldo Base: ")
        diccionario_empleado = insertar_empleado(diccionario_empleado, rut, nombre, apellido, depto, sbase)
        diccionario_depatamentos = insertar_empleado_dpto(diccionario_depatamentos,rut,nombre,apellido,depto,sbase)

    elif opc == 2:
        clave = diccionario_empleado.keys()
        listadepto = list(diccionario_empleado.values())
        print("\n\n Los departamentos son: ", clave, listadepto)

    elif opc == 3:

        insertar_empleado(diccionario_empleado, "16910661-4", "Ivan", "Cano","Informática", 280000)
        insertar_empleado(diccionario_empleado, "19934977-5", "Pamela", "Fritis","Tecnóloga", 780000)
        insertar_empleado(diccionario_empleado, "8548684-5", "Hector", "Villarroel","Informática", 56333)
        insertar_empleado(diccionario_empleado, "9486161-6", "Dayana", "Gonzalez","Tecnóloga", 10090090)
        insertar_empleado(diccionario_empleado, "9486952-8", "Fernando", "Silva","Profesor", 5420000)
        insertar_empleado_dpto(diccionario_depatamentos, "16910661-4", "Ivan", "Cano","Informática", 280000)
        insertar_empleado_dpto(diccionario_depatamentos, "19934977-5", "Pamela", "Fritis", "Tecnóloga", 780000)
        insertar_empleado_dpto(diccionario_depatamentos, "8548684-5", "Hector", "Villarroel","Informática", 56333)
        insertar_empleado_dpto(diccionario_depatamentos, "9486161-6", "Dayana", "Gonzalez","Tecnóloga", 10090090)
        insertar_empleado_dpto(diccionario_depatamentos, "9486952-8", "Fernando", "Silva","Profesor", 5420000)
        print("\n\n\t Datos ingresados..... ")

    elif opc == 4:

        new_sbase = 0
        y = 0
        while y == 0:
            rut = input("Ingresa el rut para modificar: ")
            #import pdb; pdb.set_trace()
            existe = (rut in diccionario_empleado)
            while existe == True:
                valor = diccionario_empleado[rut]
                print(" ", valor)
                new_sbase = int(input("\n\n Ingrese nuevo sueldo: "))
                actualizar_empleado_sbase(diccionario_empleado, diccionario_depatamentos, rut, new_sbase)
                y = 1
                print("\n\n Sueldo Actualizado")
                sum_sbase = 0
                for key, value in diccionario_empleado.items():
                    print(key, value)
                    sum_sbase += value[3]
                print("Sueldo Base: " + str(sum_sbase))

                existe = False

    elif opc == 5:
        print("\n\n Bienvenidos al ejercicio 2")
        prom = 0.0
        num = 0.0
        x = 0
        x = int(input("\n\n Ingrese cantidad de números que va a ingresar: "))
        for i in range(x):
            num = float(input("\n\n Ingrese los números"))
            lista2.append(num)
            prom = prom + num
        print("Lista: ", lista2)
        print("El Promedio es: ", prom / len(lista2))
        min(lista2)
        print("El valor minimo es: ", min(lista2))
        max(lista2)
        print("El Valor Mayor es: ", max(lista2))
