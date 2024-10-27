import pandas as pd
import numpy as np
from itertools import *

import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots

from datetime import date, timedelta, datetime

from data import accum

# # # # # # # # # # # # # fig_b # # # # # # # # # # # # # # # #

from plotly.offline import *
import plotly.io as pio
from plotly.subplots import make_subplots
from itertools import *

pio.renderers.default = 'iframe'

#done

def fig_b_subplots(df1, date1, date2):

    ymask1 = ( df1["Datetime"] >= date1 )
    ymask2 = ( df1["Datetime"] <= date2 )

    accum = df1[ymask1 & ymask2]

    mask_place = ( accum["Resort"]=="jackson hole" )
    df = accum[mask_place]
    trace1 = go.Scatter(x=df["Date"], y=df["SeasonalSum"], mode="markers", marker={"color":df["Colors"], "symbol": "diamond"}, name=df["Resort"].values[0])
    
    mask_place = ( accum["Resort"]=="snowbird" )
    df = accum[mask_place]
    trace0 = go.Scatter(x=df["Date"], y=df["SeasonalSum"], mode="markers", marker={"color":df["Colors"], "symbol": "diamond"}, name=df["Resort"].values[0])
        
    mask_place = ( accum["Resort"]=="telluride" )
    df = accum[mask_place]
    trace2 = go.Scatter(x=df["Date"], y=df["SeasonalSum"], mode="markers", marker={"color":df["Colors"], "symbol": "diamond"}, name=df["Resort"].values[0])
    
    mask_place = ( accum["Resort"]=="whistler blackcomb" )
    df = accum[mask_place]
    trace3 = go.Scatter(x=df["Date"], y=df["SeasonalSum"], mode="markers", marker={"color":df["Colors"], "symbol": "diamond"}, name=df["Resort"].values[0])
    
    plots = make_subplots(rows=4, cols=1, shared_xaxes=True)
    
    plots = plots.add_trace(trace0, row=1, col=1)
    plots = plots.add_trace(trace1, row=2, col=1)
    plots = plots.add_trace(trace2, row=3, col=1)
    plots = plots.add_trace(trace3, row=4, col=1)
    plots = plots.update_yaxes({"range":[-400, 1900]}).update_layout({
        "legend": {"orientation": "h", "y": 1.25, "x": 0.4}, 
        "title": "Snowfall, across resorts, across time",
        "clickmode": "select"
    })
    
    return plots
fig_b_subplots(accum, "2009-10-01", "2018-04-08")

# # # # # # # # # # # # # fig_d # # # # # # # # # # # # # # # #
# def inplace_fig_d_geo():
    
#     fig = px.scatter_geo(accum, lat="Latitude", lon="Longitude", scope="world", color="Resort", color_discrete_sequence=px.colors.sequential.Blues[4:])
#     fig.update_geos({
#         "projection" :{"type": "orthographic", 
#         "distance": 1.5,
#         "rotation": {"lat":40, "lon": -110}},
#         "showcountries":True, 
#         "countrycolor":"Black",
#     }).update_layout({
#         "legend": {"visible": False},
#         "margin":{"r":0,"t":0,"l":0,"b":0}
#     })

#     return fig

# inplace_fig_d_geo()

# # # # # # # # # # # # # fig_e # # # # # # # # # # # # # # # #

# done

def fig_e_balls(df1, date1, date2):
    
    ymask1 = ( df1["Datetime"] >= date1 )
    ymask2 = ( df1["Datetime"] <= date2 )

    gb = df1.groupby(["Resort"]).agg({"SeasonalSum": "sum", "Colors": "min"}).reset_index()
    gb["column"] = [1, 2, 1, 2]
    gb["row"] = [1, 1, 2, 2]

    cd = pd.concat([pd.Series(gb["Resort"]), pd.Series(gb["SeasonalSum"])], axis=1)
    
    trace = go.Scatter(
        x=gb["column"],
        y=gb["row"],
        mode="markers",
        marker={"size": gb["SeasonalSum"] / 5000, "color": gb["Colors"]},
        name="",
        customdata=cd,
        hovertemplate=
        "Resort: %{customdata[0]}" +
        "<br>Total Snowfall: %{customdata[1]}"
    )        

    fig = go.Figure(trace).update_layout({
        "xaxis": {"showticklabels": False, "range": [0, 3]}, 
        "yaxis": {"showticklabels": False, "range":[0, 3]}, 
        "clickmode": "select",
        "title": "Total snowfall as size"
    })
    
    return fig


# # # # # # # # # # # # # fig_f # # # # # # # # # # # # # # # #
def fig_f_bar(df1, date1, date2):

    mask1 = ( df1["Datetime"] >= date1 )
    mask2 = ( df1["Datetime"] <= date2 )
    
    df = df1[mask1 & mask2]
    
    gb = accum.groupby(["Resort"]).agg({"Total": "sum"}).reset_index()
    gb = gb.sort_values(by="Resort", ascending=True)
    fig= px.bar(gb, x="Resort", y="Total", color="Resort", color_discrete_sequence=px.colors.sequential.Blues[4:]).update_layout({"clickmode": "select"})
    return fig.update_layout({"title": "Total snowfall, all years", 
                              "yaxis": {"title": "Snowfall (cm)"}, 
                              "xaxis": {"showticklabels": False},
                              "legend": {"visible": False},
                            })



# # # # # # # # # # # # # fig_g # # # # # # # # # # # # # # # #

# date2 = pd.to_datetime("2017-08-01")

# from datetime import date, timedelta, datetime

# date1 = pd.to_datetime("2008-08-01")
# date2 = pd.to_datetime("2017-08-01")

def fig_g_messyscatter(df, date2):
    
    season1 = datetime(pd.to_datetime(date2).year, 8, 1) - timedelta(365)
    season2 = datetime(pd.to_datetime(date2).year, 8, 1)
    

    smask1 = ( df["Datetime"] >= str(season1) )
    smask2 = ( df["Datetime"] <= str(season2) )
    df = df[smask1 & smask2]        
    fig = px.scatter(x=df["Datetime"], y=df["SeasonalSum"], color=df["Resort"], symbol_sequence=["diamond"], color_discrete_sequence=px.colors.sequential.Blues[4:])

    return fig.update_layout({
        "title": "Snowfall across time, most recent season",
        "xaxis": {"title": "Date"},
        "yaxis": {"title": "Aggregate snowfall (cm)"},
        "legend": {"title": "Resort"}
    })

# fig_g_messyscatter(accum, date2)