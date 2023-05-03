
from flashtext2 import KeywordProcessor

# Criar um processador de palavras-chave
kp = KeywordProcessor()

# Palavras-chaves
kp.add_keyword('mínima ideia')
kp.add_keyword('O que é')
kp.add_keyword('a vida')

# Exemplo de texto
texto = 'O que é a vida ? não faço a mínima ideia'

# Encontrando as palavras chaves
palavras_chave_encontradas = kp.extract_keywords(texto)


print(palavras_chave_encontradas)