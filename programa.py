# imput


print("1=sumar")
print("2=restar")
print("3=multiplicacion")
print ("4=dividir")
print ("5=potencia")
print("6=logaritmo")
opcion= input("seleccione la opcion:   ")
opcion=int(opcion)
# selecione x e y
x = input ("seleccione x: ")
y = input ("seleccione y: ")
# convertir a float
x = float(x)
y = float(y)
# proccesing
if opcion == 1:
    r = x+y
elif opcion == 2:
    r = x-y 
elif opcion  ==3:
    r  = x * y 
elif opcion == 4:
    if y !=0: 
        r =x/y
    else :
        r= ("Error")
elif opcion  ==5:
    r=x**y
elif opcion ==6:
    import math 
    r=math.log(x,y)
print ("el resultado es :  "+str(r))  
    