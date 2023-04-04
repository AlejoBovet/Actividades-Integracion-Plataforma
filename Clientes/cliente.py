from zeep import Client
from os import system
import time

#crear cliente 
cliente = Client('http://localhost/Actividades-Integracion-Plataforma/Servidor/soap.php?wsdl');

Historial = []
system("cls")
opcion=5

while opcion!=6:
    try:
        opcion=int(input("\tMenu\n1) Sumar\n2) restar\n3) multiplicar\n4) dividir\n5) Historial\n6) Salir\nIngrese su opcion aqui:---> "))
    except:
        system("cls")

    if opcion==1:
        system("cls")

        num1=int(input("Ingrese el primer digito\n"))
        num2=int(input("Ingrese el segundo digito\n"))


        if cliente.service.Suma(num1,num2):
            time.sleep(2)
            print('informacion enviada\n')
            time.sleep(5)
            print((cliente.service.Suma(num1,num2)))
            Historial.append(f"{num1} / {num2} ={cliente.service.Suma(num1,num2)}")
        else: 
            print('info no enviada')
        
            input("Presione enter para continuar")

    elif opcion==2:
        system("cls")

        num1=int(input("Ingrese el primer digito\n"))
        num2=int(input("Ingrese el segundo digito\n"))
        if cliente.service.resta(num1,num2):
            time.sleep(2)
            print('informacion enviada\n')
            time.sleep(5)
            print((cliente.service.resta(num1,num2)))
            Historial.append(f"{num1} / {num2} ={cliente.service.resta(num1,num2)}")
        else: 
            print('info no enviada');
        
            input("Presione enter para continuar")
        
    elif opcion==3:
        
        num1=int(input("Ingrese el primer digiton\n"))
        num2=int(input("Ingrese el segundo digito\n"))
        if cliente.service.multiplicacion(num1,num2):
            time.sleep(2)
            print('informacion enviada\n')
            time.sleep(5)
            print((cliente.service.multiplicacion(num1,num2)))
            Historial.append(f"{num1} / {num2} ={cliente.service.dmultiplicacion(num1,num2)}")
        else: 
            print('info no enviada')
        
            input("Presione enter para continuar")

    elif opcion==4:

        num1=int(input("Ingrese el primer digito\n"))
        num2=int(input("Ingrese el segundo digito\n"))
        if cliente.service.divicion(num1,num2):
            time.sleep(2)
            print('informacion enviada\n')
            time.sleep(5)
            print((cliente.service.divicion(num1,num2)))
            Historial.append(f"{num1} / {num2} ={cliente.service.divicion(num1,num2)}")
        else: 
            print('info no enviada')
        
            input("Presione enter para continuar")
    
    elif opcion==5:
        print("Historial")
        print(Historial)
        

    elif opcion==6:
        print ("salir")
        input("Presione enter para continuar")
        break
    

else:
    print("esa opcion no existe")






