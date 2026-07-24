import pandas as pd
import datetime as dt
import os
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import tab1
import tab2
import tab3
import plotly.graph_objects as go
import dash_auth


class db:
    def __init__(self):
        self.transactions = db.transaction_init()
        self.cc = pd.read_csv(r'db\country_codes.csv',index_col=0)
        self.customers = pd.read_csv(r'db\customers.csv',index_col=0)
        self.prod_info = pd.read_csv(r'db\prod_cat_info.csv')

    @staticmethod
    def transaction_init():
        transactions = pd.DataFrame()
        src = r'db\transactions'
        for filename in os.listdir(src):
            transactions = transactions._append(pd.read_csv(os.path.join(src,filename),index_col=0))

        def convert_dates(x):
            try:
                return dt.datetime.strptime(x,'%d-%m-%Y')
            except:
                return dt.datetime.strptime(x,'%d/%m/%Y')

        transactions['tran_date'] = transactions['tran_date'].apply(lambda x: convert_dates(x))

        return transactions

    def merge(self):
        df = self.transactions.join(self.prod_info.drop_duplicates(subset=['prod_cat_code'])
        .set_index('prod_cat_code')['prod_cat'],on='prod_cat_code',how='left')

        df = df.join(self.prod_info.drop_duplicates(subset=['prod_sub_cat_code'])
        .set_index('prod_sub_cat_code')['prod_subcat'],on='prod_subcat_code',how='left')

        df = df.join(self.customers.join(self.cc,on='country_code')
        .set_index('customer_Id'),on='cust_id')

        self.merged = df
    
    def add_trade_day(self):
        self.merged['trade_day'] = self.merged['tran_date'].dt.day_name()

    def add_age_when_transaction_done(self):
        self.merged["DOB"] = pd.to_datetime(self.merged["DOB"],dayfirst=True)
        self.merged['age'] = ((self.merged["tran_date"] - self.merged["DOB"]).dt.days / 365.25).astype(int)
        bins = [0, 25, 35, 45, 55, 150]
        labels = ["18-25", "26-35", "36-45", "46-55", "56+"]
        self.merged["age_group"] = pd.cut(self.merged["age"],bins=bins,labels=labels)
    def flag_transaction_multi_entry(self):
        self.merged["multi_entry_flag"] = (self.merged["transaction_id"].duplicated(keep=False))

df = db()
df.merge()
# Dodanie dnia tygodnia do df w celu wyświetlenia pierwszego wykresu tab 3
df.add_trade_day()
df.flag_transaction_multi_entry()
df.add_age_when_transaction_done()
print(df.merged[["Qty", "Rate", "Tax", "total_amt"]].head(10))
# Sprawdzanie danych do wyświetlenia informacji o klientach
print(df.merged["Store_type"].value_counts())
print(df.merged["country"].value_counts())
print(df.merged["country"].nunique())
# # Jest tylko 10 krajów można by je wrzucić do listy o ile w ogóle w danych są między nimi jakieś znaczące różnice bo może nie ma sensu jezeli są podobne
# print(pd.crosstab(df.merged["Store_type"], df.merged["country"], normalize="index") * 100)
# # Sprawdzenie zależności gender od typów sklepów
# print(pd.crosstab(df.merged["Store_type"], df.merged["Gender"], normalize="index") * 100)
# #  Sprawdzenie zależności wieku i typu kanału sprzedaży
# print(pd.crosstab(df.merged["Store_type"], df.merged["DOB"], normalize="index") * 100)
# print(df.merged["DOB"].min(), df.merged["DOB"].max())
# print(df.merged["tran_date"].min(), df.merged["tran_date"].max())
# # Dodanie przedziałów wiekowych do danych
# 
# print(pd.crosstab(df.merged["Store_type"], df.merged["age_group"], normalize="index") * 100)
# # Dane są raczej sfabrykowane pod ćwiczenia tutaj nie ma za wiele do pokazania zarządowi przynajmniej w pod tym kątem
# # Jeszcze tylko sprawdziłbym coś co zapewne jest zwrotem towaru.
# returns = df.merged[df.merged["total_amt"] < 0]
# print(pd.crosstab(returns["country"],returns["Store_type"]))
# # Analiza struktury klientów według kraju, płci oraz grup wiekowych nie wykazała istotnych różnic pomiędzy kanałami sprzedaży.

