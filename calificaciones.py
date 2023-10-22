import pandas as pd 
import streamlit as st 

data = pd.read_csv('historico_resultados_pruebas_saber_11.csv')
st.dataframe(data)


'''Se filtra puntaje de matematicas iguales a 50'''

data1 = data[data["puntaje_matematicas"] == 50]
st.dataframe(data1)



''' filtrar establecimiento que contenga la palabra "institucion"'''

data2 = data[data['establecimiento'].str.contains("institucion", case=False)]
st.dataframe(data2)



''' filtro de puntaje naturales mayor o igual a 50 y puntaje sociales mayor o igual a 50'''

data3 = data[(data['puntaje_naturales'] >= 50) & (data['puntaje_sociales'] >= 50)]
st.dataframe(data3)


''' filtro que me muestra la comuna manrique y que la prestacion servicio sea oficial'''

data4 = data[(data['comuna'] == 'manrique') & (data['prestacion_servicio'] == 'oficial') ]
st.dataframe(data4)


''' filtro colegio emaus y el colegio nino jesus '''
palabras_clave = ['col emaus', 'col nino jesus']
data5 = data[data['establecimiento'].isin(palabras_clave)]
st.dataframe(data5)



