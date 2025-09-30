# Java Single vs. Platform vs. Virtual Threads Runtime Performance Assessment in the Context of Key Class Detection

Chirilă, Ciprian-Bogdan; Şora, Ioana. “Java Single vs. Platform vs. Virtual Threads Runtime Performance Assessment in the Context of Key Class Detection,” in 2024 IEEE 18th International Symposium on Applied Computational Intelligence and Informatics (SACI), 2024. doi: [10.1109/SACI60582.2024.10619722](https://doi.org/10.1109/SACI60582.2024.10619722).

## 1. Fichamento de Conteúdo

O artigo apresenta uma avaliação comparativa entre três modelos de concorrência em Java: _single thread (ST)_, _platform threads (PT)_ e _virtual threads (VT)_. O contexto é a detecção de "classes-chave": classes mais importantes em um sistema usadas como ponto de partida para reengenharia ou documentação. Sobre o problema é o tempo de execução de algoritmos de análise de grafos como HITS e PageRank, críticos em sistemas grandes ou quando executados repetidamente. Os autores implementaram versões paralelas desses algoritmos usando os três modelos e os executaram em 14 projetos Java de tamanhos variados, em quatro máquinas, sendo elas Windoes e Linux. Os resultados mostram que o modelo VT, introduzido pelo Projeto Loom, supera significativamente ST e PT, com redução de tempo de execução de 58,41% em relação ao modelo _single thread_. Observa-se também que, para projetos com menos de 1.200 classes, o modelo ST apresenta melhor desempenho que PT, enquanto PT só fica à frente em projetos maiores.

## 2. Fichamento Bibliográfico

* _Key Classes (Classes-Chave)_: classes consideradas mais importantes do sistema; detectadas por algoritmos de análise de grafos para apoiar reengenharia e documentação.
* _Algoritmo HITS_: calcula scores de "authority" e "hub" para nós de um grafo; aplicado às classes para estimar importância baseada em relações.
* _Algoritmo PageRank_: atribui pontuações numéricas a nós (classes) para representar importância, considerando referências entre classes.

## 3. Fichamento de Citações

* _"The results show that single thread implementations for project having a relative small number of classes, namely under 1,200, perform better than platform threads implementations. Conversely, virtual threads perform better than any single thread implementation."_
* _"We conclude that virtual thread model speeds up the computation of attributes with a runtime decrease of 58.41% against the single thread model."_
* _"Virtual threads are characterized by their lightweight nature and the ability to execute Java code on an underlying OS thread without monopolizing it for the entirety of the code’s execution."_
* _"The runtime execution of the two algorithms is critical when they run on graphs having different class relationship weights."_
* _"The VT model outperforms both ST and PT. Clearly, the recent advent of VT model is a success."_

