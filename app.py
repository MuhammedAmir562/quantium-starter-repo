from dash import dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

#load final filtered csv file
data = pd.read_csv('processed_sales.csv')
#sort value by date
data = data.sort_values(by='date')

COLORS = {
    "primary": "#FEDBFF",
    "secondary": "#D598EB",
    "font": "#522A61"
}

#make dash app
app = dash.Dash(__name__)

#layout of app
app.layout = html.Div(children=[
    html.H1(children='Soul Foods: Pink Morsel sales data'),
    html.H4("Filter by Region"),
    dcc.RadioItems(
        id='region',
        options=[
            {'label': 'All Regions', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},

        ],
        value='all'
    ),

    dcc.Graph(id='sales-graph'),
])



#setup button function
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region', 'value')
)

def filter_chart(selected_region):
    if selected_region == 'all':
        filtered_data = data
    else:
        filtered_data = data[data['region'].str.lower() == selected_region]


    daily_sales = filtered_data.groupby('date')['sales'].sum().reset_index()
    daily_sales = daily_sales.sort_values(by='date')

    fig = px.line(daily_sales, x='date', y='sales', title='Pink Morsel Sales Data')
    fig.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)