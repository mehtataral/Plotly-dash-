# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:57:15 2022

@author: user
"""

import pandas as pd 
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import datetime as dt


df = pd.read_csv(r"https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv",parse_dates=["Date"])
# df =pd.read_csv(r"C:\Users\Admin\Downloads\apple_stock.csv",parse_dates=["Date"])
df
df.info()
df.isnull().sum()
df["Year"] = df.Date.dt.year
df
df["Year"] =df.Year.astype(str)
df.info()
df["Month"] = df.Date.dt.month
df
df1_copy = df.copy() 
df1_copy

df1_copy.Month.unique()
df1_copy.sort_values("Month",inplace=True)
df1_copy["Month_in_Word"] = df1_copy.Month.astype(str)
df1_copy.info()
df1_copy.Month_in_Word.replace(
                  {"1":"January",
                  "2":"February",
                  "3":"March",
                  "4":"April",
                  "5":"May",
                  "6":"June", 
                  "7":"July",
                  "8":"August",
                  "9":"September",
                  "10":"October",
                  "11":"November",
                  "12":"December",
                  },inplace=True)
df
df1_copy
df.info()
df1_copy.info()

app =dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

fig100 =px.bar(df1_copy,x=df1_copy["Month_in_Word"], y=df1_copy["AAPL.Close"],color =df1_copy["Year"])  

# app.layout =dbc.Container(
app.layout =html.Div(
    [
    dbc.Row([
            dbc.Col(html.H6("Stock Market Dashboard1", 
                            style ={"textAlign":"Right"},
                            #className='text-center'
                            ),
                width ={'size':4,'offset':1, 'order':2},
                ),
            dbc.Col(html.H6("Stock Market Dashboard2", 
                            #className='text-center',
                            style ={"textAlign":"Right"}
                            ),
                width={'size':4, 'offset':1, 'order':1},
                ),
            ]),
    # Horizontal:start,center,end,between,around
    # style={"width": "6rem"},
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id ="dropdown1",
                options = [{
                    "label":"AAPL.Open",
                    "value":"AAPL.Open"
                    },
                {
                    "label":"AAPL.High",
                    "value":"AAPL.High"   
                    },
               
                {
                    "label":"AAPL.Low ",
                    "value":"AAPL.Low"
                    },
               
                {
                    "label":"AAPL.Close",
                    "value":"AAPL.Close",
                   
                    }],multi =True),
        ], width={'size':2, 'offset':1, 'order':2},
            #xs=12, sm=12, md=12, lg=5, xl=5
        ),
        ]),
    dbc.Row(dbc.Col(
        dcc.Checklist(id='my_checklist',# used to identify component in callback
                options=[
                        {'label': "2015", 'value': "2015", 'disabled':False},
                        {'label': "2016", 'value': "2016", 'disabled':False},
                        {'label': "2017", 'value': "2017", 'disabled':False},
                        {'label': "2018", 'value': "2018", 'disabled':True}
                ],
                # value=['2019'],    
                inputStyle={'cursor':'pointer'},      # style of the <input> checkbox element
                style ={
                "backgroundColor":"lightblue"
                },
            ),
        )),
    dbc.Row([
        dbc.Col(dcc.Graph(id="linegraph0"),width ={'size':6}),
        dbc.Col(dcc.Graph(id="linegraph1",figure =fig100),width ={'size':6}),
        ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='pie_graph'))
      ]),
    ])

@app.callback(
    Output("linegraph0","figure"),
    Input("dropdown1","value"),
    )

def graph1(dropdown):
    fig0 = px.line(df, x='Date', y=dropdown, title =" Date vs  GRaph",)
    return fig0
  
    
@app.callback(
    Output("pie_graph","figure"),
    Input("linegraph0","hoverData"),
    Input("my_checklist","value"),
    )

def graph2(hov_data,Year_chosen):
    if hov_data is None:
        dff2 = df[df.Year.isin(Year_chosen)]
        dff2 = dff2[dff2.Year == "2017"]
        print(dff2)
        fig2 = px.pie(data_frame=dff2, values='2017', names='direction',
                      title='stock for 2017')
        return fig2
    else:
        print(hov_data)
        print("*********************************************")
        print(f'hover data: {hov_data}')
        dff2 = df[df.Year.isin(Year_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.Year == hov_year]
        fig2 = px.pie(data_frame=dff2, values='Year', names='direction', title=f'Population for: {hov_year}')
        return fig2
    
if  __name__ =="__main__":
    app.run()   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
