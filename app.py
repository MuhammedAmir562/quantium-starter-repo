from dash import dash, dcc, html
import plotly.express as px
import pandas as pd

#load final filtered csv file
data = pd.read_csv('processed_sales.csv')

data = data.sort_values(by='date')


#make graph
fig = px.line(data, x='date', y='sales', color='region', title='Pink Morsel Sales Data')

#make dash app
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Pink Morsel sales data'),

    dcc.Graph(figure=fig),
])
if __name__ == '__main__':
    app.run(debug=True)