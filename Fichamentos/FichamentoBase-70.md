# Measuring the Benefits of CI/CD Practices for Database Application Development
Fluri, Jasmin; Fornari, Fabrizio; Pustulka, Ela. "Measuring the Benefits of CI/CD Practices for Database Application Development".

## 1. Fichamento de Conteúdo

O artigo aborda a automação de processos de desenvolvimento para aplicações de banco de dados, um campo onde a integração e entrega contínua (CI/CD) são raramente aplicadas, apesar de seus benefícios já conhecidos no desenvolvimento de software em geral. O problema central é que a integração e a implantação de bancos de dados são frequentemente executadas manualmente, o que as torna caras e propensas a erros. Para resolver isso, os autores propõem um pipeline de CI/CD projetado especificamente para o contexto de bancos de dados. A metodologia consistiu na implementação deste pipeline em dois estudos de caso industriais, um em um projeto de _data warehouse_ e outro em um _back-end_ de banco de dados. A avaliação do impacto foi realizada por meio de uma análise quantitativa e qualitativa, comparando medições e entrevistas com as equipes de desenvolvimento antes e depois da automação. Os resultados demonstraram que a adoção do pipeline de CI/CD reduziu significativamente as falhas de implantação, aumentou a estabilidade e o número de implantações executadas. Além disso, as entrevistas revelaram uma redução da carga cognitiva dos desenvolvedores, que passaram a ter mais confiança e agilidade no processo de entrega de software.

## 2. Fichamento Bibliográfico
* _Pipeline Design de CI/CD para Bancos de Dados_: pipeline dividido em três fases principais: Integração (que verifica o código, realiza análise estática, backup, implantação em um banco de dados de CI e executa testes), _Release_ (que define o número da versão e armazena o artefato) e _Deployment_ (que implanta o artefato no banco de dados de destino).
* _Métricas de Desempenho para Avaliação do Pipeline_: conjunto específico de medições para verificar quantitativamente os benefícios da automação. As principais são: _Lead time_ (tempo entre o início da implementação e a produção), número de implantações com falha (um indicador de estabilidade), número de funcionalidades por implantação (reflete o tamanho e o risco de uma implantação), e tempo para restaurar um ambiente (mede a eficácia dos mecanismos de recuperação).
• _Release Coordinator (Coordenador de Release)_: figura central nos fluxos de trabalho manuais, responsável por coletar, empacotar e implantar as alterações de todos os desenvolvedores. Este modelo cria um gargalo e um ponto único de falha. A automação com o pipeline de CI/CD elimina essa dependência, pois capacita todos os desenvolvedores a implantar suas próprias funcionalidades, removendo o coordenador como intermediário.

## 3. Fichamento de Citações

* _"However, when it comes to database applications, the database integration and deployment are often executed manually, making it costly and error-prone."_

* _"From a quantitative perspective, we found that introducing CI/CD pipelines reduces failed deployments, improves stability and increases the number of executed deployments."_

* _"From a qualitative perspective, we interviewed the developers before and after the implementation of the CI/CD pipeline and the results show the CI/CD pipeline brings clear benefits to the development team (i.e., reduced cognitive load)."_ 

* _"The interviews we conducted with developers in both use cases before the pipeline implementation reported that manual deployments involved a high level of context switching because the release coordinator needed to get back to the developers if installations failed, causing them to pause their current work for bug fixes."_ 

* _"A fixed-release cycle defined by the business leads to longer lead times and can be seen as an anti-pattern."_

* _"The ability to deploy features for all developers also removed the release coordinator as a single point of failure and dependency for the teams."_