import arrow 
s ='2023-04-25 21:30:50'
  
# Covertendo o formato da data
date = arrow.get(s, 'YYYY-MM-DD HH:mm:ss') 
print(date) 