# # Sprawdzenie czy dla zwrotu istnieje transakcja odwrotna
# print(df.merged[df.merged["cust_id"] == 273764].sort_values("tran_date"))
# # Istnieje to samo transaction_id więc można takie transakcje odrzucić w drugim wykresie
# duplicates = df.merged["transaction_id"].value_counts()

# print(duplicates[duplicates > 1])
# print(df.merged[df.merged["transaction_id"] == 426787191].sort_values("tran_date"))
# print(df.merged[df.merged["transaction_id"] == 4170892941].sort_values("tran_date"))


# # counts = df.merged["transaction_id"].value_counts()
# # ids_2 = counts[counts == 2].index
# # duplicates_2 = df.merged[df.merged["transaction_id"].isin(ids_2)]
# # summary = duplicates_2.groupby("transaction_id")["total_amt"].sum()
# # print(summary[summary != 0])
# # print((duplicates[duplicates > 1]).count())
# print(duplicates[duplicates > 1].value_counts().sort_index())
print(df.merged[df.merged["transaction_id"] == 97439039119].sort_values("tran_date"))

print(f'puste dane = \n{df.merged.isna().sum()}')
#  nie ma znacząco dużo braków danych
print(f'duplikaty = \n{df.merged.duplicated().sum()}')
# 13 rekordów ma dokładne duplikaty w danych
print(df.merged[df.merged.duplicated(keep=False)])
# wszystkie są jednak ujemne nie będzie więc wiekszego problemu z odfiltrowaniem


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)
USERNAME_PASSWORD = [['user','pass']]

auth = dash_auth.BasicAuth(app, USERNAME_PASSWORD)

@app.callback(Output('tabs-content','children'),[Input('tabs','value')])
def render_content(tab):

    if tab == 'tab-1':
        return tab1.render_tab(df.merged)
    elif tab == 'tab-2':
        return tab2.render_tab(df.merged)
    elif tab == 'tab-3':
        return tab3.render_tab(df.merged)

## tab1 callbacks
@app.callback(Output('bar-sales','figure'),
    [Input('sales-range','start_date'),Input('sales-range','end_date')])
def tab1_bar_sales(start_date,end_date):

    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)]
    grouped = truncated[truncated['total_amt']>0].groupby([pd.Grouper(key='tran_date',freq='M'),'Store_type'])['total_amt'].sum().round(2).unstack()

    traces = []
    for col in grouped.columns:
        traces.append(go.Bar(x=grouped.index,y=grouped[col],name=col,hoverinfo='text',
        hovertext=[f'{y/1e3:.2f}k' for y in grouped[col].values]))

    data = traces
    fig = go.Figure(data=data,layout=go.Layout(title='Przychody',barmode='stack',legend=dict(x=0,y=-0.5)))

    return fig
@app.callback(Output('choropleth-sales','figure'),
            [Input('sales-range','start_date'),Input('sales-range','end_date')])
def tab1_choropleth_sales(start_date,end_date):

    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)]
    grouped = truncated[truncated['total_amt']>0].groupby('country')['total_amt'].sum().round(2)

    trace0 = go.Choropleth(colorscale='Viridis',reversescale=True,
                            locations=grouped.index,locationmode='country names',
                            z = grouped.values, colorbar=dict(title='Sales'))
    data = [trace0]
    fig = go.Figure(data=data,layout=go.Layout(title='Mapa',geo=dict(showframe=False,projection={'type':'natural earth'})))

    return fig
## tab2 callbacks
@app.callback(Output('barh-prod-subcat','figure'),
            [Input('prod_dropdown','value')])
