# Considerations for Integrating Virtual Threads in a Java Framework: a Quarkus Example in a Resource-Constrained Environment

Navarro, Arthur; Ponge, Julien; Le Mouël, Frédéric; Escoffier, Clément. “Considerations for Integrating Virtual Threads in a Java Framework: a Quarkus Example in a Resource-Constrained Environment,” in Proceedings of the 17th ACM International Conference on Distributed and Event-Based Systems (DEBS ’23), pp. 103–114, 2023. doi: 10.1145/3583678.3596895

## 1. Fichamento de Conteúdo

O artigo investiga, por meio de experimentos, como _Virtual Threads_ (VT) do Java se comportam quando integradas a um _stack_ moderno baseado em Quarkus, especialmente sob restrições de CPU e memória. Os autores comparam três estilos: tradicional bloqueante, reativo (_event loops_ + I/O não bloqueante) e VT. O estudo mede latência e vazão em cargas crescentes e discute efeitos colaterais como pressão de _Garbage Collection_ (GC) e custos de _ThreadLocal_ ao escalar para muitas VTs. Os resultados sugerem que VT supera o bloqueante clássico em diversos cenários _I/O-bound_, mas ainda fica atrás do reativo em regimes de alta concorrência, sobretudo quando o runtime pressupõe pouacos event loops e o aplicativo cria milhares de VTs, gerando incompatibilidades internas. A principal contribuição é mostrar onde VT compensa pela simplicidade do código (imperativo, fácil de ler e depurar) e onde o reativo ainda domina (picos de concorrência e eficiência extrema). Como implicação prática, os autores recomendam combinar observabilidade para identificar hotspots (GC, contenção através de thread pinning) e tomar decisões arquiteturais conscientes ao ativar VT por padrão.

## 2. Fichamento Bibliográfico 

* _Virtual Threads (VT)_: threads leves gerenciadas pela JVM que permitem código bloqueante escalar para muitas unidades concorrentes mantendo o estilo imperativo. Úteis para I/O-bound; não monopolizam threads do SO, permitindo alto grau de concorrência com baixa sobrecarga (página 1).

* _Containers_ (Ambiente com recursos restritos): cenários com CPU/RAM limitados evidenciam diferenças entre VT, reativo e bloqueante (página 1).
 
* _Platform Threads (PT)_: modelo tradicional em Java; cada thread da aplicação corresponde a uma thread do SO, com custo de criação e gerenciamento mais alto (página 1).

* _Event-loop_ (Modelo reativo): arquitetura baseada em Vert.x/Netty com I/O não bloqueante sobre poucos event loops; alta eficiência sob concorrência elevada, porém maior complexidade. (página 3).

* _Netty/Vert.x_ (integração): stacks otimizados para poucos _event loops_; ao criar muitas VTs pode haver mismatch (buffers, context switching) que afeta latência (página 4).

* _Carrier threads_ & chamadas bloqueantes: VTs são agendadas sobre _carrier threads_; trechos bloqueantes longos e certas APIs podem degradar o escalonamento.(página 4).

* _ThreadLocal_ e pressão de GC: uso intenso de _ThreadLocal_ e alocações transitórias aumenta pressão de GC e pode piorar P95/P99 quando há milhares de VTs. (página 5).

* Métricas de desempenho: latência (com ênfase em P95/P99) e _throughput_ são as métricas principais; também avaliar CPU/memória e _threads_ ativas. (página 6)

## 3. Fichamento de Citações

* _"This study reveals that the integration of virtual threads in Quarkus doesn’t perform as well as Quarkus-reactive."_

* _“[…] virtual threads enable writing blocking code that scales to large numbers of concurrent tasks.”_

* _“In resource-constrained containers, reactive remains more efficient at high concurrency compared to VT.”_

* _“We observed increased GC pressure related to ThreadLocal usage when spawning many VTs.”_

* _“The mismatch between Netty’s event-loop model and massive VT creation impacts tail latency.”_

* _"The study highlights the mismatch between the core assumptions of Netty, which assumes a limited number of event-loop threads, and the core assumptions of virtual threads, which assume that they are cheap to create and can be spun up as needed."_
