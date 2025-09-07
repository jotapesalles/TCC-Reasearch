
# Assessing the Efficiency of Java Virtual Threads in Database-Driven Server Applications
Lasić, L.; Beronić, D.; Mihaljević, B.; Radovan, A. "Assessing the Efficiency of Java Virtual Threads in Database-Driven Server Applications".

## 1. Fichamento de Conteúdo

O artigo examina o impacto das _Virtual Threads_ (VTs) do Java em aplicações de servidor orientadas a banco de dados, especialmente sob o modelo thread por requisição. Os autores implementam e comparam duas versões de um servidor RESTful — uma baseada em _threads_ tradicionais e outra em VTs — realizando _benchmarks_ com seis bancos de dados: MySQL, PostgreSQL, Oracle, MongoDB, Cassandra, Neo4j. O estudo utiliza JDBC puro para isolar o efeito do modelo de concorrência. Os resultados mostram que as VTs reduzem significativamente a latência média das operações CRUD, com ganhos mais expressivos em bancos como PostgreSQL de até 20,76% e Cassandra de até 24,6%. O artigo conclui que as VTs são mais eficientes que as threads tradicionais em cenários de alta concorrência e operações intensivas de entrada e saída, sendo especialmente vantajosas para bancos de dados não relacionais.

## 2. Fichamento Bibliográfico

* _Modelo Thread-per-request_: Arquitetura onde cada requisição é processada por uma thread dedicada. Com threads tradicionais, o custo de criação limita a escalabilidade; VTs resolvem esse gargalo (página 2).

* _Continuation_: Estrutura que representa o estado de execução de uma VT, permitindo pausar e retomar sua execução, o que viabiliza o desacoplamento eficiente das carrier threads(página 5).

* Metodologia de _Benchmark_: Aplicação RESTful implementada em duas versões (threads tradicionais e VTs), realizando operações CRUD em bancos de dados com latência média medida sob carga de requisições/segundo (página 8).

## 3. Fichamento de Citações

* _"Virtual Threads represent a contemporary structured concurrency model in Java Virtual Machine (JVM) seeking to increase the performance of multi-threaded Java applications by optimizing the utilization of the operating system (OS) resources."_ 
* _"The creation of Java threads significantly leans on the operating system (OS) kernel threads, making them inherently heavyweight."_ 

* _"When the Virtual Thread gets blocked, the JVM releases the OS Thread, thereby allowing it to be used by another Virtual Thread instead of idly waiting for a resource to be unblocked."_

* _"Throughout the experiments, a consistent pattern of performance enhancement was observed with the introduction of Virtual Threads, underscoring their potential benefits."_ 

* _"Synthesizing observations from both applications using relational and non-relational database systems, Virtual Threads consistently demonstrate superior performance over traditional threads."_ 

