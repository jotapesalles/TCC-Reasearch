
# Automated Runtime Transition between Virtual and Platform Threads in the Java Virtual Machine
Rosà, Andrea; Basso, Matteo; Bohnhoff, Leonardo; Binder, Walter. "Automated Runtime Transition between Virtual and Platform Threads in the Java Virtual Machine".

#### 1. Fichamento de Conteúdo
O artigo propõe um novo framework para a Máquina Virtual Java (JVM) capaz de selecionar e alternar automaticamente entre o uso de _platform threads_ (PT) e _virtual threads_ (VT) em tempo de execução. A necessidade surge porque a escolha ótima entre os dois tipos de thread depende do comportamento da aplicação, que pode variar ao longo do tempo: _virtual threads_ melhoram _throughput_ em cargas _I/O-bound_, enquanto em cargas _CPU-bound_ podem introduzir sobrecargas.

O framework monitora continuamente métricas como taxa de operações de bloqueio, utilização de CPU e número de threads ativas. Com base nesses sinais, o usuário pode definir critérios para classificar qual tipo de thread é o "preferido" em um dado momento. O sistema então inicia uma transição para adaptar as threads em execução ao tipo preferido, encerrando threads do tipo não preferido e criando novas do tipo ideal.

A avaliação preliminar foi feita usando o servidor _Eclipse Jetty_. Os resultados mostram que o framework tende a selecionar o tipo de thread que maximiza o _throughput_ conforme o comportamento da aplicação, sem introduzir penalidades de desempenho significativas; a sobrecarga medida foi insignificante, com os testes indicando até um leve ganho médio de desempenho.

#### 2. Fichamento Bibliográfico
* _Framework Adaptativo_: sistema proposto capaz de adaptar automaticamente o tipo de thread usado pela aplicação conforme seu comportamento muda.
* _I/O-bound_: quando uma tarefa é limitada pelo tempo de espera de entrada/saída (rede, disco, banco de dados), e não pela capacidade de processamento do CPU.
* _CPU-bound_: quando uma tarefa é limitada pela capacidade de processamento do processador (CPU), e não por esperas de entrada/saída como rede ou disco.

#### 3. Fichamento de Citações
* _"Virtual threads promise a significant throughput improvement in workloads that make intensive use of blocking operations, but incur performance overheads in CPU-bound workloads... Hence, the optimal choice between platform and virtual threads depends on application behavior (which can change significantly during the execution) and on the system running the application."_
* _"Deciding which thread type (i.e., platform or virtual threads) leads to the highest throughput is generally very hard, as it greatly depends on the application behavior and on the underlying system."*
* _"Our preliminary evaluation results show that the framework applies transitions to the thread type yielding the highest throughput depending on the application’s behavior, without introducing performance penalties."*
* _"The average slowdown factor is 0.994× ± 0.02 (actually a speedup), which demonstrates that, on average, using the proposed framework incurs in negligible or no overhead and can be used in production-standard applications without performance penalties."_
