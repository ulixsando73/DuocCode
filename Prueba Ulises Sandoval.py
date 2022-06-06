from logging import exception
from pickle import APPEND


opt= ""
clientes= []
while opt != 4:
    print("1.-Registrar Cliente")
    print("2.-Suscripcion")
    print("3.-Consultar Datos Cliente")
    print("4.-Salir")
    opt= int(input("Ingrese el numero de la opcion que desea aplicar: "))

    try:
        if(opt == 1):
            cliente= []
            rut= ""
            nombre= ""
            direccion= ""
            comuna= ""
            correo= ""
            edad= 0
            celular= ""
            tipo= ""
            suscripcion= ""

            rut = input("Ingrese su Rut(sin punto ni digito verificador): ")
            if(len(rut) !=8):
                print("Rut debe tener 8 caracteres")
                break
            if("." in rut or  "-"in rut):
                print("Rut no debe tener punto ni guion")
                break

            nombre= input("Ingrese nombre de cliente: ")
            direccion= input("ingrese direccion del cliente: ")
            comuna= ("Ingrese comuna del cliente: ")
            correo= ("Ingrese correo del cliente: ")

            if("@" not in correo):
                print("Correo debe tener al menos una @")
                break

            edad= int(input("Ingrese edad del cliente"))
            if(edad<0 and edad>110):
                print("La edad debe estar entre 0 y 110")
                break
            
            genero= input("Ingresar genero del cliente(M para Masculino y F para Femenino")
            genero=genero.strip()
            if(genero !="M" and genero !="F"):
                print("Genero debe ser solamente M o F")
                break

            celular= input("Ingrese numero celular: ")

            tipo= input("Ingrese tipo: Premium - Silver - Gold: ")
            tipo= tipo.upper()
            tipo= tipo.strip()
            if(tipo!= "Premium" and tipo!= "Silver" and tipo!= "Gold"):
                print("Tipo debe ser solamente Premuim Silver o Gold")
                break

            cliente.append(rut)
            cliente.append(nombre)
            cliente.append(direccion)
            cliente.append(comuna)
            cliente.append(correo)
            cliente.append(edad)
            cliente.append(genero)
            cliente.append(celular)
            cliente.append(tipo)
            cliente.append(suscripcion)

            clientes.append(cliente)
            print(clientes)

        if(opt==2):   
            rut= input("Ingrese rut que desea buscar")
            for cliente in clientes:
                if(cliente[0] ==rut):
                    print("Datos del cliente: \n")
                    print(f"Rut del cliente: {cliente[0]}")
                    print(f"Nombre del cliente: {cliente[1]}")
                    print(f"Direccion del clienrte: {cliente[2]}")
                    print(f"Comuna del cliente: {cliente[3]}")
                    print(f"Correo del cliente: {cliente[4]}")
                    print(f"Edad del cliente: {cliente[5]}")
                    if(cliente[6]=="M"):
                        print(f"Genero del cliente: Masculino")
                    elif(cliente[6]=="F"):
                        print(f"Genero del cliente: Femenino")
                        print(F"Celular del cliente: {cliente[7]}")
                    if(cliente[8]=="Premium"):
                        print("Tipo de cliente: Premium")
                    elif(cliente[8]=="Silver"):
                        print("Tipo de cliente: Silver")
                    elif(cliente[8]=="Gold"):
                        print("Tipo de cliente: Gold")
                    print(f"Tipo de suscripcion del cliente: {cliente[9]}")

    except ValueError:
        print("valor debe ser numerico")
        if(opt>4):
            raise exception("Opcion elegida debe ser del 1 a 4")
print("Gracias por subcribirse  a la app de Juan Maestro")



            
