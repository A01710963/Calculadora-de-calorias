# En este programa realizaremos una calculadora de calorias por dia
# Claudio Gabriel Lopez Briceño
def operacion (p, s, e, a):
    """Lo que estoy haciendo aqui es la operacion necesaria para calcular las calorias diaras.
    La variable p se refiere a el peso, la variabel s al sexo, la variable e a la edad y la variable a a la actividad de la persona"""
    cal = a*(p*(s*e))
    return cal
def menus ():
    """Este menu le permitira al usuario elegir su sexo """
    print ("1. Masculino")
    print ("2. Femenino")

def menua ():
    """Este menu le permitira al usuario elegir su nivel de actividad"""
    print ("1. No muy activo")
    print ("2. Poco activo")
    print ("3. Activo")
    print ("4. Muy activo")
    
def menu ():
     """Este menu es el menu general, le permitira al usuario elegir cuando salir del programa"""
    print ("1. Calcular mi gasto calorico")
    print ("2. Salir")

def main ():
    while(True):
         """Aqui el usuario seleccionara su sexo"""
            print ("Selecciona una opcion")
            menu()
            opcion = (input())
            if opcion == '1':
                print ("¿Cual es tu sexo?")
                menus()
                opcions = (input())
                while (True):
                    if opcions == '1':
                        s = 1
                        break
                    elif opcions == '2':
                        s = 0.9
                        break
                    else:
                        print ("Respuesta invalida, asegurate de haber insertado el numero correcto")
                        menus()
                        opcions = (input())
                 """Aqui el usuario seleccionara su nivel de actividad diaria"""
                print ("¿Cual es tu nivel de actividad diaria?")
                menua()
                opciona = (input())
                while (True):
                    if opciona == '1':
                        a = 1.2
                        break
                    elif opciona == '2':
                        a = 1.375
                        break
                    elif opciona == '3':
                        a = 1.55
                        break
                    elif opciona == '4':
                        a = 1.725
                        break
                    else:
                        print ("Respuesta invalida, asegurate de haber insertado el numero correcto")
                        menua()
                        opciona = (input())
                """En estos dos apartados ingresara su peso y su edad"""
                p = float(input("Ingresa tu peso en kilogramos: "))
                
                e = int(input("Ingresa tu edad en años: "))
                """Imprimimos la respuesta"""
                print ("Tu consumo diario de calorias es de: ", operacion(p,s,e,a))
                
            elif opcion == '2':
                print ("Adios")
                break
            else:
                print ("Respuesta invalida, asegurate de haber insertado el numero correcto")
main()
