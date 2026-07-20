from dash import Dash, dcc, html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = Dash(__name__)

data = [go.Scatter(x=[1,2,3,4], y=[10,20,30,40])]
layout = go.Layout(title="Pierwszy wykres", width=600, height=600)
fig = go.Figure(data=data, layout=layout)

app.layout = html.Div(children=[
    html.H1("Mój dashboard"),
    html.Div("Tu pojawi się content"),
    dcc.Graph(id="first-graph", figure=fig)
])

@app.callback(Output(component_id='first-graph',component_property='figure'),
            [Input('my-slider','value')])
def update_figure(max_range):

    data = [go.Scatter(x=[1,2,3,4],y=[10,20,30,40])]
    layout = go.Layout(title='Pierwszy wykres',width=600,height=300,
    xaxis=dict(range=[1,max_range]))
    fig = go.Figure(data=data,layout=layout)

    return fig

app.layout = html.Div(children=[
            html.H1('Mój dashboard',style={'margin':'auto'}),
            html.Div('Tu pojawi się content',style={'color':'red'}),
            dcc.Graph(id='first-graph',figure=fig),
            html.Label('Slider'),
            html.Div([dcc.Slider(id='my-slider',min=1,max=4,step=1,value=1)],
            style={'width':'400px'})
])

if __name__ == '__main__':
    app.run()