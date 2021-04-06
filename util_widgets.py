from ipywidgets import interactive, widgets, Layout, GridspecLayout, Box

# form_item_layout = Layout(
#     display='flex',
#     flex_flow='row',
#     justify_content='space-between'
# )

style = {'description_width': '150px'}

##======================问题1================================
w_p0_Mechanical_Ventilation = widgets.ToggleButtons(
    options=[('not received',0), ('received',1)],
    description='Mechanical Ventilation:',
    value=0,
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    style=style, 
#     layout=form_item_layout
)

w_p0_Kcl = widgets.ToggleButtons(
    options=[('not received',0), ('received',1)],
    description='Kcl:',
    value=1,
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    style=style, 
#     layout=form_item_layout
)


w_p0_Morphine_Sulfate = widgets.ToggleButtons(
    options=[('not received',0), ('received',1)],
    description='Morphine Sulfate:',
    value=0,
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    style=style, 
#     layout=form_item_layout
)

w_p0_Cefazolin = widgets.ToggleButtons(
    options=[('not received',0), ('received',1)],
    description='Cefazolin:',
    value=0,
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    style=style, 
#     layout=form_item_layout
)

w_p0_Norepinephrine = widgets.ToggleButtons(
    options=[('not received',0), ('received',1)],
    description='Norephinephrine:',
    value=0,
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    style=style, 
#     layout=form_item_layout
)

w_p0_GCS_total = widgets.IntText(
    description='GCS total:',
    value=15,
    disabled=False,
    style=style, 
#     layout=form_item_layout
)

w_p0_sum_diagnosis = widgets.IntText(
    description='sum_diagnosis:',
    value=14,
    disabled=False,
    style=style, 
#     layout=form_item_layout
)

w_p0_Glucose_Blood = widgets.FloatText(
    description='Glucose Blood (mg/dL):',
    value=142.1,
    step=0.1,
    disabled=False,
    style=style, 
#     layout=form_item_layout
)

w_p0_Age = widgets.IntText(
    description='Age (year):',
    value=74,
    disabled=False,
    style=style, 
#     layout=form_item_layout
)

w_p0_Albumin = widgets.FloatText(
    description='Albumin (g/dL):',
    value=4.4,
    step=0.1,
    disabled=False,
    style=style, 
#     layout=form_item_layout
)

w_p0_Ca = widgets.FloatText(
    description='Ca (mg/dL):',
    value=9.8,
    step=0.1,
    disabled=False,
    style=style, 
#     layout=form_item_layout
)

w_p0_submit = widgets.Button(
    description='Submit',
    disabled=False,
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check'
)

w_p0_result = widgets.Label(value='Predicted Probability:')

w_p0_c1 = widgets.FloatSlider(
    value=0,
    min=0,
    max=1.0,
    step=0.001,
    description='Dead:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.3f',
)

w_p0_c2 = widgets.FloatSlider(
    value=0,
    min=0,
    max=1.0,
    step=0.001,
    description='FMC:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.3f',
)

w_p0_c3 = widgets.FloatSlider(
    value=0,
    min=0,
    max=1.0,
    step=0.001,
    description='Home:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.3f',
)
##======================问题2===========================

w_p1_Mechanical_Ventilation = widgets.ToggleButtons(
    options=[('not received',0), ('received',1)],
    description='Mechanical Ventilation:',
    value=0,
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    style=style, 
#     layout=form_item_layout
)

w_p1_los_hospital = widgets.FloatText(
    description='Los Hospital (day):',
    value=12.6,
    step=0.1,
    disabled=False,
    style=style, 
#     layout=form_item_layout
)


w_p1_Kcl = widgets.ToggleButtons(
    options=[('not received',0), ('received',1)],
    description='Kcl:',
    value=1,
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    style=style, 
#     layout=form_item_layout
)

w_p1_Age = widgets.IntText(
    description='Age (year):',
    value=70,
    disabled=False,
    style=style, 
#     layout=form_item_layout
)

w_p1_Morphine_Sulfate = widgets.ToggleButtons(
    options=[('not received',0), ('received',1)],
    description='Morphine Sulfate:',
    value=0,
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    style=style, 
#     layout=form_item_layout
)

w_p1_Cefazolin = widgets.ToggleButtons(
    options=[('not received',0), ('received',1)],
    description='Cefazolin:',
    value=0,
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    style=style, 
#     layout=form_item_layout
)

w_p1_Albumin = widgets.FloatText(
    description='Albumin (g/dL):',
    value=4.1,
    step=0.1,
    disabled=False,
    style=style, 
#     layout=form_item_layout
)

w_p1_GCS_Total = widgets.IntText(
    description='GCS_Total:',
    value=15,
    disabled=False,
    style=style, 
#     layout=form_item_layout
)

w_p1_BUN = widgets.FloatText(
    description='BUN (mg/dL):',
    value=27.2,
    step=0.1,
    disabled=False,
    style=style, 
#     layout=form_item_layout
)

w_p1_Fio2 = widgets.FloatText(
    description='Fio2 (%):',
    value=40.3,
    step=0.1,
    disabled=False,
    style=style, 
#     layout=form_item_layout
)


w_p1_submit = widgets.Button(
    description='Submit',
    disabled=False,
    button_style='success', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check'
)

w_p1_result = widgets.Label(value='Predicted Probability:')

w_p1_c1 = widgets.FloatSlider(
    value=0,
    min=0,
    max=1.0,
    step=0.001,
    description='Dead:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.3f',
)

w_p1_c2 = widgets.FloatSlider(
    value=0,
    min=0,
    max=1.0,
    step=0.001,
    description='FMC:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.3f',
)

w_p1_c3 = widgets.FloatSlider(
    value=0,
    min=0,
    max=1.0,
    step=0.001,
    description='Home:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.3f',
)
##======================================================
w_out = widgets.Output()

##=======================================================

   