def tab2_barh_prod_subcat(chosen_cat):

    grouped = df.merged[(df.merged['total_amt']>0)&(df.merged['prod_cat']==chosen_cat)].pivot_table(index='prod_subcat',columns='Gender',values='total_amt',aggfunc='sum').assign(_sum=lambda x: x['F']+x['M']).sort_values(by='_sum').round(2)

    traces = []
    for col in ['F','M']:
        traces.append(go.Bar(x=grouped[col],y=grouped.index,orientation='h',name=col))

    data = traces
    fig = go.Figure(data=data,layout=go.Layout(barmode='stack',margin={'t':20,}))
    return fig

## tab3 callbacks
@app.callback(Output('tab3-bar-sales-by-day','figure'),
            [Input('tab3-sales-range','start_date'),Input('tab3-sales-range','end_date')])

def tab3_sales_by_day(start_date,end_date):
    # print("CALLBACK TAB 3 URUCHOMIONY")
    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)&(df.merged['multi_entry_flag'] == False)&(df.merged['total_amt']>0)]
    grouped = truncated.groupby(['trade_day','Store_type'])['total_amt'].sum().round(2).unstack(fill_value=0)
    days_order = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ]
    grouped = grouped.reindex(days_order, fill_value=0)
    traces = []
    for col in grouped.columns:
            traces.append(go.Bar(x=grouped.index,y=grouped[col],name=col,hoverinfo='text',
            hovertext=[f'{y/1e3:.2f}k' for y in grouped[col].values]))
    
    data = traces
    fig = go.Figure(data=data,layout=go.Layout(title='Sprzedaż według dnia tygodnia',barmode='group',legend=dict(x=0,y=-0.5)))
    return fig

@app.callback(
    Output("tab3-sales-secondary-chart", "figure"),
    [Input("tab3-sales-range", "start_date"),Input("tab3-sales-range", "end_date")])

def tab3_clients_by_store_type(start_date, end_date):

    truncated = df.merged[(df.merged['tran_date']>=start_date)&(df.merged['tran_date']<=end_date)&(df.merged['multi_entry_flag'] == False)&(df.merged['total_amt']>0)]
    # # wewnętrzny check danych po dofiltrowaniu multi entry
    # print(f'liczba duplikatów po transaction id = {truncated["transaction_id"].duplicated().sum()}')
    # print(f'liczba ujemnych transakcji = {(truncated["total_amt"]< 0).sum()}')
    # # sprawdzenie czym są pojedyncze transaction_id z ujemną wartością <- dodałem jednak jeszcze (df.merged['total_amt']>0)
    # negative_single = truncated[truncated["total_amt"] < 0]
    # print(negative_single[["transaction_id","tran_date","Qty","Rate","Tax","total_amt","Store_type","prod_cat","prod_subcat"]])

    grouped = (pd.crosstab(truncated["Store_type"],truncated["Gender"],normalize="index") * 100)
    profits = truncated.groupby(['Store_type','Gender'])['total_amt'].sum().round(2).unstack(fill_value=0)

    traces = []

    for gender in grouped.columns:
        traces.append(go.Bar(x=profits.index,y=profits[gender],name=gender,hoverinfo="text",hovertext=[f"{value:.2f}$ income" for value in profits[gender]]))
    data = traces
    fig = go.Figure(data=data,layout=go.Layout(title='Przychody według płci klientów i kanału sprzedaży',barmode='group',legend=dict(x=0,y=-0.5)))
    return fig
    
app.layout = html.Div([html.Div([dcc.Tabs(id='tabs',value='tab-1',children=[
                            dcc.Tab(label='Sprzedaż globalna',value='tab-1'),
                            dcc.Tab(label='Produkty',value='tab-2'),
                            dcc.Tab(label='Kanały sprzedaży',value='tab-3')
                            ]),
                            html.Div(id='tabs-content')
                    ],style={'width':'80%','margin':'auto'})],
                    style={'height':'100%'})

if __name__ == '__main__':
    app.run(debug=True)