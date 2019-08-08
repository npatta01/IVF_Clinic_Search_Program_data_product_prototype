import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import os

df = pd.read_csv('clinics.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__

    ,meta_tags=[
        # A description of the app, used by e.g.
        # search engines when displaying search results.
        {
            'name': 'description',
            'content': 'My description'
        },
        {
            'name': 'title',
            'content': 'My title'
        },
    ]

, external_stylesheets=[dbc.themes.BOOTSTRAP])







state = df.CurrentClinicState.unique()
state_options = list()
for i in state:
    state_options.append({'label':i, 'value':i})



navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Gtihub", href="https://github.com/zhannazh/IVF_Clinic_Search_Program_data_product_prototype")),

    ],
    brand="IVF",
    brand_href="#",
    sticky="top",
)


body = dbc.Container(
    [
        dbc.Row(
            dbc.Col(html.H1('Hello Dash', className="app-header--title"))
        )
        ,dcc.Markdown('''
        #### Dash and Markdown

        Dash supports [Markdown](http://commonmark.org/help).

        Markdown is a simple way to write and format text.
        It includes a syntax for things like **bold text** and *italics*,
        [links](http://commonmark.org/help), inline `code` snippets, lists,
        quotes, and more.
        ''')
        
        ,dbc.Row(
            [
                dbc.Col(dcc.Dropdown(
                    id ='state_dropdown',
                    options=state_options,
                    value='NEW YORK'
                ), width=4)

            ]
        )
        ,html.Div(className="row mt-5")


        ,dbc.Row(
                dbc.Col(dash_table.DataTable(
                    id='table',
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict('records'),
                    sort_action="native",
                    sort_mode="multi"
                ))
        )
        
    ],
    className="mt-12"
)


app.layout = html.Div([navbar, body])


@app.callback(
    Output('table', 'data'),
    [Input('state_dropdown', 'value')])
def update_table(selected_state):
    return df[df.CurrentClinicState == selected_state].to_dict('records')


if __name__ == '__main__':
    port = os.environ.get("PORT",5000)
    debug = os.environ.get("DEBUG",True)
    app.run_server(debug=debug, port=port)