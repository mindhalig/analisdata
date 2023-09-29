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
with st.expander('Lihat'):
    st.write(top_values)

st.subheader(subheader2)
st.write(f"Pengaruh faktor cuaca seperti kecepatan angin, kelembaban, atau tekanan udara terhadap tingkat  {subheader2}")
correlation_matrix = all_df[['O3', 'RAIN', 'TEMP', 'PRES', 'DEWP']].corr()
st.write(f"Heatmap korelasi antara variabel cuaca dan tingkat {subheader2} dalam dataset '{dataset}':")
fig, ax = plt.subplots()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.caption('Copyright (c) 2023')