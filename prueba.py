import pandas as pd
import numpy as np

# Crea una matriz de 13x13 con datos de tipo float como ejemplo
data_matrix = np.random.rand(13, 13)

# Define listas de nombres para las columnas y filas
column_names = ['Columna_{}'.format(i) for i in range(1, 14)]
row_names = ['Fila_{}'.format(i) for i in range(1, 14)]

# Crea el DataFrame
df = pd.DataFrame(data_matrix, columns=column_names, index=row_names)

# Visualiza el DataFrame resultante
print(df)