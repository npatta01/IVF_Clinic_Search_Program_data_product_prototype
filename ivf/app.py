import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


df = pd.read_csv('clinics.csv')

app = dash.Dash(__name__)


state = df.CurrentClinicState.unique()
state_options = list()
for i in state:
    state_options.append({'label':i, 'value':i})



app.layout = html.Div([
    html.H1('Hello Dash'),
    dcc.Dropdown(
        id ='state_dropdown',
        options=state_options,
        value='NEW YORK'
    ),




    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
     )

])

@app.callback(
    Output('table', 'data'),
    [Input('state_dropdown', 'value')])
def update_table(selected_state):
    return df[df.CurrentClinicState == selected_state].to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)