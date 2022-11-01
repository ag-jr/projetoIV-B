import pandas as pd
import plotly.express as px
import streamlit as st 


#leitura do database
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#renomear colunas
df = df.rename(columns={'newDeaths': 'Novos óbitos','newCases': 'Novos casos','deaths_per_100k_inhabitants': 'Óbitos/100k Habitantes','totalCases_per_100k_inhabitants':'Casos/100k Habitantes', 'vaccinated':'Vacinados', 'vaccinated_per_100_inhabitants':'Vacinados/100k Habitantes'})

#SELECÃO DO ESTADO
estados = list(df['state'].unique())
titulo = st.sidebar.subheader('Selecione os filtros através das opções abaixo.')
state = st.sidebar.selectbox('Qual estado?', estados)

#SELEÇÃO DA COLUNA
colunas = ['Novos óbitos','Novos casos','Óbitos/100k Habitantes','Casos/100k Habitantes', 'Vacinados', 'Vacinados/100k Habitantes']
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)

#SELEÇÃO DAS LINHAS QUE PERTECEM AO ESTADO 
df = df[df['state'] == state]

fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

st.header('Análise e Desenvolvimento de Sistemas - Universidade de Caxias do Sul')
st.subheader('Dados da Covid no Brasil')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.')


st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
st.caption('Projeto desenvolvido para o Projeto Integrador IV-A. Grupo 7')

