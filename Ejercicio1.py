import pandas as pd
import matplotlib.pyplot as ptl
import numpy as np

archivo = pd.read_csv('WEO_Data.csv',thousands=',',decimal='.')
print(archivo)
archivo.rename(columns={'Country':'Pais'},inplace=True)
archivo.set_index('Pais',inplace=True)
lista1=list(map(str,range(2000,2024)))

def grafico1():
    archivo.sort_values(by='2022', ascending=False, inplace=True)
    top5 = archivo[lista1].head(5)
    top5 = top5.transpose()
    top5.plot(kind='area')
    ptl.title('Top 5 paises (PBI)')
    ptl.ylabel('Billones de $')
    ptl.xlabel('Años')
    ptl.show()

grafico1()