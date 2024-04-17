import funciones as fn
OP=True
while OP:
  print("OPCIONES:\n Sumar-1\n Restar-2\n Multiplicar-3\n Dividir-4\n Salir-5\n ")
  Opc=int(input("Ingrese numero de opcion "))
  if Opc==1:
    a=int(input("Ingrese numero "))
    b=int(input("Ingrese numero "))
    print(fn.suma(a,b))
  elif Opc==2:
    a=int(input("Ingrese numero "))
    b=int(input("Ingrese numero "))
    print(fn.resta(a,b))
  elif Opc==3:
    a=int(input("Ingrese numero "))
    b=int(input("Ingrese numero "))
    print(fn.multi(a,b))
  elif Opc==4:
    a=int(input("Ingrese numero "))
    b=int(input("Ingrese numero "))
    print(fn.div(a,b))
  elif Opc==5:
    break
  


lista_desordenada1 = [1,5,9,8,2,65,45,78,95,32,111,55,8,-5]

lista_ordenada1 = fn.ordenar_mayor_a_menor(lista_desordenada1)
print("Lista ordenada por la función :",lista_ordenada1)

lista_desordenada2= [51,18,89,65,4,2,3,5,96,85,74,14,25,36,32,65,98,87,45,12]

lista_ordenada2 = fn.orden_menor_a_mayor(lista_desordenada2)
print("Lista ordenada por la función :",lista_ordenada2)

lista_desordenada3= ["Bruno","Joaquin","Martin","Gonzalo","Franco","Matias","Quimy","Marti"]

lista_ordenada3 = fn.nombres(lista_desordenada3)
print("Lista ordenada por la función :",lista_ordenada3)