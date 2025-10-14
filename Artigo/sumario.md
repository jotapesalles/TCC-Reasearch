# Adoção e Uso de Virtual Threads em Projetos Java: Um Estudo Empírico

1. João Paulo de Sales Pimenta

* Danilo Maia
* Leonardo Vilela
* Raphael Ramos
* Cleiton Tavares

## Introdução
1. A área da Engenharia de Software tratada neste trabalho é: “aplicações distribuídas, principalmente por arquiteturas de microsserviços hospedadas em ambientes de computação em nuvem, nas quais a gestão eficiente de CPU e memória é crítica para desempenho e custo operacional”, com foco na concorrência na plataforma Java (_platform threads_ vs. _virtual threads_) e seus impactos de desempenho, complexidade e adoção.
2. O problema que este trabalho busca resolver nessa área é: “não há um panorama empírico consolidado sobre a adoção contemporânea de _virtual threads_ em projetos Java: onde aparecem, com que prevalência em relação a threads de plataforma e quais padrões concretos de uso predominam em diferentes _frameworks_ e domínios.”
3. Resolver este problema é relevante porque: “as _virtual threads_ foram concebidas para promover melhoria de desempenho, eficiência e racionalização de recursos em software, otimizando o uso de CPU e memória em aplicações intensivas em I/O e aumentando a taxa de transferência (_throughput_). Trata-se de uma capacidade estabilizada no JDK21, sobre a qual ainda há escassez de estudos em cenários realistas, especialmente em aplicações orientadas a banco de dados na nuvem. Em paralelo, há sinais de adoção em _frameworks_ e servidores web populares, como Quarkus, Spring e Jetty. Nesse contexto, compreender benefícios, custos e desafios de integração torna-se essencial para embasar decisões técnicas, mitigar riscos e orientar a construção de sistemas escaláveis e eficientes. Além disso, a estabilização das VTs no JDK21 cria um período oportuno para observar tendências reais de adoção e consolidar recomendações que orientem decisões de engenharia com foco em automação, eficiência e uso de recursos.”
4. O objetivo geral deste trabalho é: “investigar a adoção contemporânea de virtual threads em projetos Java, categorizando sua prevalência, padrões de uso e fatores associados, em contraste com o emprego de threads de plataforma.”
5. Os três objetivos específicos deste trabalho são:
“(i) minerar repositórios de código abertos para identificar indícios de adoção (por exemplo, ocorrências de `Thread.ofVirtual()` e executores de VT, além de opções de _frameworks_ que habilitam VT);”
“(ii) classificar padrões de uso observados (como _thread-per-request_, mapeamentos VTs ou PTs e arranjos híbridos com _pools_);”
“(iii) analisar fatores associados à adoção, incluindo _framework_, versão do JDK, estilo de comunicação entre serviços (APIs REST e corretores de mensagens) e bibliotecas de acesso a dados.”

## Fundamentação Teórica

1. O conceito/teoria principal associado a este trabalho é ....  A sua definição neste trabalho  é conforme definido no trabalho .... pelo autor ...
1. O conceito/teoria secundário associado a este trabalho é ....  A sua definição neste trabalho é conforme definido no trabalho .... pelo autor ...
1. O conceito/teoria terciário associado a este trabalho é ....  A sua definição neste trabalho é conforme definido no trabalho .... pelo autor ...

## Trabalhos Relacionados

1. O trabalho mais relacionado é Assessing the Efficiency of Java Virtual Threads in Database-Driven Server Applications (Lašić et al.), publicado em 2024, porque mede diretamente o cenário mais comum do seu recorte (aplicações Java _I/O-bound_ com banco de dados no modelo _thread-per-request_) e entrega evidências de ganho de desempenho com _virtual threads_ que servirão como referência para interpretar achados na mineração de repositórios de software de código aberto.
2. O segundo trabalho mais relacionado é Considerations for Integrating Virtual Threads in a Java Framework: A Quarkus Example in a Resource-Constrained Environment (Navarro et al.), publicado em 2023, porque mostra condições concretas em que virtual threads não superam a _stack_ reativa (Quarkus/Netty), oferecendo limites de validade e critérios práticos para classificar projetos de código aberto de acordo com a concorrência.
3. O terceiro trabalho mais relacionado é Automated Runtime Transition between Virtual and Platform Threads in the JVM (Rosà et al.), publicado em 2023, porque introduz adaptação dinâmica entre _virtual threads_ e _platform threads_ com evidência experimental, fornecendo base para identificar e discutir arranjos híbridos observáveis em repositórios.
4. O quarto trabalho mais relacionado é Identification of Java Lock Contention Anti-Patterns Based on Runtime Performance Data (Chirila & Sora), publicado em 2024, porque relaciona contenção de _locks_ e desempenho comparando execução com uma única _thread_, _platform threads_ e _virtual threads_, ajudando a qualificar antipadrões que podem surgir nos projetos minerados.
5. O quinto trabalho mais relacionado é Progressive Server-Side Rendering with Traditional Web Template Engines using Java Virtual Threads (Pereira et al.), publicado em 2025, porque evidencia que _virtual threads_ viabilizam Progressive Server-Side Rendering com _template engines_ bloqueantes mantendo alto _throughput_, reforçando a validade do uso de _virtual threads_ em aplicações web _I/O-bound_, um padrão frequente em projetos WEB.
6. O sexto trabalho mais relacionado é Comparison of Java Virtual and Non-Virtual Threads in Parallel Programming (Sirotic et al.), publicado em 2025, porque demonstra que _virtual threads_ podem ser ligeiramente mais lentas que _platform threads_ em _workloads CPU-bound_, servindo como referência objetiva para identificar e rotular antipadrões de adoção nas bases analisadas.
7. O sétimo trabalho mais relacionado é Mining the Usage of Reactive Programming APIs in Open-Source Projects (Zimmerle et al., 2022), publicado em 2022, porque oferece um método de mineração de repositórios por sinais de API/operadores diretamente adaptável para detectar adoção de paralelismo/concorrência (_virtual threads_, `StructuredTaskScope`, `CompletableFuture` e _stacks_ reativas) em projetos de código aberto.

## Materiais e Métodos

1. O tipo de pesquisa adotado neste trabalho é ...., por que ...
1. Os materiais utilizados neste trabalho são .... [ex.: software, computadores, dados, etc]
1. Os métodos empregados neste trabalho são .... [ex.: método de amostragem, método de análise de correlação, método de agrupamento, etc]
1. As métricas de avaliação são .... [ex.: tempo de resposta, taxa de erros, mutation score, cobertura, latência, etc]
1. As etapa de execução do trabalho são .... [listar as etapa de execução]
