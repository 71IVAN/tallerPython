#Informacion de datos:
# nombreCliente = input("Por favor ingresa tu nombre : ")
# nPersonasAdultas = input("Por favor ingrese cuantas personas adultas van a viajar: ")
# numeroNiños = input("Por favor ingrese cuantos niños van a viajar: ")

inicio = 0
destinoUno = 1  #Guajira
destinoDos = 2  #Cañon del chicamocha
destinoTres = 3 #Llanos orientales




while True:
    print("Opciones:")
    print("1. Reservar para la Guajira")
    print("2. Reservar para Cañon del chicamocha")
    print("3. Reservar para los Llanos orientales")
    print("4. Finalizar la reserva o ingresar otro número diferente a los anteriores")
    
    opcion = int(input("Ingrese el número de su opción: "))
    
    if opcion == 1:
        
        nameU = input("Por favor ingresa tu nombre : ")
        nPerAduls = input("Por favor ingrese cuantas personas adultas van a viajar: ")
        nNiños = input("Por favor ingrese cuantas niños van a viajar: ")

        

        print("Has seleccionado reservar para la Guajira.")

    # elif opcion == 2:
    #     nameU = input("Por favor ingresa tu nombre : ")
    #     nPerAduls = input("Por favor ingrese cuantas personas adultas van a viajar: ")
    #     nNiños = input("Por favor ingrese cuantas niños van a viajar: ")
    #     print("Has seleccionado reservar para el Cañon del chicamocha.")

    # elif opcion == 3:
    #     nameU = input("Por favor ingresa tu nombre : ")
    #     nPerAduls = input("Por favor ingrese cuantas personas adultas van a viajar: ")
    #     nNiños = input("Por favor ingrese cuantas niños van a viajar: ")
    #     print("Has seleccionado reservar para Llanos grandes.")



        break  # Detener el bucle
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")

print("¡Reserva finalizada!")



 

