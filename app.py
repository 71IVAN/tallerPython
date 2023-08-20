#variables de precio
precioAdulGuajira = 1450000
precioAdulCañonChicamocha = 1600000 
precioAdulLlanosOrientales = 1200000

precioNiñoGuajira = 870000
precioNiñoCañonChicamocha = 960000
precioNiñoLlanosOrientales = 720000



while True:
    print("Bienvenido a XYZ :")
    print("1. Reservar para la Guajira")
    print("2. Reservar para Cañon del chicamocha")
    print("3. Reservar para los Llanos orientales")
    print("4. Finalizar la reserva o ingresar otro número diferente a los anteriores")
    
    opcion = int(input("Ingrese el número de sus proximas vacaciones: "))

    if opcion == 4:
        print("Cancelaste la operación.")
        break
    
    elif opcion == 1:
        
        nombreCliente = input("Por favor ingresa tu nombre completo : ")
        numeroAduls = int(input("Por favor ingrese cuantas personas adultas van a viajar: "))
        numeroNiños = int(input("Por favor ingrese cuantas niños van a viajar: "))

        print("Has seleccionado reservar para la Guajira.")

        subTotal = (numeroAduls * precioAdulGuajira) + (numeroNiños * precioNiñoGuajira) 

        break

    elif opcion == 2:
        nombreCliente = input("Por favor ingresa tu nombre completo : ")
        numeroAduls = int(input("Por favor ingrese cuantas personas adultas van a viajar: "))
        numeroNiños = int(input("Por favor ingrese cuantas niños van a viajar: "))

        print("Has seleccionado reservar para ir Cañonchicamocha.")

        
        subTotal = (numeroAduls * precioAdulCañonChicamocha) + (numeroNiños * precioNiñoCañonChicamocha) 

        break
       

    elif opcion == 3:
        nombreCliente = input("Por favor ingresa tu nombre completo : ")
        numeroAduls = int(input("Por favor ingrese cuantas personas adultas van a viajar: "))
        numeroNiños = int(input("Por favor ingrese cuantas niños van a viajar: "))

        print("Has seleccionado reservar para Llanos Orientales.")

        subTotal = (numeroAduls * precioAdulLlanosOrientales) + (numeroNiños * precioNiñoLlanosOrientales) 

        break

    else:
        print("Opción inválida. Por favor, ingrese un número válido.")

        break  
 
print("¡Reserva finalizada!")
print("Nombre del cliente ", nombreCliente)
print("Numero de pasajeros adultos mayores ", numeroAduls)
print("Numero de pasajeros menores ", numeroNiños)
print("Total a pagar ", subTotal)

