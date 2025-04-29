import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


excel = pd.ExcelFile("./budget.xlsx")


def get_data(sheet_name: str):
    data = pd.read_excel(excel, sheet_name=sheet_name)
    data.dropna(inplace=True)
    data.fillna(0, inplace=True)
    return data


# Main page content
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")


def main():
    # st.write("Session State:", st.session_state)
    st.write(f'Welcome *{st.session_state.get("name")}*')
    st.title("Some content")

    # st.text_input("Enter any text", key="input")
    number = st.number_input("Enter any number", key="number", step=1)

    st.write(f"You entered {number}")

    budget = get_data("month")
    budget["New Budget"] = budget["Budget"] + st.session_state.get("number")
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


main()
