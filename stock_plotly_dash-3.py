# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:26:53 2022

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
               hover_data= ["AAPL.Open","AAPL.Close"],#hover_data=dict(x1.index: "|%B %d, %Y"),
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

fig000 = go.Figure()

fig000= go.Figure(go.Indicator(
    value = int(df["AAPL.Open"].tail(1)),
    mode = "gauge+number",
    delta = {'reference': 160},
    gauge = {
        'axis': {'visible': True}},
    domain = {'row': 0, 'column': 0}))


fig001 = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])
app =dash.Dash()
type(app)
card =dbc.Card(children =[
    # dbc.CardImg(src =r"/Users/user/Downloads/PYTHON 1.png", className = 'align-self-center',top =True),
    dbc.CardBody(children =
        [
            html.Label("Hiiiiiiiiiiiii"),
            dbc.Button("Goooo Somewhere")
            ],
        ), 
    ],        style ={
            "backgroundColor":"Green","width": "11rem"
            },
    )

card1 = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Title", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text",
            ),
            dbc.CardLink("Card link", href="#"),
            dbc.CardLink("External link", href="https://google.com"),
            dbc.CardLink(children =["External link","My data"], href="https://amazon.com"),
        ],
        style ={
        "backgroundColor":"blue"
        },
    ),
    style={"width": "18rem"},
)
app.layout = html.Div( style ={ 
    "backgroundColor":"#111111"
    },
    children =[
        dcc.Checklist(id='my_checklist',# used to identify component in callback
               options=[
                        {'label': "2015", 'value': "2015", 'disabled':False},
                        {'label': "2016", 'value': "2016", 'disabled':False},
                        {'label': "2017", 'value': "2017", 'disabled':False},
                        {'label': "2018", 'value': "2018", 'disabled':True}
               ],
               # value=['2019'],
               style ={
               "backgroundColor":"blue"
               },
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
               "value":"AAPL.Close"
               }], 
           clearable=False,
           multi =True,
           placeholder ="select your data "
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
               "value":"AAPL.Close",
               "disabled":True
               
               }], clearable=True,
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
        dcc.Graph(id ="linegraph",
          ),
        dcc.Graph(id ="linegraph01",
          ),
        dcc.Graph(id ="linegraph02",
          ),
        dcc.Graph(id ="linegraph000",
                  figure =fig000
          ),
        dcc.Graph(id ="linegraph001",      
                  figure =fig001
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
          ),
        dbc.Row([card]),
        dbc.Row(card1),
        # dbc.CardGroup([card, card1])   # attaches cards with equal width and height columns
        # dbc.CardDeck([card, card1])    # same as CardGroup but with gutter in between cards
     
        # dbc.CardColumns([                        # Cards organised into Masonry-like columns
        #         card,
        #         card1
        # ])

   # dbc.Row(
   #  [
   #      dbc.Col(card, width=4),
   #      dbc.Col(card1, width=8),
   #  ])
        ]
    )
@app.callback(
    Output("linegraph", "figure"), 
    Input("dropdown", "value"))


def display_time_series(dropdown):
    # df = pd.read_csv(r"https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv",parse_dates=["Date"])
    # df = px.data.stocks() # replace with your own data source
    # fig = px.line(df, x='Date', y=dropdown)
    fig = px.line(df, x='Date', y=dropdown)
    return fig



@app.callback(
    Output("linegraph02", "figure"), 
    Input("dropdown1", "value"),
    Input("dropdown", "value"))


def display_time_series(dropdown,dropdown1):
    # df = pd.read_csv(r"https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv",parse_dates=["Date"])
    # df = px.data.stocks() # replace with your own data source
    # fig = px.line(df, x='Date', y=dropdown)
    fig0 = px.line(df, x=dropdown, y  =dropdown1)
    return fig0



@app.callback(
    Output("linegraph01", "figure"), 
    Input("radio_items", "value"),
    )

def radio_button_update(r_button_value):
    print("=============")
    print(r_button_value)
    df_filter = df[df["direction"] == r_button_value]
    fig10 = px.line(df_filter, x=df_filter["Date"], y=df_filter["AAPL.Low"])
    return fig10


@app.callback(
    Output("linegraph10", "figure"), 
    Input("my_checklist", "value"))


def check_button_graph(options_chosen):
    new_df = df.Date.dt.year.isin(options_chosen)
    # print (new_df['Date'].unique())
    fig11=px.line(data_frame=new_df,values='Date',names='Date')

if __name__ =="__main__":
    app.run()












