# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:59:38 2022

@author: Admin
"""
import pandas as pd
import dash  # use Dash version 1.16.0 or higher for this app to work
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
# df = pd.read_csv(r"C:\Users\Admin\Downloads\Untitled spreadsheet - Sheet1 (3).csv")
# df['gen']=list('MMMMMMMFFMFFFFFFFFFFFMMMMFFMMFFMMFFMM')

# df.drop("Unnamed: 2",inplace =True,axis ="columns")
# df.to_csv(r"C:\Users\Admin\Downloads\dummy.csv")
df = pd.read_csv(r"C:\Users\user\Desktop\Plotly\dummy1.csv")
df
df.dropna(inplace= True)
df
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Dropdown(id='dpdn2', value=['Lakshadweep','Haryana'], multi=True,
                  options=[{'label': x, 'value': x} for x in
                          df.State.unique()]),
    html.Div([
        dcc.Graph(id='pie-graph', figure={}),
        dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None)
    ])
])

@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
)
def update_graph(State_chosen):
    dff = df[df.State.isin(State_chosen)]
    fig = px.bar(data_frame=dff, x='State', y='Population', color='State',
                  # custom_data=['country', 'continent', 'lifeExp', 'pop']
                  )

    return fig


# # Dash version 1.16.0 or higher
@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='dpdn2', component_property='value')
)
def update_side_graph(hov_data, State_chosen):
    if hov_data is None:
        dff2 = df[df.State.isin(State_chosen)]
        dff2 = dff2[dff2.State == "Maharashtra"]
        print(dff2)
        fig2 = px.pie(data_frame=dff2, values="gen", names='gen',
                      title='Population')
        return fig2
    else:
        print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')
        dff2 = df[df.State.isin(State_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.State == hov_year]
        fig2 = px.pie(data_frame=dff2, values="gen" ,names='State',
                     title=f'Population for: {hov_year}')
        return fig2


if __name__ == '__main__':
    app.run_server()
