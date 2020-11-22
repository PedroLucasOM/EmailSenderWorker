<h1 align="center">Welcome to EmailSenderWorker 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <img src="https://img.shields.io/badge/nginx-1.13.0-blue.svg" />
  <img src="https://img.shields.io/badge/postgres-9.6.0-blue.svg" />
  <img src="https://img.shields.io/badge/python-3.6.0-blue.svg" />
  <img src="https://img.shields.io/badge/redis-3.2.0-blue.svg" />
  <a href="fasf" target="_blank">
    <img alt="documentation" src="https://img.shields.io/badge/documentation-yes-green.svg" />
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

# Architecture

Observe the architectural model used in the application below:

<img src="https://github.com/PedroLucasOM/EmailSenderWorker/blob/master/images/Diagrama%20em%20branco.png" width="600" />

# Usage

With the docker started, perform the following steps:

### Single worker

To run the application with a single worker, run the following command:

```sh
docker-compose up -d
```

Initially, when using the command above, the application will start with just 1 email message processor (worker), queuing requests and working synchronously, that is, only one message request is processed at a time.

See the following example:

<img src="https://github.com/PedroLucasOM/EmailSenderWorker/blob/master/images/worker1.gif" width="600" />

### Multiple worker

To run the application with multiple workers, run the following command:

```sh
docker-compose up -d --scale worker=3
```

That way, when using the command above, the application will start with 3 email message processors (workers), allocating messages among the available workers and queuing in each worker when everyone is busy. Thus, the application will work asynchronously between 3 workers.

See the following example:

<img src="https://github.com/PedroLucasOM/EmailSenderWorker/blob/master/images/worker2.gif" width="600" />

### Interface for sending requests

To send the messages, after starting the application, access <a href="http://localhost:80">http://localhost:80</a>

You will see this screen:

<img src="https://github.com/PedroLucasOM/EmailSenderWorker/blob/master/images/front.png" width="600" />

### Comparing

#### Single worker

In the first situation, each message sent needs to wait for the previous message to be processed, since there is only one worker.

Watch:

<img src="https://github.com/PedroLucasOM/EmailSenderWorker/blob/master/images/worker-1.png" width="600" />

Message 1 was processed initially.
Message 2 had to wait for message 1 to finish processing.
Message 3 had to wait for message 2 to finish processing.

#### Multiple worker

In the second situation, each message sent checked which worker was available to process it, thus occupying the 3 available workers and making the processing of the 3 messages independent.

Watch:

<img src="https://github.com/PedroLucasOM/EmailSenderWorker/blob/master/images/worker-3.png" width="600" />

Message 1 was initially processed at worker 1.
Message 2 was processed on worker 3 (fetched one of the other available workers)
Message 3 was processed on worker 2 (fetched the last available worker)

If a 4th message were sent to be processed, it would be queued in one of the workers, since everyone is busy.

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
