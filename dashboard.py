import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px


all_df = pd.read_csv('PRSA_Data_Aotizhongxin_20130301-20170228.csv')
nama = 'Mindhalig'
dataset = 'PRSA_Data_Aotizhongxin_20130301-20170228.csv'
subheader1 = 'Arah angin'
subheader2 = 'O3'

st.title('Belajar Analisis Data')
st.header(f'{nama} :smile:')

st.subheader(subheader1)
selected_column = 'wd'
top_values = all_df[selected_column].value_counts().head(5)
st.write(f"Lima arah angin dominan yang sering terjadi di Kolom '{selected_column}' dalam dataset '{dataset}':")
fig = px.bar(top_values, x=top_values.index, y=top_values.values, labels={selected_column: 'Nilai', 'index': 'Frekuensi'})
st.plotly_chart(fig)
with st.expander('Keterangan'):
    st.write(top_values)

st.subheader(subheader2)
st.write(f"Pengaruh faktor cuaca seperti kecepatan angin, kelembaban, atau tekanan udara terhadap tingkat  {subheader2}=")

column1 = 'O3'
column2 = 'TEMP'
column3 = 'PRES'

st.write(f"1. Korelasi antara {column1} dan {column2}")

plt.figure(figsize=(10, 6))
plt.scatter(all_df['O3'], all_df['TEMP'])
plt.xlabel(column1)
plt.ylabel(column2)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
with st.expander('Keterangan'):
    st.write(f"Tingkat ozon cenderung lebih tinggi pada hari-hari yang lebih panas")


st.write(f"2. Korelasi antara {column1} dan {column2}")
plt.figure(figsize=(10, 6))
plt.scatter(all_df['O3'], all_df['PRES'])
plt.xlabel(column1)
plt.ylabel(column2)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
with st.expander('Keterangan'):
    st.write(f"Tingkat ozon cenderung menurun pada saat tekanan udara meningkat, dan jika tekanan udara menurun tingkat ozon cenderung meningkat")



st.caption('Copyright (c) 2023')
