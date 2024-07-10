import random, csv, statistics



def AsignarSueldosAleatorios(trabajadores):
    
    sueldos_trabajadores = {}
    
    for trabajador in trabajadores:
        sueldo = random.randint(300000, 2500000) #Generar Sueldos en un limite de $300.000 a $2.500.000 
        sueldos_trabajadores[trabajador] = sueldo #asigna los sueldos a los distintos trabajadores
    print("Sueldos Generados correctamente")
    print(sueldos_trabajadores)
    return sueldos_trabajadores    

def ClasificarSueldos(sueldo_trabajadores):    
    menor800k = {} # filtro
    de800k_2millones = {} # filtro
    arribade_2millones = {} #filtro
    
    for trabajador,sueldo in sueldo_trabajadores.items(): # Filtro de sueldos para poder asignarlos
        if sueldo < 800000 : 
            menor800k[trabajador] = sueldo
        elif sueldo <= 2000000 :
            de800k_2millones[trabajador] = sueldo
        else:
            arribade_2millones[trabajador] = sueldo
    
    print("")                                           #Linea 29 a 52 se encarga en printear los sueldos con sus respectivos filtros
    print("Sueldos menores a $800.000")
    print("TOTAL : ",len(menor800k))
    print("Nombre empleado" ,"Sueldo")
    for trabajador,sueldo in menor800k.items():
        print(trabajador,sueldo)
    print("")
    
    print("")
    print("Sueldos entre $800.000 a $2.000.000")
    print("TOTAL : ",len(de800k_2millones))
    print("Nombre empleado","Sueldo")
    for trabajador,sueldo in de800k_2millones.items():
        print(trabajador,sueldo)
    print("")
    
    print("")
    
    print("Sueldos mayores a $2.000.000")
    print("TOTAL : ",len(arribade_2millones))
    print("Nombre empleado", "Sueldo")
    for trabajador,sueldo in arribade_2millones.items():
        print(trabajador,sueldo)
    print("")
    
def CalcularEstadisticas(sueldo_trabajadores):  
    
    sueldo = list(sueldo_trabajadores.values()) #Sacamos los valores del sueldo (1,2,345,4646,....)

    if not sueldo_trabajadores:
        return None,None,None
    
    max_sueldo = max(sueldo)            #Sacamos las estadisticas
    minsueldo_ = min(sueldo)
    promedio = (sum(sueldo) / len(sueldo))
    MediaGeoemtrica = statistics.geometric_mean(sueldo) 
    
    return max_sueldo,minsueldo_,promedio,MediaGeoemtrica

def ReporteDeSueldos(sueldo_trabajadores):
    informacion_trabajadores = [] #Creo una lista para posteriormente usarlo para crear el archivo.csv
    
    for trabajador, sueldo in sueldo_trabajadores.items():
        DescAFP = (sueldo * 7) / 100  #Descuentos
        DescSalud = (sueldo * 12) / 100 #Descuentos
        SueldoLiquido = sueldo - DescAFP - DescSalud #Descuentos
        
        informacion_trabajadores.append([trabajador,sueldo,DescAFP,DescSalud,SueldoLiquido]) #Añadimos la informacion a la lista
    
    with open ("Reporte_sueldos.csv","w",newline="") as file: #Generamos el archivo con el nombre y formato csv, en modo writer y evitamos evitamos altados de linea con el newline
        escritor = csv.writer(file,delimiter=",") # informacion del escritor, importante el delimeter debido a que separara la info con , 
        escritor.writerow(['Nombre Empleado','Sueldo Base','Descuento AFP','Descuento Salud','Sueldo Liquido']) # Genera los apartados de la informacion
        
        for informacion in informacion_trabajadores: # Con este bucle, ponemos la informacion al csv
            escritor.writerow(informacion)
    
    print("Reporte Generado correctamente.")