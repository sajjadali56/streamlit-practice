import streamlit as st
from streamlit_option_menu import option_menu

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

number = st.session_state.get("my_number") or 0
st.write(f"You entered {number}")

left, right = st.columns(2)
with left:
    selected = option_menu(
        "When does the salary gets affected?",
        [
            "Beginning of the Year",
            "After 3 Months",
            "After 6 Months",
            "After 9 Months",
            "End of the Year",
        ],
        icons=[
            "calendar2-event",
            "list-task",
            "book-half",
            "layers-half",
            "calendar-check",
        ],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {
                "padding": "0!important",
            },
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            # "nav-link-selected": {"background-color": "#02ab21"},
        },
    )

    st.write(f"You selected: {selected}")

with right:
    selected = option_menu(
        "The rate at which you want to calculate the sensitivity of Model?",
        ["±1%", "±0.5%", "±0.1%", "±0.01%"],
        icons=["calendar", "list-task", "cloud-upload", "gear", "house"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        # "background-color": "#fafafa"
        styles={
            "container": {
                "padding": "0!important",
            },
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#02ab21"},
        },
    )
