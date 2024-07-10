import funciones as fn 

trabajadores = ["Juan Pérez", "María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

sueldo_trabajadores = {}

sueldo_trabajadores = {trabajador : 0 for trabajador in trabajadores}
print("(Los sueldos empiezan con valor : 0)")

while True:
    print("")
    print("=== S U E L D O S ===")
    print("[1] Asignar Sueldos Aleatorios.")
    print("[2] Clasificar Sueldos.")
    print("[3] Ver estadisticas. ")
    print("[4] Reporte de sueldos.")
    print("[5] Salir del programa. ")
    print("")
    try:
        opcion = int(input("Ingrese opcion a entrar: "))
            
        if opcion == 1 : 
            print("Generando sueldos...")
            sueldo_trabajadores = fn.AsignarSueldosAleatorios(trabajadores)
        elif opcion == 2 : 
            if sueldo_trabajadores:
                fn.ClasificarSueldos(sueldo_trabajadores)
        elif opcion == 3: 
            if sueldo_trabajadores:
                MediaGeoemtrica,max_sueldo, minsueldo_, promedio = fn.CalcularEstadisticas(sueldo_trabajadores)
                print("Sueldo Maximo:",max_sueldo)
                print("Sueldo Minimo:",minsueldo_)
                print("Promedio de sueldos: ",promedio)
                print("La media Geometrica es : ",MediaGeoemtrica)
        elif opcion == 4 : 
            if sueldo_trabajadores:
                fn.ReporteDeSueldos(sueldo_trabajadores)
        elif opcion == 5 :
            print("Finalizando Programa...")
            print("Desarrollado por : Eduardo Figueroa")
            print("Rut 21.898.312-k")
            break
        else:
            print("Opcion no valida, Re intente nuevamente")
    except ValueError:
        print("Interaccion no valida")