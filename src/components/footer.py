# Created on 2023-01-29 03:35:19.083559

import dash_bootstrap_components as dbc
from dash import dcc, html


def footer():
    """
    App footer
    """
    return html.Div([
        # # # # # # # # Footer # # # # # # # #
        dbc.CardFooter(
            [
                dcc.Markdown(
                    "**HiSim-Webtool** - Based on Dash and Bootstrap",
                    style={
                        "display": "inline-block",
                        'font-size': '15px'}),
            ],
            style={'backgroundColor': 'black',
                   'textAlign': 'center',
                   'width': '100%',
                   'color': 'white',
                   'height': 'auto'},
            className='align-bottom'),
    ],
        style={
            'backgroundColor': 'black',
            'width': '100%',
    }
    )