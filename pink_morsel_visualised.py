import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

FILE_PATH = "./formatted_data.csv"

# load and prepare data
df = pd.read_csv(FILE_PATH)
df = df.sort_values("date")

# build chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

# create Dash app
app = Dash(__name__)

# layout components
title = html.H1("Pink Morsel Sales Dashboard", id="page-title")

chart = dcc.Graph(
    id="sales-chart",
    figure=fig
)

app.layout = html.Div(children=[
    title,
    chart
])

# run server
if __name__ == "__main__":
    app.run(debug=True)