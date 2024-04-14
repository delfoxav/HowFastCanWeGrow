from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
from src.utils import Individual
import dash
import numpy as np

#TODO make full pictures when the individual is fully changed


app = Dash(__name__)
individual = Individual(0.1,1, True)

update_flag = False

app.layout = html.Div([
    html.H1("How fast Could you become a new person?"),
    html.H2("Parameter Configuration"),
    html.Div([
        html.Label("Change Probability:"),
        dcc.Input(id='change-probability', type='number', value=0.1, step=0.01),
    ]),
    html.Div([
        html.Label("Number of Change Percent:"),
        dcc.Input(id='num-change-percent', type='number', value=1, min=1, max=99, step=1),
    ]),
    html.Div([
        html.Label("Change to Random:"),
        dcc.RadioItems(
            id='change-to-random',
            options=[
                {'label': 'True', 'value': True},
                {'label': 'False', 'value': False}
            ],
            value=True,
        ),
    ]),
    html.Button('Start', id='start-button', n_clicks=0),
    html.Button('Stop', id='stop-button', n_clicks=0),
    html.Button('Reset', id='reset-button', n_clicks=0),
    dcc.Graph(id="live-update-graph"),
    dcc.Interval(
        id='interval-component',
        interval=200,  # in milliseconds
        n_intervals=0
    )
])

@app.callback(
    Output("live-update-graph", "figure"),
    Output("interval-component", "disabled"),
    Input("interval-component", "n_intervals"),
    Input("start-button", "n_clicks"),
    Input("stop-button", "n_clicks"),
    Input("reset-button", "n_clicks"),
    State("change-probability", "value"),
    State("num-change-percent", "value"),
    State("change-to-random", "value"))
def update_plot(n_intervals, start_clicks, stop_clicks, reset_clicks, change_probability, num_change_percent, change_to_random):
    global individual, heatmap_data, cmap, update_flag
    
    ctx = dash.callback_context
    if not ctx.triggered:
        return dash.no_update, dash.no_update

    if ctx.triggered[0]['prop_id'] == 'start-button.n_clicks':
        if individual is None:
            individual = Individual(change_probability, num_change_percent, change_to_random)
        if individual.change_probability != change_probability or individual.nb_change_percent != num_change_percent or individual.change_to_random != change_to_random:
            individual = Individual(change_probability, num_change_percent, change_to_random)
        heatmap_data = individual.state.reshape(10, 10).astype(str)
        cmap = 'Viridis' if individual.change_to_random else ['red', 'blue']
        update_flag = True
        return px.imshow(heatmap_data, color_continuous_scale=cmap).update_layout(title=f"Day {individual.days}",), False

    if ctx.triggered[0]['prop_id'] == 'reset-button.n_clicks':
        individual.reset()
        heatmap_data = individual.state.reshape(10, 10).astype(str)
        cmap = 'Viridis' if individual.change_to_random else ['red', 'blue']
        update_flag = False
        return px.imshow(heatmap_data, color_continuous_scale=cmap).update_layout(title=f"Day {individual.days}", coloraxis_showscale=False), True

    if ctx.triggered[0]['prop_id'] == 'stop-button.n_clicks':
        update_flag = False
        return dash.no_update, True

    if update_flag:
        individual.change()
        heatmap_data = individual.state.reshape(10, 10).astype(str)
        return px.imshow(heatmap_data, color_continuous_scale=cmap).update_layout(title=f"Day {individual.days}", coloraxis_showscale=False), False

    # stop when the individual is fully different
    if not np.any(individual.state == 1):
        update_flag = False
        return px.imshow(heatmap_data, color_continuous_scale=cmap).update_layout(title="You are now a totally new person"), True
    return dash.no_update, True

if __name__ == '__main__':
    app.run_server(debug=True)
