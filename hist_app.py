import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd
import dropdown_options
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Col, Row
from numpy import linspace
import numpy as np
import plotly.graph_objects as go

df=pd.read_csv('/merged_perfiles_fondos.csv')
var = [{'label':i, 'value':i} for i in df.filter(regex='^[^Q]').columns]


def dropdown(ide, options):
    return dcc.Dropdown(id=ide, options = options, value=options[0]['value'])

def checklist(ide, options):
    return dcc.Checklist(id=ide, options = options, value=[x['value'] for x in options],
                         labelStyle={'display':'inline-block'})
    
def rgslider(ide, var, n_marks):
    limits = (var.min(), var.max())
    return dcc.RangeSlider(id = ide, min=limits[0], max=limits[1], 
                           step=(limits[1]-limits[0])/100, value = limits,
                           marks = {i:'{:.1f}'.format(i) for i in linspace(limits[0], limits[1], n_marks)})




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

layout = {
    "autosize":True,
    "automargin":True,
    "margin":{"l":"30", "r":"30", "b":"50", "t":"80"},
    "paper_bgcolor": "#555",
    "plot_bgcolor": "rgba(1, 1, 1, 0.1)",
    "titlefont": {"color": "#FFF"},
    "xaxis": {"tickfont": {"color": "#FFF"}},
    "yaxis": {"tickfont": {"color": "#FFF"}}
}

app.layout = html.Div([
    Row([
        Col([html.H1('Histogram Comparison for bme data',
                     style = {'margin-bottom':50, 'margin-top':20})],
            width={"size": 12, "offset": 1})
    ]),
    Row([
        Col([
            dcc.Graph(id='hist_1', style={'width':'95%','box-shadow':'2px 2px 2px grey'})
        ], width={"size": 4, "offset": 1}),
        Col([
            html.Div([
                html.Div([
                    html.H3('Hist 1'),
                    dropdown('var_1', var),
                    Row([Col(html.H5('Q0: '), sm=1), Col(checklist('multi_Q0_1',dropdown_options.Q0))]),
                    Row([Col(html.H5('Q1: '), sm=1), Col(checklist('multi_Q1_1',dropdown_options.Q1))]),
                    Row([Col(html.H5('Q2: '), sm=1), Col(checklist('multi_Q2_1',dropdown_options.Q2))]),
                    Row([Col(html.H5('Q3: '), sm=1), Col(checklist('multi_Q3_1',dropdown_options.Q3))]),
                    Row([Col(html.H5('Q4: '), sm=1), Col(rgslider('rgslider_Q4_1',df.Q4, 8))]),
                    Row([Col(html.H5('Q5: '), sm=1), Col(rgslider('rgslider_Q5_1',df.Q5, 5))]),
                    Row([Col(html.H5('Q6: '), sm=1), Col(rgslider('rgslider_Q6_1',df.Q6, 5))]),
                    Row([Col(html.H5('Q7: '), sm=1), Col(checklist('multi_Q7_1',dropdown_options.Q7))]),
                    Row([Col(html.H5('Q8: '), sm=1), Col(rgslider('rgslider_Q8_1',df.Q8, 5))]),
                    Row([Col(html.H5('Q9: '), sm=1), Col(checklist('multi_Q9_1',dropdown_options.Q9))]),
                    Row([Col(html.H5('Q10: '), sm=1), Col(rgslider('rgslider_Q10_1',df.Q10, 5))])
                ], style={'width':'95%'})
            ], style={'width':'95%', 'box-shadow':'2px 2px 2px grey'})
        ])
        
    ]),
    Row([
        Col([
            dcc.Graph(id='hist_2', style={'width':'95%','box-shadow':'2px 2px 2px grey'})
        ], width={"size": 4, "offset": 1}),
        Col([
            html.Div([
                html.Div([
                    html.H3('Hist 2'),
                    dropdown('var_2', var),
                    Row([Col(html.H5('Q0: '), sm=1), Col(checklist('multi_Q0_2',dropdown_options.Q0))]),
                    Row([Col(html.H5('Q1: '), sm=1), Col(checklist('multi_Q1_2',dropdown_options.Q1))]),
                    Row([Col(html.H5('Q2: '), sm=1), Col(checklist('multi_Q2_2',dropdown_options.Q2))]),
                    Row([Col(html.H5('Q3: '), sm=1), Col(checklist('multi_Q3_2',dropdown_options.Q3))]),
                    Row([Col(html.H5('Q4: '), sm=1), Col(rgslider('rgslider_Q4_2',df.Q4, 8))]),
                    Row([Col(html.H5('Q5: '), sm=1), Col(rgslider('rgslider_Q5_2',df.Q5, 5))]),
                    Row([Col(html.H5('Q6: '), sm=1), Col(rgslider('rgslider_Q6_2',df.Q6, 5))]),
                    Row([Col(html.H5('Q7: '), sm=1), Col(checklist('multi_Q7_2',dropdown_options.Q7))]),
                    Row([Col(html.H5('Q8: '), sm=1), Col(rgslider('rgslider_Q8_2',df.Q8, 5))]),
                    Row([Col(html.H5('Q9: '), sm=1), Col(checklist('multi_Q9_2',dropdown_options.Q9))]),
                    Row([Col(html.H5('Q10: '), sm=1), Col(rgslider('rgslider_Q10_2',df.Q10, 5))])
                ], style={'width':'95%'})
            ], style={'width':'95%','box-shadow':'2px 2px 2px grey'})
        ])
    ]),
    html.Div('bme-data')
        
], style = {'background-color': '#333'})



