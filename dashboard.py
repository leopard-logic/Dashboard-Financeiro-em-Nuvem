# ==============================================================================
# ZETTA FINANCE ANALYTICS - DASHBOARD CORPORATIVO
# Desenvolvedor: Marcelo (Zetta IA e TI)
# Portfólio: https://github.com/leopard-logic
# Foco: Engenharia de Dados e Automação Contábil
# ==============================================================================

import streamlit as st
import pandas as pd
import numpy as np

# 1. CONFIGURAÇÃO DA PÁGINA WEB (Minimalista)
st.set_page_config(page_title="Zetta Finance Analytics", layout="wide")

# CSS Customizado para um visual mais limpo e profissional
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; padding-bottom: 0rem; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("Zetta Finance Analytics")
st.markdown("Módulo de inteligência financeira e análise de fluxo de caixa corporativo.")
st.markdown("---")

# 2. FUNÇÃO PARA GERAR DADOS DE DEMONSTRAÇÃO
def carregar_dados_teste():
    datas = pd.date_range(start="2026-06-01", end="2026-06-30")
    receitas = np.random.randint(2000, 8000, size=len(datas))
    despesas = np.random.randint(1000, 5000, size=len(datas))
    
    df = pd.DataFrame({'Data': datas, 'Receitas': receitas, 'Despesas': despesas})
    df['Lucro Líquido'] = df['Receitas'] - df['Despesas']
    return df

# 3. MOTOR DE INGESTÃO DE DADOS (Com suporte ao padrão brasileiro)
arquivo = st.file_uploader("Importar base de dados (CSV ou Excel)", type=["csv", "xlsx"])

if arquivo is not None:
    try:
        if arquivo.name.endswith('.csv'):
            try:
                df = pd.read_csv(arquivo)
            except UnicodeDecodeError:
                arquivo.seek(0)
                df = pd.read_csv(arquivo, encoding='latin1', sep=';')
        else:
            df = pd.read_excel(arquivo)
        st.success("Dados processados e validados.")
    except Exception as e:
        st.error(f"Falha na leitura do arquivo: {e}")
        df = carregar_dados_teste()
else:
    df = carregar_dados_teste()

# 4. INDICADORES CHAVE DE DESEMPENHO (KPIs)
st.subheader("Resumo Executivo")
col1, col2, col3 = st.columns(3)

total_receitas = df['Receitas'].sum()
total_despesas = df['Despesas'].sum()
lucro_total = df['Lucro Líquido'].sum()

col1.metric("Faturamento Bruto", f"R$ {total_receitas:,.2f}")
col2.metric("Despesas Operacionais", f"R$ {total_despesas:,.2f}")
col3.metric("Lucro Líquido", f"R$ {lucro_total:,.2f}", delta=f"R$ {lucro_total:,.2f}")

# 5. VISUALIZAÇÃO GRÁFICA
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Evolução Diária de Caixa")
st.line_chart(df.set_index('Data')[['Receitas', 'Despesas']])

# 6. TABELA DE AUDITORIA
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("Dados Consolidados")
st.dataframe(df, use_container_width=True)

# 7. ASSINATURA DO DESENVOLVEDOR (Visível no site)
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #888888; font-size: 0.9em;'>
        Desenvolvido por <b>Marcelo | Zetta IA e TI</b><br>
        <a href='https://github.com/leopard-logic' target='_blank' style='color: #888888; text-decoration: none;'>github.com/leopard-logic</a>
    </div>
    """, 
    unsafe_allow_html=True
)