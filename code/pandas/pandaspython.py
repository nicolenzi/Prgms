import pandas as pd
import numpy as np

#s = pd.Series([2,4,6])

#print(s)
#print(s.count())
#print(s.sum())
#print(s.min())
#print(s.max())
#print(s.describe())

dataF = pd.DataFrame(data = [["uno",1,1.0],["dos",2,2.0]])
print(dataF)

"""
            DROPNA

dropna elimina todas las filas para "axis=0" o para columna "axis=1".
Argumentos de dropna:
#axis:especifica si se deben eliminar las filas "axis=0" 0 columnas "axis=1"

#subset:especifica un subconjunto de columnas a considerar para el valor duplicado
 cuando el valor sea"axis=0"

#inplace: 

#keep:especifica que valores duplicados conservar, mantener puede ser igual que el 
primero, el ultimo falso para eliminar todos los duplicados

"""