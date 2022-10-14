# En este programa realizaremos una calculadora de calorias por dia
# Claudio Gabriel Lopez Briceño
def operacion (peso, sexo, edad, actividad):
    """Lo que estoy haciendo aqui es la operacion necesaria para calcular las calorias diaras.
    La variable p se refiere a el peso, la variabel s al sexo, la variable e a la edad y la variable a a la actividad de la persona"""
    calorias = actividad*(peso*(sexo*edad))
    return calorias
def menuSexo ():
    #Este menu le permitira al usuario elegir su sexo 
    print ("1. Masculino")
    print ("2. Femenino")

def menuActividad ():
    #Este menu le permitira al usuario elegir su nivel de actividad
    print ("1. No muy activo")
    print ("2. Poco activo")
    print ("3. Activo")
    print ("4. Muy activo")
    
def menuPrincipal ():
    #Este menu es el menu general, le permitira al usuario elegir cuando salir del programa
    print ("1. Calcular mi gasto calorico")
    print ("2. Recomendaciones de comida")
    print ("3. Salir")

#Lista de recomendaciones de comida
listaRecomendaciones = [
    ["Proteinas:", "Carbohidratos:", "Grasas:", "Snacks:"],
    ["Pollo", "Papa", "Nueces", "Fruta"],
    ["Carnes rojas", "Pasta", "Aguacate", "Verdura"],
    ["Huevo", "Arroz", "Aceite de oliva", "Palomitas de maiz"],
    ["Salmon", "Pan integral", "Aceite de nabina", "Frutos secos"]
    ]
#Esta funcion imprime una columna de la matriz dependiendo de la eleccion del usuario
def imprimirRecomendaciones (listaRecomendaciones):
    i = input("¿De que deseas obtener recomendaciones? Proteinas(0) Carbohidratos(1) Grasas(2) Snacks(3): ")
    columna = [fila[int(i)] for fila in listaRecomendaciones]
    print (columna, end = "\n")
    
def pruebas():
    operacion(18,17,16,5)
    menuSexo()
    menuActividad()
    menuPrincipal()
    imprimirRecomendaciones(listaRecomendaciones)

def main ():
    #pruebas()
    while(True):
            #Aqui el usuario seleccionara su sexo
            print ("Selecciona una opcion")
            menuPrincipal()
            opcion = (input())
            if opcion == '1':
                print ("¿Cual es tu sexo?")
                menuSexo()
                opcionSexo = (input())
                while (True):
                    #Dependiendo del sexo se cambia el numero, ya que asi lo pide la formula para calcular el gasto energetico
                    if opcionSexo == '1':
                        sexo = 1
                        break
                    elif opcions == '2':
                        sexo = 0.9
                        break
                    else:
                        print ("Respuesta invalida, asegurate de haber insertado el numero correcto")
                        menuSexo()
                        opcions = (input())
                #Aqui el usuario seleccionara su nivel de actividad diaria
                print ("¿Cual es tu nivel de actividad diaria?")
                menuActividad()
                opcionActividad = (input())
                while (True):
                    #Dependiendo del nivel de actividad se asigna un numero, ya que asi lo pide la formula para calcular el gasto energetico
                    if opcionActividad == '1':
                        actividad = 1.2
                        break
                    elif opcionActividad == '2':
                        actividad = 1.375
                        break
                    elif opcionActividad == '3':
                        actividad = 1.55
                        break
                    elif opcionActividad == '4':
                        actividad = 1.725
                        break
                    else:
                        print ("Respuesta invalida, asegurate de haber insertado el numero correcto")
                        menuActividad()
                        opciona = (input())
                #En estos dos apartados ingresara su peso y su edad
                peso = float(input("Ingresa tu peso en kilogramos: "))
                
                edad = int(input("Ingresa tu edad en años: "))
                #Imprimimos la respuesta
                print ("Tu consumo diario de calorias es de: ", operacion(peso,sexo,edad,actividad))
            
            #En esta opcion imprimimos una columna de la matriz "listaRecomendaciones" dependiendo de la eleccion del usuario
            elif opcion == '2':
                #Llamamos la funcion
                imprimirRecomendaciones(listaRecomendaciones)
            
            #Esta opcion sirve para salir del programa
            elif opcion == '3':
                #Imprimos adios y terminamos el ciclo while
                print ("Adios")
                break
            else:
                print ("Respuesta invalida, asegurate de haber insertado el numero correcto")
main()
