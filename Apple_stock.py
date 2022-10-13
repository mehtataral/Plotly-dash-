

#******************************** database connectivity   ********************************

import mysql.connector as mysql
import pandas as pd

db_con =mysql.connect(host ="localhost",user="root",passwd ="root",
                      database ="d1")

# optional Part
# my_cur =db_con.cursor()
# my_cur.execute("use abc;")
# my_cur.execute("select * from stud_db;")
# for x in my_cur:
#     print(x)
    
query = 'select * from apple_stock'

df = pd.read_sql(query, con = db_con,parse_dates=["Date"],)
print(df)
df.info()

# *********************** Stock Market *************************************************

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


app =dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

fig5 =go.Figure()
fig5.add_scattergl(x=df["Date"], y=df["AAPL.Close"],line={'color': 'black'})

# Full line
fig5.add_scattergl(x=df["Date"], y=df["AAPL.Close"].where(df["AAPL.Close"] <=115), 
                    line={'color': 'red'})

# Above threshhgold    
fig5.add_scattergl(x=df["Date"],y=df["AAPL.Close"].where(df["AAPL.Close"] >115),
                  line={'color': 'green'})


fig5.update_traces(mode="markers+lines",   
                   hovertemplate="%{y}%{_xother}")

fig5.update_layout(hovermode="x unified")
fig5.update_layout(height=700,width=1000)

fig6 = go.Figure()

fig6.add_trace(go.Bar(
    x=df["Date"],
    y=df["AAPL.Close"],
    # xperiod="M3",
    # xperiodalignment="middle",
    # xhoverformat="Q%q",
    hovertemplate="%{y}"
))

fig6.add_trace(go.Scatter(
    x=df["Date"],
    y=df["AAPL.Low"],
    # xperiod="M1",
    # xperiodalignment="middle",
    hovertemplate="%{x}"
))

fig100 =px.line(x=df["Date"], y=df["AAPL.Close"])  

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

        dbc.Col(
            dcc.Dropdown(id ="dropdown2",
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
                     
                    }] ),
            width={'size':2, 'offset':1, 'order':1},
            #xs=12, sm=12, md=12, lg=5, xl=5,
        ),
    dbc.Col(
        dcc.Dropdown(id ="dropdown3",
            options = [
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
            ] ),
        width={'size':2, 'offset':1, 'order':3},
        #xs=12, sm=12, md=12, lg=5, xl=5,
    ),
    dbc.Col(
        dcc.Dropdown(id ="dropdown4",
            options = [
            {
                "label":"Increasing",
                "value":"Increasing"
                },
            {
                "label":"Decreasing",
                "value":"Decreasing"
                },
            ] ),
        width={'size':2, 'offset':1,"order":4},
        #xs=12, sm=12, md=12, lg=5, xl=5,
    )
    ]),
    dbc.Row(dbc.Col(dcc.RadioItems(
            style ={
            "backgroundColor":"white",
            "textAlign":"Right"
            },
        id='radio_items',
        options=[
            {'label': 'Increasing', 'value': 'Increasing'},
            {'label': 'Decreasing', 'value': 'Decreasing'},
        ],
        value='Decreasing'
    ),width ={'size':2, "offset":2,"order":5})),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id="linegraph0"),width ={'size':6}),
        dbc.Col(dcc.Graph(id="linegraph1"),width ={'size':6}),
        ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='pie_graph')),
        dbc.Col(dcc.Graph(figure =fig100))
      ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="linegraph2"),width ={'size':6}),
        dbc.Col(dcc.Graph(id="linegraph3"),width ={'size':6}),  
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
    dbc.Row(dbc.Col(
        dcc.Checklist(id='my_checklist2',# used to identify component in callback
                options=[
                         {'label': "January", 'value':"1", 'disabled':False},
                         {'label': "February", 'value':"2", 'disabled':False},
                         {'label': "March", 'value':"3", 'disabled':False},
                         {'label': "April", 'value':"4", 'disabled':False},
                         {'label': "May", 'value':"5", 'disabled':False},
                         {'label': "June", 'value':"6", 'disabled':False},
                         {'label': "July", 'value':"7", 'disabled':False},
                         {'label': "August", 'value':"8", 'disabled':False},
                         {'label': "September", 'value':"9", 'disabled':False},
                         {'label': "October", 'value':'10', 'disabled':False},
                         {'label': "November", 'value':"11", 'disabled':False},
                         {'label': "December", 'value':"12", 'disabled':False}
                         # for x in df['Month Call Made'].unique()
                ],
               # value=['2019'],    
               inputStyle={'cursor':'pointer'},      # style of the <input> checkbox element
               style ={
               "backgroundColor":"lightpink"
               },
            ),
        )),
    dbc.Row(dbc.Col([dbc.CardLink("First link",  href="#"),
                     dbc.CardLink("Second link", href="https://Amazon.com")],
                    width="auto")),
    

    dbc.Row([
        dbc.Col(dcc.Graph(id="linegraph4"),width ={'size':6}),
        ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id="linegraph6",figure =fig5),width ={'size':6}),
        ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="linegraph7",figure =fig6),width ={'size':6}),
        ])
    
    ])
  
   
