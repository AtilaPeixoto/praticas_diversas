import schedule
import time

def tarefa():
    print('executando...')
    
# schedule.cada.tempo.fazer
schedule.every(5).seconds.do(tarefa)
schedule.every().monday.at('08:00').do(tarefa)
schedule.every().day.at('08:00').do(tarefa)


while True:
    schedule.run_pending()
    time.sleep(1)
    
