import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from pages import statistics, segmentation

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA], suppress_callback_exceptions=True)

def layout_content():
    return html.Div(
        className="content",
        children=[
            dcc.Location(id="url", refresh=True),
            
            html.Div([
                dcc.Link('İstatistikler', href='/statistics', style={'margin-right': '20px'}),
                dcc.Link('Tahminler', href='/predictions', style={'margin-right': '20px'})
            ], style={'padding': '10px', 'background-color': '#f0f0f0', 'border-radius': '5px'}),
            
            html.Div(id="page-content"),
            
            dcc.Store(id='results-store'),
        ]
    )

layout_main = layout_content()
app.layout = html.Div([layout_main])

@app.callback(
    dash.dependencies.Output('page-content', 'children'),
    [dash.dependencies.Input('url', 'pathname')],
    prevent_initial_call=True
)
def display_page(pathname):
    if pathname == '/statistics':
        return statistics.layout
    elif pathname == '/predictions':
        return segmentation.layout()
    
if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050, debug=True)





