import pandas as pd
import plotly.express as px

file = pd.read_csv("line_chart.csv")
fig = px.line(file,x = "Year",y = "Per capita income",color = "Country",title = "Per Capita Income Country Wise")
fig.show()