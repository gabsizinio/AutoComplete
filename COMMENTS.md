# Comentários sobre o projeto Autocomplete

## Obtenção dos Dados

Os dados foram obtidos usando um algoritmo de web scraping (utilizando, sobretudo, as bibliotecas BeautifulSoup e requests) em uma página de glossário jurídico do Conselho Nacional do Ministério Público (foram testadas outras fontes, como o glossário jurídico do Supremo Tribunal Federal, mas esbarrei em problemas com Captcha). A opção pelo uso de web scraping, ao invés de inserir os dados manualmente ou usar alguma LLM para gerar as palavras, foi feita porque dessa forma era possível pegar uma grande quantidade de dados de uma fonte extramamente confiável e respaldada, e de maneira automática, sem precisar fazer esse trabalho manualmente. Os códigos de obtenção dos dados estão em **backend/Scraper**;


## Back-end

O backend foi feito usando FastAPI pois ela oferece alta performance, facilidade de desenvolvimento, suporte ao uso de tipagem estática e integração simples com GraphQL via bibliotecas como Ariadne. Os dados foram armazenados em uma Trie, pois ela permite buscas de prefixo de forma extremamente rápida e eficiente, além de facilitar o processo de execução do projeto por terceiros, pois a Trie é construída em tempo de inicialização, eliminando a necessidade de configuração de um banco de dados externo, deixando o código mais enxuto e facilitando a distruibuição. Inicialmente, tinha montado todo o projeto usando Postgresql, o resultado não foi negativo, mas percebi que usar Trie simplificaria vários pontos, e ainda ganharia em eficiência e velocidade.

A trie também foi "separada" do código principal, havendo um módulo próprio pra ela para que facilitasse testes, manutenção, alterações, e para que as responsabilidades de cada componenete do sistema ficassem bem definidas (princípio esse que também se aplica a separação de código principal e resolvers da API).


## Front-end

O frontend foi desenvolvido utilizando React (como pede a descrição do desafio). A aplicação faz uso de componentização, o que facilita a manutenção, a reutilização de código e a escalabilidade do projeto. A responsividade também foi algo bastante priorizado. Optei pelo uso de CSS puro, pois é um projeto de interface simples com o principal foco estando no back-end, sendo ele mais que o suficiente para implementá-la.


## Possíveis melhorias

- Uso de Fuzzy Search: O uso de Fuzzy Search integrado com o uso de Trie permitiria que o autocomplete retornasse resultados mesmo quando o usuário comete pequenos erros de digitação, o que tornaria a aplicação mais robusta e tolerante a falhas humanas (melhorando a experiência do usuário);
- Ranking de Relevância: Atualmente os resultados são retornados na ordem em que forma inseridos, poderia ser criado um ranking de relevância com base em frequência de uso, popularidade do termo ou algum outro critério;
- Expansão das sugestões: Mais páginas ou glossários jurídicos podem ser adicionados no web-scraping de obtenção dos dados;