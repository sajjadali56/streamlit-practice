import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader
import pandas as pd


def get_data(sheet_name: str):
    data = pd.read_excel("./budget.xlsx", sheet_name=sheet_name)
    data.dropna(inplace=True, how="all")
    data.fillna(0, inplace=True)
    return data


def main():
    authenticator.logout()
    st.write(f'Welcome *{st.session_state.get("name")}*')
    st.title("Some content")

    st.text_input("Enter any text", key="input_text")
    st.write(st.session_state.get("input_text"))

    budget = get_data("month")

    st.markdown("## Budget")
    st.write(f"{budget.iloc[3, 0]} = {budget.iloc[3,2]}")
    st.dataframe(budget)

    flat = get_data("flat")

    st.markdown("## Flat")
    st.write(f"{flat.iloc[3, 0]} = {flat.iloc[3,2]}")
    st.dataframe(flat)

    extra = get_data("extra")

    st.markdown("## Extra")
    st.dataframe(extra)


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
