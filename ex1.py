import pandas as pd

#Criando uma lista
tabela = { 'Data': ['01-01-2016', '02-01-2016', '03-01-2016', '04-01-2016', '05-01-2016', '06-01-2016','07-01-2016', '08-01-2016', '09-01-2016', '10-01-2016'],
          'Temperatura média': [26.0, 28.0, 28.0, 30.0, 30.0, 29.0, 26.0, 26.0, 26.0, 27.0], 
          
          }

#Trandormando em tabela
dataframe = pd.DataFrame(tabela)
print(dataframe)