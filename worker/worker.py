import json
import os
import redis
from random import randint
from time import sleep

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    r = redis.Redis(host=redis_host, port=6379, db=0)
    print('Aguardando mensagens...')
    while True:
        mensagem = json.loads(r.blpop('sender')[1])
        # Simulando envio de e-mail...
        print('Mandando a mensagem:', mensagem['assunto'])
        sleep(randint(5, 15))
        print('Mensagem', mensagem['assunto'], 'enviada')
