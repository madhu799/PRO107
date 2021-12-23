import pandas as pd
import csv
import plotly.express as pe

df = pd.read_csv('data.csv')
print(df.groupby('level')['attempt'].mean())
fig = pe.scatter(df ,x = 'student_id' ,y = 'level', size='attempt',color='attempt' )
fig.show()
