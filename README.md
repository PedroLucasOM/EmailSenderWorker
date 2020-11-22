<h1 align="center">Welcome to EmailSenderWorker 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <img src="https://img.shields.io/badge/nginx-1.13.0-blue.svg" />
  <img src="https://img.shields.io/badge/postgres-9.6.0-blue.svg" />
  <img src="https://img.shields.io/badge/python-3.6.0-blue.svg" />
  <img src="https://img.shields.io/badge/redis-3.2.0-blue.svg" />
  <a href="fasf" target="_blank">
    <img alt="documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
  <a href="https://github.com/kefranabg/readme-md-generator/graphs/commit-activity" target="_blank">
    <img alt="maintenance" src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" />
  </a>
  <a href="https://twitter.com/PedroLucasOM" target="_blank">
    <img alt="Twitter: PedroLucasOM" src="https://img.shields.io/twitter/follow/PedroLucasOM.svg?style=social" />
  </a>
</p>

> 💻 Aplicação escalável para simulação de envio de e-mails com workers do Docker 🐳 e Pyhton com o micro-framework Bottle 🐍

# 🏠 [Homepage](https://github.com/PedroLucasOM/EmailSenderWorker)

# Prerequisites

- docker

# Arquitetura

Observe abaixo o modelo arquitetural usado na aplicação:

<img src="https://github.com/PedroLucasOM/EmailSenderWorker/blob/master/images/Diagrama%20em%20branco.png" width="600" />

# Usage

Com o docker iniciado, execute os passos a seguir:

### Worker único

Para rodar a aplicação com um único worker, execute o seguinte comando:

```sh
docker-compose up -d
```

Inicialmente, ao usar o comando acima, a aplicação irá iniciar com apenas 1 processador de mensagens de e-mail (worker), enfileirando as requisições e trabalhando de forma síncrona, ou seja apenas uma requisição de mensagem é processada por vez.

Veja o exemplo a seguir:

![worker1](https://github.com/PedroLucasOM/EmailSenderWorker/blob/master/images/worker1.gif)

### Worker múltiplo

Para rodar a aplicação com múltiplos workers, execute o seguinte comando:

```sh
docker-compose up -d --scale worker=3
```

Dessa forma, ao usar o comando acima, a aplicação irá iniciar com 3 processadores de mensagens de e-mail (workers), alocando as mensagens entre os workers disponíveis e enfileirando em cada worker quando todos estiverem ocupados. Dessa forma, a aplicação trabalhará de forma assíncrona entre 3 workers.

Veja o exemplo a seguir:

![worker2](https://github.com/PedroLucasOM/EmailSenderWorker/blob/master/images/worker2.gif)

### Interface para envio de requisição

Para enviar as mensagens, após iniciar a aplicação, acesse <a href="http://localhost:80">http://localhost:80</a>

Você verá esta tela:

<img src="https://github.com/PedroLucasOM/EmailSenderWorker/blob/master/images/front.png" width="600" />

### Comparando

#### Worker único

Na primeira situação, cada mensagem enviada precisa esperar a mensagem anterior ser processada, já que existem apenas um worker.

Observe:

<img src="https://github.com/PedroLucasOM/EmailSenderWorker/blob/master/images/worker-1.png" width="600" />

A mensagem 1 foi processada inicialmente.
A mensagem 2 precisou esperar a mensagem 1 terminar o seu processamento.
A mensagem 3 precisou esperar a mensagem 2 terminar o seu processamento.

#### Worker múltiplo

Na segunda situação, cada mensagem enviada verificou qual worker estava disponível para processá-la, ocupando assim os 3 workers disponíveis e tornando o processamento das 3 mensagens independentes.

Observe:

<img src="https://github.com/PedroLucasOM/EmailSenderWorker/blob/master/images/worker-2.png" width="600" />

A mensagem 1 foi processada inicialmente no worker 1.
A mensagem 2 foi processada no worker 3 (buscou um dos outros workers disponíveis)
A mensagem 3 foi processada no worker 2 (buscou o último worker disponível)

Caso uma 4ª mensagem fosse enviada para ser processada, ela seria enfieleirada em um dos workers, já que todos estão ocupados.

# Author

👤 **Pedro Lucas**

* Twitter: [@PedroLucasOM](https://twitter.com/PedroLucasOM)
* Github: [@PedroLucasOM](https://github.com/PedroLucasOM)
* LinkedIn: [@PedroLucasOM](https://linkedin.com/in/PedroLucasOM)

# 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/PedroLucasOM/EmailSenderWorker/issues). 

# Show your support

Give a ⭐️ if this project helped you!

# 📝 License

Copyright © 2020 [Pedro Lucas](https://github.com/PedroLucasOM).<br />
