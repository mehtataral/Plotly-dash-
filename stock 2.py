# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:26:53 2022

@author: user
"""
import pandas as pd 
import numpy as np
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objects as go
df = pd.read_csv(r"https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv",parse_dates=["Date"])
df
df.info()
df.isnull().sum()  
df1_copy = df.copy() 
df1_copy
df1_copy.set_index("Date",inplace = True) # if index is true then we can't get DATE COLUMN 
x1 = df.iloc[:,:-1]
# df1 = px.data.stocks(indexed=True)-1
fig1 = px.line(df, x=df.Date, y="AAPL.Open")

fig2 = px.bar(df, x=df.Date, y="AAPL.Open")

fig3 = px.area(df1_copy, facet_col="direction", facet_col_wrap=2)

fig4 = px.line(x1,x=x1.Date,y=x1.columns, hover_name= "AAPL.Low",
               hover_data= ["AAPL.Open","AAPL.Close"],
               #hover_data=dict(x1.index: "|%B %d, %Y"),
              title='custom tick labels')

df1 =df.loc[df.Date >= "2016-11-21"]
fig5 = px.line(df1, x ="Date",y ="AAPL.Open")
fig5.update_xaxes(rangeslider_visible=True)
  

df2 = df.loc[(df["Date"] >= "2015-04-30") & (df["Date"] <= "2016-12-22")]
df2.drop("direction",inplace=True,axis ="columns")

fig6 = px.line(df2, x ="Date",y =df2.columns)
fig6.update_xaxes(rangeslider_visible=True)


fig7 = px.line(df, x='Date', y='AAPL.High', range_x=['2016-07-01','2016-10-31'])#range ofdate   
fig7.update_xaxes(rangeslider_visible=True)

# histfunc =  ['count', 'sum', 'avg', 'min', 'max']
fig8 = px.histogram(df, x="Date", y="AAPL.Close", histfunc="sum", title="Histogram on Date Axes")
# fig2 = px.line(df, x='Date', y="AAPL.Open",color ="direction")
# fig3 = px.line(df, x='Date', y="AAPL.Open",color ="direction")
fig9 = px.area(df, x="Date", y="AAPL.Close", title="Histogram on Date Axes")
fig9.update_xaxes(rangeslider_visible =True,
                  rangeselector =dict(
                      buttons =list([
                          # step =['month', 'year', 'day', 'hour', 'minute', 'second','all']
                          # stepmode =['backward', 'todate']
                          dict(count=1,label ="1Month",step="month",stepmode ="backward"),
                          dict(count=6,label ="6M",step="month",stepmode ="backward"),
                          dict(count=1,label ="YTD",step="year",stepmode ="todate"),
                          dict(count=1,label ="1Y",step="year",stepmode ="backward"),
                          dict(step ="all")
                          ])
                      )
                  )   

card0 =dbc.Card(children =[
    dbc.CardBody(children=[
        html.Label("Hi, I'm Taral Mehta"),
        html.H1("Byee")]
        ),
    dbc.CardBody(children =[
        html.Label("Hi, I'm learning Plotly Dash"),
        html.H1("Byee")]
        ),
  ],
    style ={
        "backgroundColor":"Gold"
        
        },
    
)
card1 =dbc.Card(children =[
    dbc.CardBody(children=[
        html.Label("Hi, I'm Mehta"),
        html.H1("Byee")]
        ),
    dbc.CardBody(children =[
        html.Label("Hi, I'm learning Dash"),
        html.H1("Byee")]
        ),
  ],
    style ={
        "backgroundColor":"Pink"
        },
    
)     

fig10 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = int(df["AAPL.Close"].tail(1)),
    number = {'prefix': "$"},
   delta = {'position': "top",'reference': 160},
    gauge = {
        'axis': {'visible': True}},
    domain = {'row': 2, 'column': 2}))


fig11 = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

app =dash.Dash()
type(app)

app.layout = html.Div( style ={ 
    "backgroundColor":"#111111"
    },
    children =[
        dcc.Checklist(id ="mychecklist",
                      options =[
                          {
                               "label":"2015",
                               "value":"2015"
                               },
                          {
                               "label":"2016",
                               "value":"2016"
                               },
                          
                          {
                               "label":"2017",
                               "value":"2017"
                               },
                          {
                               "label":"2018",
                               "value":"2018",
                               "disabled" :True
                               },
                          {
                               "label":"2019",
                               "value":"2019",
                               "disabled" :True
                               },
                          
                          ],
                      style ={"backgroundColor":"pink"}
                      ),
        dcc.Dropdown(id ="dropdown",
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
               "disabled": True,
               },
           {
               "label":"Date",
               "value":"Date",
               }], 
           clearable=False,
           multi = True,
           placeholder="Select a city",
            ),
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
               "value":"AAPL.Close"
               },
           {
               "label":"Date",
               "value":"Date",
         
               }], clearable=False,
            ),
        dcc.RadioItems(
            style ={
            "backgroundColor":"white"
            },
        id='radio_items',
        options=[
            {'label': 'Increasing', 'value': 'Increasing'},
            {'label': 'Decreasing', 'value': 'Decreasing'},
        ],
        value='Decreasing'
    ),
        dbc.Row(dbc.Col(children =[card0,card1],width =2)) ,
        # dbc.Row(card1),
        # dbc.CardGroup([card0, card1]) ,  # attaches cards with equal width and height columns
       # dbc.CardDeck([card0, card1])  ,  # same as CardGroup but with gutter in between cards
   
       # dbc.CardColumns([                        # Cards organised into Masonry-like columns
       #         card0,
       #         card1
       # ]),
        dcc.Graph(id ="linegraph",
          ),
        dcc.Graph(id ="linegraph01",
          ),
        dcc.Graph(id ="linegraph02",
          ),
        dcc.Graph(id ="linegraph03",
          ),
    html.Button('Submit', id='button',style ={"backgroundCOlor":"lightpink"}),
        
        html.Div("First Graph"), 
        
        dcc.Graph(id ="linegraph1",
          figure =fig1,
          ),
        dcc.Graph(id ="linegraph2",
           figure =fig2,
          ),
        dcc.Graph(id ="linegraph3",
           figure =fig3,    
          ),
        dcc.Graph(id ="linegraph4",
           figure =fig4,    
          ),
        dcc.Graph(id ="linegraph5",
           figure =fig5,    
          ),
        dcc.Graph(id ="linegraph6",
           figure =fig6,    
          ),
        dcc.Graph(id ="linegraph7",
           figure =fig7,    
          ),
        dcc.Graph(id ="linegraph8",
           figure =fig8,    
          ),
        dcc.Graph(id ="linegraph9",
           figure =fig9,    
          ),
        dcc.Graph(id ="linegraph10",
           figure =fig10,    
          ),
        dcc.Graph(id ="linegraph11",
          figure =fig11
          ),
       ]
    )
@app.callback(
    Output("linegraph", "figure"), 
    Input("dropdown", "value"),
    Input("dropdown1", "value"))


def display_time_series(dropdown1,dropdown):
    # df = pd.read_csv(r"https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv",parse_dates=["Date"])
    # df = px.data.stocks() # replace with your own data source
    fig = px.line(df, x=dropdown1, y=dropdown)
    return fig



@app.callback(
    Output("linegraph01", "figure"), 
    Input("dropdown", "value"))


def display_time_series(dropdown):
    # df = pd.read_csv(r"https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv",parse_dates=["Date"])
    # df = px.data.stocks() # replace with your own data source
    # fig = px.line(df, x='Date', y=dropdown)
    fig0 = px.line(df, x="Date", y=dropdown)
    return fig0



@app.callback(
    Output("linegraph02", "figure"), 
    Input("radio_items", "value"),
    )

def radio_button_update(r_button_value):
    print("=============")
    print(r_button_value)
    df_filter = df[df["direction"] == r_button_value]
    fig10 = px.line(df_filter, x=df_filter["Date"], y=df_filter["AAPL.Low"])
    return fig10




@app.callback(
    Output("linegraph03", "figure"), 
    Input("mychecklist", "value"),
    )

def check_button_update(check_button_value,dropdown):
    print("*************")
    print(check_button_value)
   # df.Date.dt.year =="2015"
    temp_year =df.Date.dt.year.unique()
    print(temp_year)
    
    # df.Date.dt.year ==check_button_value
    new_df =df.Date.dt.year.isin(check_button_value)
    fig11 = px.line(df, x =new_df,y =dropdown)
    return fig11
    
if __name__ =="__main__":
    app.run()











