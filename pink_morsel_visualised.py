import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

DATA_PATH = "./formatted_data.csv"

df = pd.read_csv(DATA_PATH)
df = df.sort_values("date")

# cutoff date
CUTOFF_DATE = "2021-01-15"

app = Dash(__name__)

app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "background": "linear-gradient(135deg, #f7f7fb, #eef2ff)",
        "minHeight": "100vh",
        "padding": "60px"
    },
    children=[

        # Header
        html.Div(
            style={"textAlign": "center", "marginBottom": "30px"},
            children=[
                html.H1("Pink Morsel Sales Dashboard",
                        style={"color": "#2c3e50", "fontSize": "44px"}),
                html.P("Filter sales by time and region",
                       style={"color": "#6c7a89", "fontSize": "18px"})
            ]
        ),

        # FILTERS ROW (Time + Region)
        html.Div(
            style={"textAlign": "center", "marginBottom": "30px"},
            children=[

                # Time filter
                html.Div(
                    children=[
                        html.H4("Time Filter"),
                        dcc.RadioItems(
                            id="time-filter",
                            options=[
                                {"label": "All Data", "value": "all"},
                                {"label": "Before Price Increase", "value": "before"},
                                {"label": "After Price Increase", "value": "after"}
                            ],
                            value="all",
                            inline=True
                        )
                    ],
                    style={"marginBottom": "20px"}
                ),

                # Region filter (NEW)
                html.Div(
                    children=[
                        html.H4("Region Filter"),
                        dcc.RadioItems(
                            id="region-filter",
                            options=[
                                {"label": "All", "value": "all"},
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"},
                            ],
                            value="all",
                            inline=True
                        )
                    ]
                )
            ]
        ),

        # Graph container
        html.Div(
            style={
                "maxWidth": "1200px",
                "margin": "0 auto",
                "backgroundColor": "white",
                "borderRadius": "18px",
                "padding": "35px",
                "boxShadow": "0 12px 35px rgba(0,0,0,0.10)"
            },
            children=[
                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)


# CALLBACK (NOW WITH 2 FILTERS)
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("time-filter", "value"),
    Input("region-filter", "value")
)
def update_chart(time_filter, region_filter):

    filtered_df = df.copy()

    # ---- time filter ----
    if time_filter == "before":
        filtered_df = filtered_df[filtered_df["date"] < CUTOFF_DATE]
    elif time_filter == "after":
        filtered_df = filtered_df[filtered_df["date"] >= CUTOFF_DATE]

    # ---- region filter (NEW) ----
    if region_filter != "all":
        filtered_df = filtered_df[filtered_df["region"] == region_filter]

    # create chart
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region" if region_filter == "all" else None,
        title="Pink Morsel Sales Over Time",
        markers=True
    )

    fig.update_layout(template="plotly_white")

    return fig


if __name__ == "__main__":
    app.run()