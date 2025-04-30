import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader


st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="My End Of Service App",
    page_icon="🎉",
    menu_items={
        "Get Help": "https://www.extremelycoolapp.com/help",
        "Report a bug": "https://www.extremelycoolapp.com/bug",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)


def main():
    authenticator.logout()

    # Define the pages
    main_page = st.Page("./routes/main_page.py", title="Main Page", icon="🎈")
    page_2 = st.Page("./routes/page_2.py", title="Page 2", icon="❄️")
    page_3 = st.Page("./routes/page_3.py", title="Page 3", icon="🎉")
    dummy = st.Page("./routes/dummy_page.py", title="ShadCN UI", icon="🎉")

    # Set up navigation
    pg = st.navigation(
        [main_page, page_2, page_3, dummy],
        expanded=True,
    )

    # Run the selected page
    pg.run()


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
