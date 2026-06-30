# Zetta Finance Analytics | Dashboard em Nuvem

Uma aplicação Web interativa desenvolvida em Python para análise de fluxo de caixa e inteligência financeira. Construído para transformar dados brutos de planilhas de back-office em painéis visuais de fácil interpretação para a tomada de decisão gerencial.

---

## Visão Executiva
No ambiente corporativo, analisar o fluxo de caixa através de planilhas estáticas atrasa a tomada de decisão. Este projeto resolve esse gargalo automatizando a ingestão de dados financeiros (`.csv` e `.xlsx`) e renderizando KPIs (Indicadores-Chave de Desempenho) e gráficos dinâmicos em tempo real, sem necessidade de recarregar a página.

Uma ponte direta entre a Engenharia de Dados e as Ciências Contábeis.

## 🔗 Acesso ao Sistema Ao Vivo
O projeto está em produção (Deploy) e pode ser testado diretamente no navegador através do Streamlit Community Cloud:
 **[Acessar Dashboard Zetta Finance Analytics](https://dashboard-financeiro-em-nuvem-hauajzlbo5ubpampu8kmmu.streamlit.app/)**

---

## 🛠️ Stack Tecnológico
* **Linguagem:** Python 3
* **Framework Web:** `Streamlit` (Criação da interface e reatividade)
* **Engenharia de Dados:** `pandas` e `numpy` (Tratamento, cálculos de KPIs e manipulação de DataFrames)
* **Processamento de Arquivos:** `openpyxl` (Leitura nativa de Excel)

## ⚙️ Funcionalidades Principais
1. **Upload Dinâmico de Dados:** O usuário pode arrastar relatórios de faturamento do ERP direto para o sistema.
2. **Cálculo de KPIs em Tempo Real:** Processamento instantâneo de Faturamento Bruto, Despesas Operacionais e Lucro Líquido.
3. **Visualização Gráfica:** Renderização de gráficos de linha (`st.line_chart`) detalhando a evolução diária de caixa.
4. **Data Generation:** Motor interno que gera dados financeiros fictícios automaticamente caso nenhum arquivo seja carregado (Ideal para apresentações e portfólio).
5. **Auditoria de Dados:** Tabela interativa renderizada no rodapé para conferência linha a linha.

---

## 💻 Como Rodar o Projeto Localmente

### Pré-requisitos

Certifique-se de ter o Python instalado e instale as dependências:
```bash
pip install -r requirements.txt
Certifique-se de ter o Python instalado e instale as dependências:
```bash
pip install -r requirements.txt
