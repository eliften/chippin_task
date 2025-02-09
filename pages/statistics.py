from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import middleware

time_series_df, customer_anlys_df, branch_analys_df = middleware.get_data()

def layout():
    layout = html.Div([
        html.H1("Satış ve Müşteri Analizi Dashboard", style={'textAlign': 'center'}),
        dbc.Card(
            dbc.CardBody([
                html.Label("Zaman Periyodu Seç:"),
                dcc.Dropdown(
                    id="time_series_dropdown",
                    options=[{"label": i, "value": i} for i in ["Günlük", "Aylık", "Haftalık", "Hafta sonu/Hafta içi"]],
                    value="Aylık",
                    clearable=False
                ),
                dcc.Graph(id="customer_analysis_graph") ,
                dcc.Graph(id="customer_features_graph"),
                dcc.Graph(id="branch_features_graph") 
            ]
            ),
            id='customer_analysis_card'
        ),
    ])
    return layout

layout = layout()


@callback(
    Output("customer_analysis_graph", "figure"),
    Output("customer_features_graph", "figure"),
    Output("branch_features_graph", "figure"),
    Input("time_series_dropdown", "value")
)
def update_customer_analysis_graph(value):
    if value == "Günlük":
        df_grouped = time_series_df.groupby('day_of_week').agg(
            total_sales=('cb_customer_id', 'count')
        ).reset_index()
        fig_time = px.pie(df_grouped, names='day_of_week', values='total_sales', hole=.3,
                    title="Günlük Satışlar: Toplam Satışlar")
    elif value == "Haftalık":
        df_grouped = time_series_df.groupby('week_of_year').agg(
            total_sales=('cb_customer_id', 'count')
        ).reset_index()
        fig_time = px.pie(df_grouped, names='week_of_year', values='total_sales', hole=.3,
                    title="Haftalık Satışlar: Toplam Satışlar")
    elif value == "Hafta sonu/Hafta içi":
        df_grouped = time_series_df.groupby('is_weekend').agg(
            total_sales=('cb_customer_id', 'count')
        ).reset_index()
        fig_time = px.pie(df_grouped, names='is_weekend', values='total_sales', hole=.3,
                    title="Haftasonu Satışlar: Toplam Satışlar")
    else:
        df_grouped = time_series_df.groupby('month').agg(
            total_sales=('cb_customer_id', 'count')
        ).reset_index()
        fig_time = px.pie(df_grouped, names='month', values='total_sales', hole=.3,
                    title="Aylık Satışlar: Toplam Satışlar")

    df_top_100 = customer_anlys_df.nlargest(100, "total_transactions")
    df_top_100["cb_customer_id"] = df_top_100["cb_customer_id"].astype(str)

    fig_cust = px.bar(df_top_100, x="cb_customer_id", y="total_transactions",
                title="En Çok Satın Alma Yapan İlk 100 Müşteri",
                hover_data=["recency", 'life_time', 'first_transaction', 'last_transaction'])
    
    branch_analys_df["cb_branch_id"] = branch_analys_df["cb_branch_id"].astype(str)

    fig_branch = px.bar(branch_analys_df, x="cb_branch_id", y="branch_transaction_count",
            title="Şubelerin satış sayısı")
    
    return fig_time, fig_cust, fig_branch