@app.callback(
    Output("linegraph0", "figure"), 
    Input("dropdown1", "value"))

def display_time_series(dropdown):
    fig0 = px.line(df, x='Date', y=dropdown, title =" Date vs  GRaph",)
    return fig0


@app.callback(
    Output("linegraph1", "figure"), 
    Input("dropdown1", "value"),
    Input("dropdown3", "value"))

def display_time_series(dropdown2,dropdown3):
    dff =df[df["Year"]==dropdown3]
    fig1 = px.line(dff, x="Date", y =dropdown2,title =" GRaph vs  GRaph")
    return fig1


@app.callback(
    Output("linegraph2", "figure"), 
    Input("radio_items", "value"),
    )

def radio_button_update(r_button_value):
    print("=============")
    print(r_button_value)                
    print("=============")
    # df[df["direction"] == "Decreasing"] ---- it shows whole data frame
    df_filter1 = df[df["direction"] == r_button_value]
    fig2 = px.line(df_filter1, x=df_filter1["Date"], y=df_filter1["AAPL.Low"],title =" Date vs  Low")
    return fig2

#line chart
@app.callback(
    Output("linegraph3", "figure"), 
    Input("my_checklist", "value"),
    )
    
def line_update(options_chosen):
    print("=============")
    print(options_chosen)      
    print("=============")
    # df[df["Year"] == 2015] ---- it shows whole data 
    x = df.Year.unique()
    x
    df_filter2 = df[df["Year"].isin(options_chosen)]
    print ("**************",df_filter2['Year'].unique(),"********")
    fig3 = px.pie(df_filter2, values ="AAPL.Low",hole =0.4)
    return fig3


@app.callback(
    Output("linegraph4", "figure"), 
    Input("my_checklist2", "value"))

def month_wise_graph(options_chosen):
    print("***********Month is word******************",options_chosen)
    df_filter_v1 = df1_copy[df1_copy['Year']=='2015']
    df_filter_v1["Month"]=df_filter_v1.Month.astype(str)
    df_filter_v1["Month"]    
    df_filter3 =df_filter_v1[df_filter_v1["Month"].isin(options_chosen)]
    fig4 = px.bar(df_filter3, x="Date", y="AAPL.Low", title =" Month vs  GRaph")
    return fig4

@app.callback(
    Output(component_id='pie_graph', component_property='figure'),
    Input(component_id='my_graph', component_property='hoverData'),
    Input(component_id='dropdown2', component_property='value')
)
def update_side_graph(hov_data, country_chosen):
    if hov_data is None:
        return fig100
    else:
        print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')
        dff2 = df1_copy[df1_copy.country.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.year == hov_year]
        fig2 = px.pie(data_frame=dff2,values='AAPL.Low', names='direction', title=f'Population for: {hov_year}')
        return fig2

if  __name__ =="__main__":
    app.run()   
