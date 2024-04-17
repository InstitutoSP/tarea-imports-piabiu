def suma(a,b):
      sumar=(a+b)
      return(sumar)
def resta(a,b):
    resta=(a-b)
    return(resta)
def multi(a,b):
    mult=(a*b)
    return(mult)
def div(a,b):
  div=(a/b)
  return(div)

def ordenar_mayor_a_menor(list1):

    stop=True
    listaord=[]
    while stop:
        val_max= list1[0]
        for i in range(len(list1)):
            x=list1[i]

            if x > val_max:
                val_max=x

        listaord.append(val_max)
        list1.remove(val_max)

        if len(list1)==0:
            stop=False
    
    return listaord

def orden_menor_a_mayor(list2):
    stop=True
    listaord=[]
    while stop:
        val_min= list2[0]
        for i in range(len(list2)):
            x=list2[i]

            if x < val_min:
                val_min=x

        listaord.append(val_min)
        list2.remove(val_min)

        if len(list2)==0:
            stop=False
    return listaord
def nombres(list3):
    stop=True
    listaord=[]
    while stop:
        menor_le= list3[0]
        for i in range(len(list3)):
            x=list3[i]

            if x < menor_le:
                menor_le=x

        listaord.append(menor_le)
        list3.remove(menor_le)

        if len(list3)==0:
            stop=False
    return listaord