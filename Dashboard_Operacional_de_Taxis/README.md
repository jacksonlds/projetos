# 🚖 Dashboard Operacional de Táxis - Pipeline de Dados, Orquestração e BI

Este repositório apresenta uma solução completa de engenharia de dados desenvolvida para centralizar, processar, transformar e disponibilizar métricas operacionais de frotas de táxis. A arquitetura foi desenhada seguindo as melhores práticas de mercado, utilizando conteinerização com Docker, orquestração com Apache Airflow e modelagem analítica com o dbt.

---

## 🏗️ Arquitetura da Solução

O projeto é estruturado em componentes modulares independentes, permitindo um desacoplamento limpo entre armazenamento, processamento e transformação:

1. **Camada de Armazenamento e Ingestão (`meu-postgres`)**:
   * Base de dados relacional em **PostgreSQL** rodando em contentor isolado.
   * Responsável por persistir tanto os dados brutos operacionais como as tabelas dimensionais e fatos consolidadas.

2. **Camada de Orquestração (`airflow_docker`)**:
   * Implementação completa do **Apache Airflow** (com Scheduler, Webserver, Triggerer e Worker).
   * Automatiza o ciclo de vida dos dados (ETL/ELT), garantindo reexecuções seguras, tratamento de falhas e monitoramento de dependências.

3. **Camada de Transformação e Modelagem (`projeto_dbt`)**:
   * Utilização do **dbt (data build tool)** para aplicar o padrão *analytics engineering*.
   * Transformações baseadas em SQL modular, documentação automática de linhagem de dados e testes rigorosos de integridade.

4. **Automação e Scripts de Apoio (`Script_Python`)**:
   * Scripts em Python utilitários criados para auxiliar na carga massiva e manipulação de arquivos de dados ou compactações restritas em ambientes de nuvem.

---

## 📂 Estrutura de Diretórios do Repositório

```text
Dashboard_Operacional_de_Taxis/
├── Script_Python/       # Scripts utilitários em Python para ingestão e suporte
├── airflow_docker/      # Configurações do ambiente Docker Compose e DAGs do Airflow
├── meu-postgres/        # Ficheiros de configuração, volumes e Docker Compose do PostgreSQL
├── projeto_dbt/         # Modelos SQL, macros, seeds e projeto dbt configurado
├── Painel.png           # Captura ilustrativa do dashboard final de BI
└── README.md            # Documentação técnica detalhada do projeto

Guia de Execução Local / Cloud (Manual via Docker Compose)Para colocar o ecossistema completo a funcionar em servidores dedicados ou máquinas virtuais (como instâncias Linux na Google Cloud Platform), siga a inicialização modular por componentes:   
