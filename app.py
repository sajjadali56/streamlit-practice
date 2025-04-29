import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np


def get_data(sheet_name: str):
    data = pd.read_excel("./budget.xlsx", sheet_name=sheet_name)
    data.dropna(inplace=True)
    data.fillna(0, inplace=True)
    return data


def main():
    authenticator.logout()

    st.write("Session State:", st.session_state)

    import time

    "Starting a long computation..."

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f"Iteration {i+1}")
        bar.progress(i + 1)
        time.sleep(0.1)

    st.write(f'Welcome *{st.session_state.get("name")}*')
    st.title("Some content")

    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
    )

    st.map(map_data)

    x = st.slider("x")  # 👈 this is a widget
    st.write(x, "squared is", x * x)

    # Add a selectbox to the sidebar:
    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
    )

    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))

    chosen = st.sidebar.radio(
        "Sorting hat",
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"),
        horizontal=True,
    )
    st.sidebar.write(f"You are in {chosen} house!")

    st.text_input("Enter any text", key="input")
    st.write(st.session_state.get("input"))

    budget = get_data("month")
    # budget.sort_values("Budget", ascending=False, inplace=True)

    st.markdown("## Monthly Budget")
    st.write(f"{budget.iloc[3, 0]} = {budget.iloc[3,2]}")
    st.dataframe(budget)

    # sns plot here for Item agains Budget
    left, right = st.columns(2)

    fig, ax = plt.subplots()
    ax = sns.barplot(
        x="Item",
        y="Budget",
        data=budget,
        palette="pastel",
    )
    ax.set(xlabel="Item", ylabel="Budget")
    plt.xticks(rotation=90)
    left.pyplot(fig)

    fig, ax = plt.subplots()
    ax = plt.pie(
        budget["Budget"],
        labels=budget["Item"].values,
        autopct="%1.1f%%",
        colors=sns.color_palette("pastel"),
    )
    right.pyplot(fig)

    flat = get_data("flat")

    st.markdown("## Flat")
    st.write(f"{flat.iloc[3, 0]} = {flat.iloc[3,2]}")
    st.dataframe(flat)

    extra = get_data("extra")

    st.markdown("## Extra")
    st.dataframe(extra)

    explode = [0.1, 0, 0, 0, 0]
    fig, ax = plt.subplots()
    ax = plt.pie(
        extra["Budget"],
        labels=extra["Item"].values,
        explode=explode,
        autopct="%1.1f%%",
        colors=sns.color_palette("pastel"),
    )
    st.pyplot(fig)


with open("./config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)


authenticator = Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["cookie_expiry_days"],
)

try:
    res = authenticator.login()

    if st.session_state.get("authentication_status"):
        main()
    elif st.session_state.get("authentication_status") is False:
        st.error("Username or password is incorrect")
    elif st.session_state.get("authentication_status") is None:
        st.warning("Please enter your username and password")
except Exception as e:
    st.error(e)
