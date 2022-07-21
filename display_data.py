
import pymysql
import streamlit as st
import pandas as pd

st.write("Hello! This is a placeholder for the language data app.")

languages = []

conn = pymysql.connect( host='sql11.freemysqlhosting.net',
                        user='sql11507620',
                        password='rysHMx8qHS',
                        db='sql11507620')
cursor = conn.cursor()

cursor.execute("SELECT language from Languages")
languages_list = [i[0] for i in cursor.fetchall()]
cursor.execute("SELECT dif_gm from Languages")
gm_rankings = [i[0] for i in cursor.fetchall()]
cursor.execute("SELECT dif_vc from Languages")
vc_rankings = [i[0] for i in cursor.fetchall()]

st.write(pd.DataFrame({
    'Language'          : languages_list,
    'Grammar rank'      : gm_rankings,
    'Vocabulary rank'   : vc_rankings,
}))

# cursor.execute("SELECT * FROM Languages")
# records = cursor.fetchall()
# for row in records:
#     print(row)
#     # st.write(row)
#     languages.append({
#         'language'  : row[0],
#         'dif_gm'    : row[1],
#         'dif_vc'    : row[2],
#     })
#
# st.write(languages)

cursor.close()
conn.close()
