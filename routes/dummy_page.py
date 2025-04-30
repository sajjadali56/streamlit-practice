import streamlit as st
import streamlit_shadcn_ui as ui

from utils import get_data

st.markdown("# ShadCN UI ❄️")
col1, col2 = st.columns([1, 3])
with col1:
    ui.avatar(
        src="https://images.unsplash.com/photo-1633332755192-727a05c4013d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80",
    )

with col2:
    ui.tabs(
        ["Tab 1", "Tab 2", "Tab 3"],
        default_value="Tab 1",
    )


import streamlit_shadcn_ui as ui

ui.badges(
    badge_list=[
        ("default", "default"),
        ("secondary", "secondary"),
        ("outline", "outline"),
        ("Hello", "destructive"),
        ("World", "destructive"),
    ],
    class_name="flex gap-2",
    key="badges1",
)

clicked = ui.button("Button", variant="destructive", size="lg", full_width=True)

st.write("Button clicked", clicked)

ui.checkbox(default_checked=True, label="I am a Checkbox 1")

col1, col2, col3, col4 = st.columns(4)

metricValues = [
    ("Temperature", "70 °F", "42 °C"),
    ("Wind", "9 mph", "-4 kph"),
    ("Humidity", "86%", "4%"),
    ("Pressure", "1012 hPa", "29 mm"),
]

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        ui.metric_card(
            title=metricValues[i][0],
            content=metricValues[i][1],
            description=metricValues[i][2],
        )

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        st.metric(
            label=metricValues[i][0],
            value=metricValues[i][1],
            delta=metricValues[i][2],
        )

ui.date_picker("Date picker", mode="single")
st.date_input("Date input", value=None, min_value=None, max_value=None, key=None)


budget = get_data("month")
ui.table(budget)
