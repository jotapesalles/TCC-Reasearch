# (2024) Availability and Usage of Platform-Specific APIs: A First Empirical Study
Ricardo Job and Andre Hora. 2024. Availability and Usage of Platform-Specific APIs: A First Empirical Study. In 21st International Conference on Mining Software Repositories (MSR ’24), April 15–16, 2024, Lisbon, Portugal. ACM, New York, NY, USA, 5 pages. 

## 1. Fichamento de Conteúdo

O artigo apresenta o primeiro estudo empírico focado em APIs específicas de plataforma, que são interfaces de programação implementadas para um sistema particular (como Windows ou Unix) e que podem não funcionar em outros. O problema abordado é a falta de conhecimento sobre a real disponibilidade e o impacto do uso dessas APIs, especialmente em um contexto onde sistemas de software são frequentemente testados em múltiplas plataformas. Para investigar isso, os autores analisaram a Biblioteca Padrão do Python, identificando quais APIs possuem restrições de plataforma, e mineraram o uso dessas APIs em 100 projetos populares do GitHub. Os resultados indicam que 21% das APIs da Biblioteca Padrão do Python são específicas de plataforma. Além disso, elas são amplamente utilizadas, com mais de 19 mil usos detectados, divididos quase que igualmente entre código de produção (52,6%) e de teste (47,4%). O estudo conclui discutindo a necessidade de documentação dedicada e de melhores práticas para lidar com essas APIs, já que seu uso incorreto pode quebrar suítes de teste e funcionalidades em determinadas plataformas.

## 2. Fichamento Bibliográfico

* _Platform-Specific API (API Específica de Plataforma)_: conceito central do artigo, definido como uma API implementada para uma plataforma particular (por exemplo, um sistema operacional), o que significa que ela pode não funcionar em outras plataformas. O artigo usa como exemplos a API `os.listvolumes`, disponível apenas para Windows, e a `os.chown`, disponível apenas para Unix.

* _Defensive Code (Código Defensivo)_: prática de programação que os desenvolvedores utilizam para garantir que o uso de uma API específica de plataforma não cause falhas em sistemas que rodam em múltiplas plataformas. O artigo ilustra este conceito com exemplos reais, como o uso de blocos `if` para verificar o sistema operacional antes de chamar a API ou blocos `try-except` para capturar exceções caso a API não esteja disponível no ambiente de execução.

* _API Availability (Disponibilidade de API)_: forma como a documentação oficial indica as restrições de plataforma de uma API. O estudo utiliza as notas de disponibilidade como critério para identificar e classificar uma API como específica de plataforma, sendo este o método principal para a coleta de dados sobre quais APIs analisar.

* _Análise de Uso em Código de Produção vs. Teste_: Trata-se da metodologia empregada para categorizar a localização do uso das APIs específicas de plataforma. O estudo define "código de teste" como qualquer arquivo de código-fonte cujo caminho contenha a substring "test"; caso contrário, é classificado como "código de produção". Essa distinção conceitual é importante para entender em que contextos essas APIs são mais utilizadas.

## 3. Fichamento de Citações

* _"A platform-specific API is an API implemented for a particular platform (e.g., operating system), therefore, it may not work on other platforms than the target one."_

* _"In this context, platform-specific APIs are problematic because they may break test suites on a certain platform if not properly used."_

* _"We find that 21% of the Python Standard Library APIs are platform-specific and that 15% of the modules contain at least one."_

* _"Platform-specific APIs are largely used in Python. We find 19,288 usages of 683 platform-specific APIs in all 100 projects, in both production (52.6%) and test code (47.4%)."_

* _"Despite platform-specific APIs being widespread in the Python Standard Library, there is no documentation dedicated to their availability."_

* _"Given that platform-specific APIs are largely used by Python systems, developers would benefit from best practices to use them, both in test or production code."_
