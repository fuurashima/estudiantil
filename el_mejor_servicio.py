def Diccionario(dicc_empleado,rut,nombre,apellido,depto,sbase):
    dicc_empleado[rut]= rut, nombre, apellido, depto, sbase
    return dicc_empleado
def Diccionario2(dicc_empleado,rut,nombre,apellido,depto,sbase):
    dicc_empleado[depto] = rut, nombre, apellido, depto, sbase
    return dicc_empleado
#Hola

print("\n\n\t El Mejor Servicio")
#Listas
dicc_empleado = {}
lista2 =[]

opc=0
while opc!=6:
    print("\n\n 1.- Ingreso de Cliente Manualmente: ")
    print("\n\n 2.- Consulta Departamentos: ")
    print("\n\n 3.- Llenar lista de Empleados automáticamente: ")
    print("\n\n 4.- Actualizar sueldo base sobre Rut: ")
    print("\n\n 5.- Llenar una lista y averiguar el promedio,mayor y menor ")
    print("\n\n 6.- Salir")
    opc=int(input("Ingrese Opcion: "))

    if opc == 1:
        rut = input("\n\t Ingrese RUT: ")
        nombre = input("\n\t Ingrese Nombre: ")
        apellido = input("\n\t Ingrese Apellido: ")
        depto = input("\n\t Ingrese Depto: ")
        sbase = input("\n\t Ingrese Sueldo Base: ")
        dicc_empleado = Diccionario(dicc_empleado, rut, nombre, apellido, depto, sbase)
        dicc_empleado = Diccionario2(dicc_empleado, rut, nombre, apellido, depto, sbase)



    elif opc == 2:
        clave = dicc_empleado.keys()
        listadepto = list(dicc_empleado.values())
        print("\n\n Los departamentos son: ", clave)


    elif opc == 3:

        dicc_empleado[169106614]=(169106614, "Ivan","Cano","Informática", 280000)
        dicc_empleado[199349775] = (199349775, "Pamela","Fritis", "Tecnóloga", 780000)
        dicc_empleado[85486845] = (8548684-5, "Hector", "Villarroel","Informático", 56333)
        dicc_empleado[94861616] = (9486161-6, "Dayana", "Gonzalez","Tecnologa", 10090090)
        dicc_empleado[94869528] = (94869528, "Fernando", "Silva","Profesor", 5420000)
        print("\n\n\t Datos ingresados..... ")

    elif opc == 4:
        #for i in range(0, len(dicc_empleado), 1):
        #clave = dicc_empleado.keys()
        #listadepto = list(dicc_empleado.values())
        #print("\n\n ",listadepto)
        #for nombre,apellido,depto,sbase in listadepto:
            #print(" ", nombre, apellido, depto, sbase)

        new_sbase = 0
        y = 0
        print (dicc_empleado)
        while y == 0:
            rut = input("Ingresa el rut para modificar: ")
            existe = (rut in dicc_empleado)
            while existe == True:
                valor = dicc_empleado.get(rut)
                print (" ", valor)
                new_sbase = int(input("\n\n Ingrese nuevo sueldo: "))
                dicc_empleado[rut] = (valor[0], valor[1], valor[2], valor[3],valor[4], new_sbase)
                print ("\n\n Nueva lista de empleados actualizada: ")
                print (dicc_empleado)
                y = 1
                print("\n\n Sueldo Actualizado")
        

    elif opc == 5:
        print("\n\n Bienvenidos al ejercicio 2")
        prom =0.0
        num = 0.0
        x = 0
        x = int(input("\n\n Ingrese cantidad de números que va a ingresar: "))
        for i in range (x):
            num = float(input("\n\n Ingrese los números a ingresar: "))
            lista2.append (num)
            prom = prom + num
        print ("Lista: ",lista2)
        print ("El Promedio es: ", prom/len(lista2))
        min(lista2)
        print ("El valor minimo es: ", min(lista2))
        max(lista2)
        print ("El Valor Mayor es: ", max(lista2))






