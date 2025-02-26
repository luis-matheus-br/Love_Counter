
from datetime import datetime
import time

# Definir a data inicial
data_inicial = datetime(2018, 12, 1)

while True:
    # Obter a data e hora atual
    agora = datetime.now()

    # Calcular a diferença
    diferenca = agora - data_inicial

    # Exibir o tempo decorrido
    print(f"Tempo desde 01/12/2018: {diferenca.days} dias, {diferenca.seconds // 3600} horas, {(diferenca.seconds // 60) % 60} minutos, {diferenca.seconds % 60} segundos", end="\r")

    # Aguardar 1 segundo antes de atualizar
    time.sleep(1)


