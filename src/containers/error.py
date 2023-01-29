# Created on 2023-01-29 03:35:19.173279

from dash import html


def error_page(error_path: str):
    """
    Generates a 404 page which includes a link below to
    return back to /home
    """
    return html.Div(
        [
            html.Div(
                [
                    html.H1("404 - Not Found", style={"color": "white"}),
                    html.P(
                        f"{error_path} was not found.",
                        style={"font-size": "24px", "padding-bottom": "40px", 'color': 'white'}),
                    html.P(
                        f"Return to the home page by clicking the link below.",
                        style={"color": "red", "font-size": "24px"}),
                    html.A(
                        "Return to Home",
                        href="/",
                        style={"color": "red", "font-size": "24px"}),
                ],
                style={"text-align": "center", "margin-top": "50px"},
            )
        ],
        style={'height': '100vh', 'width': '100%'}
    )
