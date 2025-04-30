import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from utils import get_data

# Main page content
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")


def main():
    # st.write("Session State:", st.session_state)
    st.write(f'Welcome *{st.session_state.get("name")}*')
    st.title("Some content")

    # st.text_input("Enter any text", key="input")
    number = st.session_state.get("my_number") or 0
    number = st.number_input(
        "Enter any number",
        key="number",
        step=1,
        min_value=0,
        max_value=100,
        value=number,
    )

    budget = get_data("month")

    if number:
        st.session_state.my_number = number

        st.write(f"You entered {number}")
        budget["New Budget"] = budget["Budget"] + st.session_state.get("number")
    # budget.sort_values("Budget", ascending=False, inplace=True)

    st.markdown("## Monthly Budget")
    st.write(f"{budget.iloc[3, 0]} = {budget.iloc[3,2]}")
    st.dataframe(budget)

    # plt.style.use("dark_background")

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

    left, right = st.columns(2)

    with left:
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

    with right:
        fig, ax = plt.subplots()
        ax = sns.barplot(
            x="Item",
            y="Budget",
            data=extra,
            palette="pastel",
        )
        ax.set(xlabel="Item", ylabel="Budget")
        plt.xticks(rotation=90)
        st.pyplot(fig)


main()
