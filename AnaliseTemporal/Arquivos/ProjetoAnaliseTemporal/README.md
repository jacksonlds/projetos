# Análise Temporal do Uso da Internet no Brasil

## Descrição
Este projeto tem como objetivo realizar uma **análise temporal do uso da internet no Brasil**, utilizando técnicas de manipulação e análise de dados em **Python** (com as bibliotecas **Pandas** e **NumPy**) integradas a um **banco de dados relacional via SQL**. 

A análise é baseada em dados públicos sobre o uso da internet entre os anos de 2000 e 2023, fornecidos pelo [Kaggle](https://www.kaggle.com).

O projeto foi desenvolvido no ambiente **Jupyter Notebook**, aplicando conceitos de Banco de Dados, SQL, Python e Análise de Dados.

---

## Objetivos do Projeto
- Aplicar, de forma prática, conceitos de:
  - Banco de Dados Relacional
  - SQL (consultas e análises)
  - Manipulação e análise de dados com **Python**, **Pandas** e **NumPy**
- Realizar uma análise temporal do uso da internet no Brasil, abrangendo:
  -  Crescimento absoluto
  -  Crescimento atual
  -  Média de crescimento anual
  -  Pico de crescimento anual
  -  Ranking do Brasil no primeiro e no último ano da série histórica
  -  Cálculo da média aritmética do período

---

## Dataset
- **Fonte:** [Global Internet Usage by Country (2000-2023) - Kaggle](https://www.kaggle.com/datasets/meleknur/global-internet-usage-by-country-2000-2023)
- **Descrição:** Dados sobre a porcentagem da população com acesso à internet em diversos países no período de 2000 a 2023.

---

## Tecnologias Utilizadas
- **Python** (Jupyter Notebook)
- **Pandas** e **NumPy** para análise e manipulação de dados
- **SQL** via **SQLite** para consultas e armazenamento local
- **IPython-SQL** para integração de SQL com Jupyter Notebook

---

## Análises Realizadas
- Evolução temporal do uso da internet no Brasil
- Crescimento absoluto e crescimento atual
- Cálculo da média de crescimento anual
- Identificação do pico de crescimento anual
- Ranking do Brasil no início e no final da série histórica
- Cálculo da média aritmética do uso no período analisado

---

## Status do Projeto
 **Projeto finalizado.**

---

## Como Executar este Projeto

### Pré-requisitos:
- [Python 3.9 ou superior](https://www.python.org/)
- [Jupyter Notebook](https://jupyter.org/)
- [Git](https://git-scm.com/) (opcional, para clonar o repositório)

### Instalação das dependências:
Recomenda-se criar um ambiente virtual (opcional, mas boa prática):

```bash
python -m venv venv
```
### Ativar o ambiente virtual:
- No Windows:
```
venv\Scripts\activate
```
- No macOS/Linux:
```
source venv/bin/activate
```
### Instalar as dependências:
```
pip install -r requirements.txt
```
### Ou, se preferir, instalar manualmente:
```
pip install pandas numpy sqlalchemy ipython-sql jupyterlab
```
## Clonar o Repositório (opcional)
### Se desejar, clone o repositório diretamente do GitHub:
```
git clone https://github.com/jacksonlds/projetos.git
cd AnáliseTemporal/Arquivos/ProjetoAnaliseTemporal
```
## Executar o Notebook
### No terminal, rode:
```
jupyter notebook
```
- Isso abrirá o Jupyter no seu navegador.
- Abra o arquivo **Projeto.ipynb**.
- Execute as células (Shift + Enter) uma a uma para rodar todo o código.

## Estrutura do Projeto
```
ProjetoAnaliseTemporal/
├── anaconda_projects/         # (Ignorar) Pasta criada automaticamente pelo Anaconda, não precisa estar no repositório
│   └── project_filebrowser.db
├── database/                  # Bancos de dados utilizados no projeto (SQLite, por exemplo)
│   └── dbprojeto1.db
├── dataset/                   # Arquivos de dados brutos ou tratados (CSV, Excel, JSON, etc.)
│   └── internet_usage.csv
├── imagens/                   # Imagens utilizadas no README ou no notebook (ex.: gráficos, diagramas, capa do projeto)
│   └── projeto.jpg
├── LICENSE                    # Licença do projeto (MIT)
├── Projeto.ipynb              # Notebook com código, análise e resultados
├── README.md                  # Documentação do projeto (descrição, instruções, etc.)
├── requirements.txt           # Dependências necessárias para rodar o projeto
```

## Funcionalidades

- [x] Leitura e limpeza dos dados.
- [x] Criação e utilização de banco de dados relacional (SQLite).
- [x] Consultas SQL diretamente no Jupyter Notebook.
- [x] Análise temporal do uso da internet no Brasil.
- [x] Cálculo de crescimento absoluto, crescimento atual e crescimento médio anual.
- [x] Identificação do pico de crescimento anual.
- [x] Geração de ranking do Brasil no início e no final da série histórica.
- [x] Cálculo da média aritmética do uso da internet no período.
- [x] Integração entre Python (Pandas, NumPy) e SQL no ambiente Jupyter Notebook.

---

## Principais Insights

- O uso da internet no Brasil apresentou um crescimento significativo entre 2000 e 2023.
- A porcentagem da população brasileira com acesso à internet saltou de aproximadamente **2.9% em 2000** para cerca de **84% em 2023**.
- O ano com maior crescimento percentual foi **2018**, com um aumento de **7,43%** em relação ao ano anterior.
- No ranking global de uso da internet:
- Em **2000**, o Brasil ocupava a posição **76ª **.
- Em **2023**, o Brasil alcançou a posição **59ª**, refletindo um avanço expressivo.
- A média de crescimento anual do uso da internet no Brasil no período analisado foi de aproximadamente **2,93**.
- Houve uma desaceleração natural nos últimos anos, indicando que o país se aproxima de uma saturação no acesso, dado que a maior parte da população já está conectada.

---

## Melhorias Futuras

- [ ] Adicionar visualizações interativas utilizando Plotly ou Power BI.
- [ ] Automatizar o processo de atualização dos dados caso haja novas versões no Kaggle.
- [ ] Expandir a análise para comparar o Brasil com outros países da América Latina ou do mundo.
- [ ] Implementar testes de integridade nos dados antes da análise.
- [ ] Criar um dashboard web com Streamlit para apresentar os resultados de forma interativa.
- [ ] Adicionar análises preditivas utilizando modelos de Machine Learning para estimar o crescimento futuro do uso da internet.
- [ ] Melhorar a organização do código, separando funções em scripts Python externos.
- [ ] Disponibilizar uma API simples que permita consultar os dados processados.

---

## Dependências

- [Python](https://www.python.org/) 3.9 ou superior
- [pandas](https://pandas.pydata.org/) — Manipulação e análise de dados
- [numpy](https://numpy.org/) — Operações numéricas
- [ipython-sql](https://github.com/catherinedevlin/ipython-sql) — Executar SQL dentro de notebooks Jupyter
- [sqlalchemy](https://www.sqlalchemy.org/) — Conector para banco de dados SQLite
- [jupyter](https://jupyter.org/) — Ambiente para execução dos notebooks

---

### Instalação das dependências

Você pode instalar manualmente:

```bash
pip install pandas numpy ipython-sql sqlalchemy jupyter
```
### Ou usar o arquivo **requeriments.txt**:
```
pip install -r requirements.txt
```

---

## Autor

Desenvolvido por **Jackson Lopes**.

- 🔗 [LinkedIn](https://www.linkedin.com/in/jacksonls/)
- 🔗 [GitHub](https://github.com/jacksonlds)
- 🔗 [Portfólio](https://jacksonlds.github.io/portfolio/)

---

## Licença

Este projeto está sob a licença **MIT** — consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.
