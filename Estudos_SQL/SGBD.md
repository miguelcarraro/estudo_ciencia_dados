# SGBD.

## Apresentação Inicial.

### Contextualização.

**Dados != Informação**

"Tudo" são dados, qualquer coisa que existe no mundo são dados.   
Dados são como um diamante bruto, já a informação são os dados após serem trabalhados e limpos para uma melhor visualização.

Antigamente os dados eram fixados como texto e números, porém, em valores de KBytes, quantidades infimas de dados coletados, armazenados em cartões e disquetes, hoje a quantidade de dados são armazenados em até PetaBytes.
Coletamos dados de redes sociais, bancos, streamings, etc...

Existe o "Novo" paradigma do BigData, os 3 V's:
'''
    Velocidade.
    Variedade.
    Volume.
'''

Cada um desses temas tem dificuldades grandes de serem trabalhadas e para isso surgiram técnologias para trabalhar esse paradigma.

Técnologias noSQL como:
'''
    mongoDB. (Orientado a documentos.)
    cassandra. (Orientado a Colunas.)
    neo4j. (Baseado em Grafos.)
'''
E para trabalhar bem com isso existe a Nuvem como a Azure e AWS, que facilitam a utilização de dados de grande escala.

### O Que são Banco de Dados?

#### O que são Dados?

**Definição geral:**
__Podemos considerar uma coleção de palavras, que dentre elas há relacionamentos entredados, constituindo então um banco de dados.__

Podem ser considerado como um fato, são o diamante bruto relacionado ao acontecimento, e ele precisa ser lapidado para ser tranformado em informação.

Para armazenar essa informação bruta foram criados os Bancos de Dados, os bancos de dados são um conjunto de dados.

Já dentro de um SGBD (Sistema de Gerenciamento de Banco de Dados)
É necessário que exista um contexto - Representação do mundo real.
Coerência.
Propósito.

### O que são SGBDs?
'''
    Definição:

        É um software de propósito geral.
        É uma etapa mais conceitual, onde vamos definir o tipo de dado, a estrutura e quais regras/diretrizes que estão relacionadas ao meu contexto.
        Onde criamos o nosos "Mini Mundo", o que quero representar no meu SGBD.

    Contrução:

        É a etapa de inserção dos dados, a persistência através de uma determinada estrutura.
        A parte de mapeamento, onde tiramos informações de requisitos entende-se o que elas são criamos uma estrutura.
        A partir dessa estrutura conseguimos criar comandos para persistir as informações dentro do SGBD.

    Manipulação:

        Aqui o SGBD já está funcinando
        Estamos na etapa de mexer e acessar essas informações, criar relatórios, etc...
        Existe determinadas linguagens que vão gerenciar o meu acesso com base em quarys que serão compiladas em linguagem de maquina.

    Compartilhamento:

        Em algum momento teremos diversos grupos acessando os dados com acesso simultâneo, criando regras para que cada grupo acesse de uma determinada forma.
'''

Querys são solicitações feitas pelo usuário e o sistema vai retornar os dados com base nessa solicitação feita.

SGBDs tem um ciclo de vida de longo prazo, podem ser usados por muito tempo sem comprometimento da base de dados em si.

São protegidos por dois níveis, um voltado ao mal funcionamento e o outro de acesso:
'''
    Em relação ao mal funcionamento pode-se usar réplicas e determinar ações para contornar erros. Utilizar o log para retornar o banco ao estado em que era persistente.

    Na parte de acesso posso restringir o acesso de determinados grupos a determinadas informações.
'''

### Histórico de SGBDs.

A idéia de criação de um gerenciamento de banco de dados surgiu em 1960.
Já o modelo relacional surgiu em 1970 pela IBM.

Surgiu essa vontade para diminuir custos com pessoal e evitar erros, pois era necessário desprender pessoas para gerenciar os dados e com isso existe a possibilidade de erros ocorregem já que pessoas podem se cansar obviamente.

Para conseguir gerenciar dados é necessário uma estrutura, no meio tempo antes da criação do modelo relacional foram utilizados dois modelos, o modelo em rede e o modelo hierárquico.

O modelo relacional foi criado por **Edgar Frank "Ted" Codd.** baseado em álgebra relacional.

O primeiro SGBD foi criado pela Honeywell em 1976 e não era relacional.
Em 1980 a Oracle lançou o Oracle 2 já era relacional.
Em 1983 IBM lançou o IBM SQL/DS também relacional.
Também em 83 a Oracle lançou o Oracle 3.

A partir dos anos 2000, com a entrada gigantesta de dados começou-se ser necessário um armazenamento mais robusto que nem sempre comportava o modelo relacional e ai nasceram os bancos **NoSQL**

#### Modelo Hierárquico.

É um sistema de gerenciamento voltado para a informação
Lembra um modelo de registo em arvore, onde temos um nó pai, nós filhos e folhas

Caso eu queira acessar uma informação especifica tenho que correr por todos os nós até localizar a informação, o que gerava custo computacional maior.

#### Modelo em Rede.

É um modelo mais complexo que utiliza links como se fosse um grafo, o principal problema é que a pessoa que utiliza ele precisa saber da estrutura do grafo para que você saiba qual é a origem da ligação "N:M"

#### Modelo Relacional.

Baseado em Álgebra relacional

O modelo relacional normalmente tem um DBA que é o administrador do banco de dados
O DBA vai definir as tabelas e constrains para os dados e os comandos usados por ele sao traduzidos pelo processador LDD ( Linguagem de Definição de Dados.)

Como o LDD vai ser entendido pelo banco de dados:
'''
    É necessária que seja feita uma tradução das querys SQL para linguagem de máquina
    Após esse processo vira um gerenciador que ira tratar a demanda e direcionar corretamente a extração daqueles dados, acessando os metadados para conhecer a estrutura e retornar a informação.
'''

Para o uso do modelo relacional também existe o usuário comum vai usar uma linguagem diferente para se comunicar com o banco de dados, ele usará uma LMD  (Linguagem de Definição de Dados)
Aqui a intenção principal é a de alterar e extrair informações, e essas informações normalmente são duráveis.

### SGBDs mais utilizados no mercado.

1- Oracle
    O pioneiro, projetado para fornecer performance, para trabalhar em grid muito usado por grandes corporações.

2- MySQL
    Também mantido pela Oracle, um SGBD leve e Open Source, muito versátil.

3- SQLServer
    Mantido pela Microsoft, um pouco mais sofisticado, com ferramentas de integração com BI.

4- PostgreSQL
    Considerado um exemplo em especificação, normalmente é um banco muito utilizado em conjunto com por exemplo python, também é open source.

5- mongoDB.
    Um SGBD NoSQL, orientado a documentos, armazena dados em bloco.

