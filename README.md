# Apache Kafka Demo
Link to docs: [Google sheets](https://drive.google.com/drive/folders/1WgUmNJzBZ12FlMsoAMJObUDGawCpizyN?usp=sharing)

## Overview

This project comprises three essential components:

1. **Pokemon API Fetcher (Producer):** This component acts as a producer within the cluster. The script employs the requests package to establish a connection with the Pokemon API (https://pokeapi.co/) and stream a comprehensive list of Pokemons to the Apache Kafka cluster.

2. **Kafka Consumer:** This program is designed to seamlessly connect to the Apache Kafka cluster, receiving real-time events and logging them to the standard output (stdout).

3. **Kafka Cluster:** The heart of the system, this cluster includes a Zookeeper and three Brokers, ensuring robust data management and distribution.
## Run Locally

Clone the project

```bash
  git clone https://github.com/omerap12/kafka_assignment.git
```

Go to the project directory

```bash
  cd kafka_assignment
```

Start the project

```bash
  docker compose up 
```

