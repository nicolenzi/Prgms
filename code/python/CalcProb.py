print("""
----------------------------
  CALCULADOR DE PROBALILIDAD 
----------------------------

* Con el primer valor se refiere al numero de "tiradas",
o mas bien al numero de posibilidades que hay en que se
repita el hecho de realizar otro numero aleatorio. El 
segundo numero se refiere a espacio muestral, cantidad
de todos los resultados posibles que ocurriran como re_
sultado.
""")

def prblidd(arg1,arg2):
    return arg1 / arg2

valor1 = input("Ingrese valor 1: ")
valor2 = input("Ingrese valor 2: ")
total = prblidd(int(valor1),int(valor2))

print(total,"de probabilidad")
