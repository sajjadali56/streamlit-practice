import streamlit as st
import time
import pandas as pd
import numpy as np

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", "70 °F", "42 °C")
col2.metric("Wind", "9 mph", "-4 kph")
col3.metric("Humidity", "86%", "4%")
col4.metric("Pressure", "1012 hPa", "29 mm")

"Starting a long computation..."
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.01)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)

st.map(map_data)


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
    placeholder="Select an option",
    index=None,
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))

chosen = st.sidebar.radio(
    "Sorting hat",
    ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"),
    horizontal=True,
)
st.sidebar.write(f"You are in {chosen} house!")
