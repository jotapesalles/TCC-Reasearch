# Adoção e Uso de Virtual Threads em Projetos Java: Um Estudo Empírico

1. João Paulo de Sales Pimenta

* Danilo Maia
* Leonardo Vilela
* Raphael Ramos
* Cleiton Tavares

## Introdução
1. A área da Engenharia de Software tratada neste trabalho é: “aplicações distribuídas, principalmente por arquiteturas de microsserviços hospedadas em ambientes de computação em nuvem, nas quais a gestão eficiente de CPU e memória é crítica para desempenho e custo operacional”, com foco na concorrência na plataforma Java (_platform threads_ vs. _virtual threads_) e seus impactos de desempenho, complexidade e adoção.
2. O problema que este trabalho busca resolver nessa área é: “não há um panorama empírico consolidado sobre a adoção contemporânea de _virtual threads_ em projetos Java: onde aparecem, com que prevalência em relação a threads de plataforma e quais padrões concretos de uso predominam em diferentes _frameworks_ e domínios.”
3. Resolver este problema é relevante porque: “as _virtual threads_ foram concebidas para promover melhoria de desempenho, eficiência e racionalização de recursos em software, otimizando o uso de CPU e memória em aplicações intensivas em I/O e aumentando a taxa de transferência (_throughput_). Trata-se de uma capacidade estabilizada no JDK~21, sobre a qual ainda há escassez de estudos em cenários realistas, especialmente em aplicações orientadas a banco de dados na nuvem. Em paralelo, há sinais de adoção em _frameworks_ e servidores web populares, como Quarkus, Spring e Jetty. Nesse contexto, compreender benefícios, custos e desafios de integração torna-se essencial para embasar decisões técnicas, mitigar riscos e orientar a construção de sistemas escaláveis e eficientes. Além disso, a estabilização das VTs no JDK~21 cria um período oportuno para observar tendências reais de adoção e consolidar recomendações que orientem decisões de engenharia com foco em automação, eficiência e uso de recursos.”
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

1. O trabalho mais relacionado é ...., publicado no ano ..., por que ....
1. O segundo trabalho mais relacionado é .... , publicado no ano ..., por que ....
1. O terceiro trabalho mais relacionado é ...., publicado no ano ...,  por que ....

## Materiais e Métodos

1. O tipo de pesquisa adotado neste trabalho é ...., por que ...
1. Os materiais utilizados neste trabalho são .... [ex.: software, computadores, dados, etc]
1. Os métodos empregados neste trabalho são .... [ex.: método de amostragem, método de análise de correlação, método de agrupamento, etc]
1. As métricas de avaliação são .... [ex.: tempo de resposta, taxa de erros, mutation score, cobertura, latência, etc]
1. As etapa de execução do trabalho são .... [listar as etapa de execução]
