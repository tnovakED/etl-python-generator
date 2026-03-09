# Pipeline de Processamento de Dados de Voos (ETL) ✈️

Este projeto demonstra a construção de um pipeline de ETL (Extract, Transform, Load) utilizando **Python Puro** e o conceito de **Generators (`yield`)**.

## 🚀 Objetivo
Processar dados operacionais de voos de forma eficiente, garantindo baixo consumo de memória RAM, simulando um ambiente de produção onde os arquivos podem ter milhões de linhas.

## 🛠️ Tecnologias e Conceitos
- **Python 3.x**
- **Generators (`yield`)**: Para processamento linha a linha (Lazy Evaluation).
- **CSV & Datetime**: Manipulação de arquivos e padronização de tipos de dados.
- **Arquitetura Medalhão**: Lógica de separação entre dados brutos (Bronze) e tratados (Silver/Gold).

## 📋 Etapas do Pipeline
1. **Extração**: Leitura eficiente do CSV sem carregar o arquivo inteiro na memória.
2. **Transformação**: 
   - Limpeza de strings (Strip e Upper Case).
   - Padronização de datas (múltiplos formatos para DD-MM-YYYY).
   - Tratamento de valores nulos e inconsistentes.
3. **Carga**: Exportação dos dados limpos para um novo arquivo CSV pronto para análise.

---
*Projeto desenvolvido como parte dos estudos para transição de carreira para Engenharia de Dados.*