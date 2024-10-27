from dash import Input, Output

from data import accum
from charts import fig_b_subplots, fig_e_balls, fig_g_messyscatter, fig_f_bar

def callbacks_baby(app):
    @app.callback(
        Output(component_id="id_b_scattersubplots", component_property="figure"),
        Output(component_id="id_e_bubbles", component_property="figure"),
        Output(component_id="id_f_barpercentage", component_property="figure"),
        Output(component_id="id_g_scattervs", component_property="figure"),
        Input(component_id="datepicker", component_property="value")
        # Input(component_id="datepicker", component_property="start_date"),
        # Input(component_id="datepicker", component_property="end_date")
    )
    def hagrids_hut(value):
        date1 = value[0]
        date2 = value[1]
        print("start is", date1)
        print("end is ", date2)
        return fig_b_subplots(accum, date1, date2), fig_e_balls(accum, date1, date2), fig_f_bar(accum, date1, date2), fig_g_messyscatter(accum, date2)