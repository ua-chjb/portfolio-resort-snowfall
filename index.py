import dash
from dash import html, dcc, _dash_renderer
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
_dash_renderer._set_react_version("18.2.0")

import pandas as pd
from datetime import date

from charts import accum

# inplace_fig_d_geo


################################# components #######################################

Comp_A = dbc.Card(
    dbc.CardBody([
        html.H1("Annual snowfall at 4 major ski resorts, '10 to '17")
    ]), className="knucklepuck bluebirddays"
)

Comp_B = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="id_b_scattersubplots", className="id_b_scattersubplots")
    ]), className="knucklepuck"
)

# Comp_C = dbc.Card(
#     dbc.CardBody([
#         dcc.DatePickerRange(
#             start_date=date(2006, 8, 1),
#             end_date=date(2017, 8, 1),
#             min_date_allowed=date(2006, 8, 1),
#             max_date_allowed=date(2017, 8, 1),
#             id="datepicker",
#             className="datepicker"
#         )
#     ]), className="knucklepuck"
# )

Comp_C = dbc.Card(
    dbc.CardBody([    
        dmc.YearPickerInput(
            type="range",
            label=None,
            placeholder="Select year",
            minDate=date(2009, 8, 1),
            maxDate=date(2017, 8, 1),
            value=[date(2009, 8, 1), date(2017, 8, 1)],
            allowSingleDateInRange=False,
            id="datepicker",
            dropdownType="modal",
        ),
    ]), className="knucklepuck yearselectorcard"
)

Comp_E = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="id_e_bubbles", className="id_e_bubbles")
    ]), className="knucklepuck"
)

Comp_F = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="id_f_barpercentage")
    ]), className="knucklepuck"
)

Comp_G = dbc.Card(
    dbc.CardBody([
        dcc.Graph(figure={}, id="id_g_scattervs")
    ]), className="knucklepuck"
)

################################# skeleton #######################################

above = html.Div([
    html.Div([
        Comp_A,
    ], className="above_title"),
    html.Div([
        html.Div([
            Comp_B
        ], className="above_body_left"),
        html.Div([
            html.Div([
                Comp_E
            ], className="above_body_right_bottomhalf"),
            html.Div([
                Comp_C            
            ], className="above_body_right_tophalf")
        ], className="above_body_right")
    ], className="above_body")
], className="above")

below1 = html.Div([
    html.Div([
        Comp_F
    ], className="below_left"),
    html.Div([
        Comp_G
    ], className="below_right")
], className="below")

################################# final #######################################

lyt = dmc.MantineProvider([
    above,
    below1
])