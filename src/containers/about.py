# Created on 2023-01-29 03:35:19.159512

import dash_bootstrap_components as dbc
from dash import html, Dash


def about_page(app: Dash):
    """
    About Page for hisim-webtool
    """

    return html.Div([

        html.Div([
            html.Div([
                # Text and Titles
                html.H3(
                    "About Page",
                    style={'padding-top': '10px'},
                ),
                html.H5([
                    "Space for explanation, description, references, etc",
                ], style={'margin-bottom': '0px'}),
                html.Hr(style={'color': 'black',
                               'margin-top': '0px', 'margin-bottom': '30px'}),

                html.Div(id='not-used'),
                html.Div([
                    dbc.Button(
                        [
                            html.P("Back to start...", style={
                                   'display': 'inline-block', 'height': '0px'}),
                        ],
                        id='about-page-button',
                        href='/',
                        className="uploadButton",
                        type="button",
                    ),
                ], style={
                    'width': '100%',
                    'display': 'flex',
                    'justify-content': 'center',
                    'margin-top': '30px',
                },
                    id="about-button"),
            ],
                style={
                    'min-width': '400px',
                    'margin-bottom': '10px',
                    'color': '#444',
                    'padding-bottom': '100px'
            }),
        ],
            style={
                'width': '70%',
        },
            className='center'
        ),
    ],
        style={
            'padding-top': '10px',
            'margin-bottom': '60px',
            'min-height': '100vh',
    },
    )