@app.callback(
    Output('hist_1', 'figure'),
    [Input('multi_Q0_1', 'value'),
     Input('multi_Q1_1', 'value'),
     Input('multi_Q2_1', 'value'),
     Input('multi_Q3_1', 'value'),
     Input('multi_Q7_1', 'value'),
     Input('multi_Q9_1', 'value'),
     Input('var_1', 'value'), 
     Input('rgslider_Q4_1', 'value'),
     Input('rgslider_Q5_1', 'value'),
     Input('rgslider_Q6_1', 'value'),
     Input('rgslider_Q8_1', 'value'),
     Input('rgslider_Q10_1', 'value')]
)
def display_hist(Q0_filter, Q1_filter, Q2_filter, Q3_filter, Q7_filter, Q9_filter,
                 var,
                 Q4_filter, Q5_filter, Q6_filter, Q8_filter, Q10_filter):
    mask = df.Q0.isin(Q0_filter)
    iterable = zip(['Q{}'.format(i) for i in (1,2,3,7,9)], 
                   (Q1_filter, Q2_filter, Q3_filter, Q7_filter, Q9_filter))
    for x in iterable:
        mask = (mask) & (df[x[0]].isin(x[1]))
    
    iterable = zip(['Q{}'.format(i) for i in (4,5,6, 8, 10)], 
                   (Q4_filter, Q5_filter, Q6_filter, Q8_filter, Q10_filter))
    for x in iterable:
        mask = (mask) & (df[x[0]] >= x[1][0]) & (df[x[0]] <= x[1][1])
    
    layout['title'] = var
    
    result = {
        'data': [
            {
                'x': df[mask][var],
                'type': 'histogram'
            },
        ],
        'layout': layout
    }
    
    return result


@app.callback(
    Output('hist_2', 'figure'),
    [Input('multi_Q0_2', 'value'),
     Input('multi_Q1_2', 'value'),
     Input('multi_Q2_2', 'value'),
     Input('multi_Q3_2', 'value'),
     Input('multi_Q7_2', 'value'),
     Input('multi_Q9_2', 'value'),
     Input('var_2', 'value'), 
     Input('rgslider_Q4_2', 'value'),
     Input('rgslider_Q5_2', 'value'),
     Input('rgslider_Q6_2', 'value'),
     Input('rgslider_Q8_2', 'value'),
     Input('rgslider_Q10_2', 'value')]
)
def display_hist2(Q0_filter, Q1_filter, Q2_filter, Q3_filter, Q7_filter, Q9_filter,
                 var,
                 Q4_filter, Q5_filter, Q6_filter, Q8_filter, Q10_filter):
    mask = df.Q0.isin(Q0_filter)
    iterable = zip(['Q{}'.format(i) for i in (1,2,3,7,9)], 
                   (Q1_filter, Q2_filter, Q3_filter, Q7_filter, Q9_filter))
    for x in iterable:
        mask = (mask) & (df[x[0]].isin(x[1]))
        
    iterable = zip(['Q{}'.format(i) for i in (4,5,6, 8, 10)], 
                   (Q4_filter, Q5_filter, Q6_filter, Q8_filter, Q10_filter))
    for x in iterable:
        mask = (mask) & (df[x[0]] >= x[1][0]) & (df[x[0]] <= x[1][1])   
        
    layout['title'] = var
    
    raw_values = df[mask][var].dropna()
    n_bins = int(np.sqrt(raw_values.shape[0]))
    x = np.histogram(raw_values, bins = n_bins)[1]
    y = np.histogram(raw_values, bins = n_bins)[0]
    
    mean = raw_values.mean()
    median = raw_values.median()
    fst_quarter = raw_values.quantile(0.25)
    thr_quarter = raw_values.quantile(0.75)
    max_hist = y.max()
    
    result = {
        'data': [
            {
                'x': x,
                'y': y,
                'type': 'bar'
            },
            {
                'x': [mean, mean],
                'y': [0, max_hist * 1.01],
                'type': 'line', 
                'name': 'mean',
            },
            {
                'x': [median, median],
                'y': [0, max_hist * 1.01],
                'type': 'line', 
                'name': 'median'
            },
            {
                'x': [fst_quarter, fst_quarter],
                'y': [0, max_hist * 0.7],
                'type': 'line', 
                'name': 'fst_quarter'
            },
            {
                'x': [thr_quarter, thr_quarter],
                'y': [0, max_hist * 0.7],
                'type': 'line', 
                'name': 'thr_quarter'
            },
        ],
        'layout': layout,
        
    }
    
    return result



if __name__ == '__main__':
    app.run_server(debug=True)
