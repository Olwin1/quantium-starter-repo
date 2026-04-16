import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

DATA_PATH = "./formatted_data.csv"

# load + sort data
df = pd.read_csv(DATA_PATH)
df = df.sort_values("date")

# create figure
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

app = Dash(__name__)

app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "backgroundColor": "#f7f7fb",
        "padding": "30px"
    },
    children=[

        html.Div(
            children=[
                html.H1(
                    "Pink Morsel Sales Visualiser",
                    style={
                        "textAlign": "center",
                        "color": "#2c3e50",
                        "marginBottom": "10px"
                    }
                ),

            ]
        ),

        # chart container (card-style feel)
        html.Div(
            children=[
                dcc.Graph(
                    id="sales-line-chart",
                    figure=fig
                )
            ],
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0 2px 10px rgba(0,0,0,0.1)"
            }
        )
    ]
)

if __name__ == "__main__":
    app.run()