#Alumno: Ceccardi Andres / Tecnicatura Superior en Programacion.
#Constante de kaprekar realizado en Python.
#IDE: Thonny
#Python v3.9 
import msvcrt
tab = []
loop = 'loop'
# tab contendrá todos los números de Kaprekar encontrados
# loop es solo para una mejor redacción

def asc(n):
    #pone los dígitos del número en forma ascendente ...
    return int(''.join(sorted(str(n))))

def desc(n):
    #y en orden descendente
    return int(''.join(sorted(str(n))[::-1]))

n = input("Ingrese el numero: ")
try:
    n = int(n)
except:
    #suponiendo n = 2016 para evitar que el programa se bloquee 
    print("\nNumero invalido especificado!!!\nContando a n como n = 2016.")
    n = "2016"
print("\nTransformando", str(n) + ":")

while True:
    #La iteracion asigna la nueva diferencia
    print(desc(n), "-", asc(n), "=", desc(n)-asc(n))
    n = desc(n) - asc(n)

    if n not in tab:
        #comprueba si ya encontro el numero
        tab.append(n)
    else:
        if tab.index(n) == len(tab)-1:
        #si se encuentra último, es una constante ...
            tab = []
            tab.append(n)
            loop = 'constante'
        else:
        #De lo contrario es un bucle
            tab = tab[tab.index(n):]
        #quitar los primeros elementos sin bucle
        break

print(  loop, 'de kaprekar', 'alcanzada:', tab)
msvcrt.getch() #evita que se cierre el programa automaticamente luego de encontrar
                #un resultado
