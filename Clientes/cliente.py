from zeep import Client
from os import system

#crear cliente 
cliente = Client('http://localhost/masterphp/Actividades-Integracion-Plataforma/soap.php?wsdl');

system("cls")
opcion=5

while opcion!=4:
    try:
        opcion=int(input("\tMenu\n1) Sumar\n2) restar\n3) multiplicar\n4) dividir\n5) Salir\nIngrese su opcion aqui:---> "))
    except:
        system("cls")

    if opcion==1:
        system("cls")

        num1=int(input("Ingrese el primer digito"))
        num2=int(input("Ingrese el segundo digito"))


        if cliente.service.Suma(num1,num2):
            print('informacion enviada')
            print (cliente.service.Suma(num1,num2))
        else: 
            print('info no enviada');
        
            input("Presione enter para continuar")

    elif opcion==2:
        system("cls")

        num1=int(input("Ingrese el primer digito"))
        num2=int(input("Ingrese el segundo digito"))
        if cliente.service.resta(num1,num2):
            print('informacion enviada')
            print (cliente.service.resta(num1,num2))
        else: 
            print('info no enviada');
        
            input("Presione enter para continuar")
        
    elif opcion==3:
        input("Presione enter para continuar")

    elif opcion==4:
        input("Presione enter para continuar")

    elif opcion==5:
        print ("salir")
        input("Presione enter para continuar")
        break
    

else:
    print("esa opcion no existe")






