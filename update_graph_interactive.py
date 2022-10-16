from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd 

df = pd.read_csv(r"https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv",parse_dates=["Date"])

df["Year"] = df.Date.dt.year

df["Year"] =df.Year.astype(str)

df["Month"] = df.Date.dt.month

df1_copy = df.copy() 

df1_copy.Month.unique()
df1_copy.sort_values("Month",inplace=True)
df1_copy["Month_in_Word"] = df1_copy.Month.astype(str)

df1_copy.Month_in_Word.replace({"1":"January",
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

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    update_title=None)

fig100 =px.bar(df1_copy,x=df1_copy["Month_in_Word"], y=df1_copy["AAPL.Close"],color =df1_copy["Year"])  

app.layout =html.Div([
    dbc.Row([
        dbc.Col(
           html.H6(
               "Stock Market Dashboard1", 
               style ={"textAlign":"Right"},
               #className='text-center'
           ),
           width ={'size':4,'offset':1, 'order':2},
       ),
       dbc.Col(
           html.H6(
               "Stock Market Dashboard2", 
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
           dcc.Dropdown(
                id ="dropdown-stock-type",
                multi =True,
                value=["AAPL.Close"],
                options = [
                    {
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
               }
           ],
       ),
   ], 
       width={'size':2, 'offset':1, 'order':2},
   ),]),
    dbc.Row(
        dbc.Col(
            dcc.Checklist(
                id='my_checklist',# used to identify component in callback
                options=[
                        {'label': "2015", 'value': "2015", 'disabled':False},
                        {'label': "2016", 'value': "2016", 'disabled':False},
                        ],
               # value=['2019'],    
               inputStyle={'cursor':'pointer'},      # style of the <input> checkbox element
               style = {"backgroundColor":"lightblue"},
           ),
            )
 ),
 dbc.Row([
     dbc.Col( dcc.Graph(id="line-stock"), width={'size':6} ),
        dbc.Col( dcc.Graph(id="linegraph1", figure=fig100), width={'size':6} ),
    ]),
    dbc.Row([
        dbc.Col( dcc.Graph(id='pie-population') ),
    ]),
])
@callback(
    Output("line-stock","figure"),
    Input("dropdown-stock-type","value"), )
def graph1(dropdown):
    return px.line(df, x='Date', y=dropdown, title =" Date vs  GRaph",)


@callback(
    Output("pie-population","figure"),
    Input("line-stock","hoverData"),
    Input("my_checklist","value"), )
def graph2(hov_data, Year_chosen):
    if hov_data is None:
        return px.pie(df, values='Year', names='direction', title='stock for 2017')
    else:
        hov_year = hov_data['points'][0]["x"][:4]
        dff2 = df[df.Year == hov_year]
        return px.pie(data_frame=dff2, values='Year', names='direction', title=f'Population for: {hov_year}')

if  __name__ =="__main__":
    app.run()   







