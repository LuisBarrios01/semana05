import pandas as pd
import matplotlib.pyplot as ptl

datos = pd.read_excel('BI_Clientes.xlsx')
grupo1 = datos.groupby('SpanishEducation')
print(grupo1.describe())


print('--------------------------------------')
grupo2 = datos.groupby('SpanishEducation').count()
print(grupo2)

print('--------------------------------------')
grupo3 = datos.groupby('SpanishEducation')['SpanishEducation'].count()
print(grupo3)

print('--------------------------------------')
grupo4 = datos.groupby('SpanishEducation')['YearlyIncome'].sum()
print(grupo4)

print('--------------------------------------')
grupo5 = datos.groupby('SpanishEducation')['YearlyIncome'].mean()
print(grupo5)

print('--------------------------------------')
grupo3.plot(kind='bar')
ptl.show()
grupo4.plot(kind='pie')
ptl.show()
grupo5.plot(kind='barh')
ptl.show()