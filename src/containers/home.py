# Created on 2023-01-29 03:35:19.190829

import dash_bootstrap_components as dbc
from dash import html, Dash, dcc
import platform
import datetime


def forms():
    """
    Generates user input forms for upload screen
    """

    calculation = dbc.Row(
        [
            dbc.Label("Calculation", html_for="calculation-select", width=3),
            dbc.Col(
                dbc.Select(
                    id='calculation-select',
                    value=1,
                    options=[
                        {"label": "Optimize Energy Costs", "value": 1},
                        {"label": "Optimize Greenhouse Gas Emissions", "value": 2},
                    ],
                ),
                width=9,
            ),
        ],
        className="mb-2 form-item",
    )

    location = dbc.Row(
        [
            dbc.Label("Location",
                      html_for="location-input", width=3),
            dbc.Col(
                dbc.Input(
                    id="location-input",
                    placeholder="Address",
                    autocomplete='on',
                    value="Sample Street No 1, 12345 Berlin",
                    style={
                        'lineHeight': '1px',
                        'minHeight': '1px',
                        'fontWeight': '100',
                        'borderStyle': 'solid',
                        'borderRadius': '0.25rem',
                    }
                ),
                width=9,
            ),
        ],
        className="mb-2 form-item",
    )

    return dbc.Form([location, calculation])


def home_page(app: Dash):
    """
    Main landing page for hisim-webtool-template
    """

    return html.Div([

        html.Div([
            html.Div([
                # Text and Titles
                html.H3(
                    "HiSim-Webtool",
                    style={'padding-top': '10px'},
                ),
                html.H5([
                    "Digital Energy Consulting"
                ], style={'margin-bottom': '0px'}),
                html.Hr(style={'color': 'black',
                               'margin-top': '0px', 'margin-bottom': '30px'}),

                # Application Details
                forms(),

                html.Div(id='call-status-text'),
                html.Div([
                    dbc.Button(
                        [
                            html.P("Show me the results", style={
                                   'display': 'inline-block', 'height': '0px'}),
                        ],
                        id='send-call-button',
                        className="uploadButton",
                        type="button",
                    ),
                ], style={
                    'width': '100%',
                    'display': 'flex',
                    'justify-content': 'center',
                    'margin-top': '30px',
                },
                    id="upload-button-container"),
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