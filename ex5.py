
import delorean

# Convertendo o horario para o fuso-horario de Chicago (USA)
agora = delorean.now()
agora_em_chicago = agora.shift('America/Chicago')


print(agora_em_chicago)
