import nltk
nltk.download('punkt') 

# Definir um texto de exemplo
texto1 = 'Era uma vez… uma lebre e uma tartaruga \n'
texto2 = 'A lebre vivia caçoando da lerdeza da tartaruga.Certa vez, a tartaruga já muito cansada por ser alvo de brincadeiras, desafiou a lebre para uma corrida.A lebre muito segura de si, aceitou prontamente.'
texto3 = 'Não perdendo tempo, a tartaruga pois-se a caminhar, com seus passinhos lentos, porém, firmes.'
texto4= '\nLogo a lebre ultrapassou a adversária, e vendo que ganharia fácil, parou e resolveu cochilar um pouco.'
texto5 = 'Quando acordou, não viu a tartaruga e começou a correr.'
texto6 = 'Já na reta final, viu finalmente a sua adversária cruzando a linha de chegada, toda sorridente.'

texto = (texto1 +  texto2 + texto3 + texto4 + texto5 + texto6)


# Colocar tokens nas palavras do texto
palavras = nltk.word_tokenize(texto)

# Selecionando apenas palavras que começam com a letra l
palavras_a = [palavra for palavra in palavras if palavra.lower().startswith('l')]

# Mostrando quais são as palavras
for palavra in palavras_a:
    print("As palavras que começam com a letra l são: ", palavra)
