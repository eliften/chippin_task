import dash
from dash import dcc, html
import dash_table
import plotly.express as px
from models.cust_segmentation import predict_data
import middleware
import dash_bootstrap_components as dbc

time_series_df, customer_anlys_df, branch_analys_df = middleware.get_data()

data = predict_data(customer_anlys_df)


def layout():
    segment_counts = data['Segment'].value_counts().reset_index()
    segment_counts.columns = ['Segment', 'Count']

    segment_bar_chart = px.bar(
        segment_counts, 
        x='Segment', 
        y='Count', 
        title="Segmentasyon Sonuçları",
        labels={'Segment': 'Segment', 'Count': 'Firma Sayısı'},
        color='Segment'
    )
    return html.Div([
        html.H4("Segmentasyon Sonuçları"),
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id='segment-bar-chart',
                    figure=segment_bar_chart
                )])),
        dbc.Card(
            dbc.CardBody([
                dash_table.DataTable(
                    data=data.to_dict('records'),
                    columns=[{'name': col, 'id': col} for col in data.columns],
                    style_table={'height': '700px', 'overflowY': 'auto'},
                    page_size=20,
                    export_format='xlsx',
                    style_cell={'textAlign': 'left', 'fontSize': '12px'},
                    sort_action='native'
                )]))])
