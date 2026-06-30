import streamlit as st
import pandas as pd
import numpy as np

# 1. CONFIGURAÇÃO DA PÁGINA WEB
st.set_page_config(page_title="Zetta Finance Analytics", page_icon="📊", layout="wide")

st.title("📊 Painel de Inteligência Financeira")
st.write("Faça o upload de uma planilha de fluxo de caixa para análise instantânea ou visualize a simulação padrão.")

# 2. FUNÇÃO PARA GERAR DADOS FALSOS (Caso não haja upload)
def carregar_dados_teste():
    # Gerando 30 dias de movimentação contábil
    datas = pd.date_range(start="2026-06-01", end="2026-06-30")
    receitas = np.random.randint(2000, 8000, size=len(datas))
    despesas = np.random.randint(1000, 5000, size=len(datas))
    
    df = pd.DataFrame({'Data': datas, 'Receitas': receitas, 'Despesas': despesas})
    df['Lucro Líquido'] = df['Receitas'] - df['Despesas']
    return df

# 3. ÁREA DE UPLOAD (Interatividade com o usuário)
arquivo = st.file_uploader("Arraste seu arquivo Excel ou CSV aqui", type=["csv", "xlsx"])

if arquivo is not None:
    try:
        if arquivo.name.endswith('.csv'):
            # Tenta ler no padrão internacional primeiro
            try:
                df = pd.read_csv(arquivo)
            except UnicodeDecodeError:
                # Se der erro de acentuação, volta o cursor do arquivo para o início...
                arquivo.seek(0)
                # ...e tenta ler no formato padrão do Excel Brasileiro (latin1 e separado por ;)
                df = pd.read_csv(arquivo, encoding='latin1', sep=';')
        else:
            df = pd.read_excel(arquivo)
        st.success("Planilha processada com sucesso!")
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
        df = carregar_dados_teste()
else:
    st.info("Nenhum arquivo detectado. Carregando cenário de demonstração...")
    df = carregar_dados_teste()

# 4. OS CARDS DE KPI (Indicadores Chave de Desempenho)
st.markdown("---")
st.subheader("📈 Resumo Executivo")

# Criando 3 colunas na tela
col1, col2, col3 = st.columns(3)

total_receitas = df['Receitas'].sum()
total_despesas = df['Despesas'].sum()
lucro_total = df['Lucro Líquido'].sum()

# Mostrando os números grandes
col1.metric("Faturamento Bruto", f"R$ {total_receitas:,.2f}")
col2.metric("Despesas Operacionais", f"R$ {total_despesas:,.2f}")
col3.metric("Lucro Líquido (Caixa Livre)", f"R$ {lucro_total:,.2f}", delta=f"R$ {lucro_total:,.2f}")

# 5. OS GRÁFICOS VISUAIS
st.markdown("---")
st.subheader("📊 Evolução Diária de Caixa")
# O Streamlit cria gráficos interativos lendo direto do Pandas
st.line_chart(df.set_index('Data')[['Receitas', 'Despesas']])

# 6. A TABELA BRUTA DE AUDITORIA
st.markdown("---")
st.subheader("📋 Tabela de Dados (Auditoria)")
# Exibe a tabela interativa onde o usuário pode ordenar as colunas
st.dataframe(df, use_container_width=True)

# Rodapé profissional
st.markdown("---")
st.caption("Desenvolvido por Marcelo | Zetta IA e TI | Foco em Automação Contábil")