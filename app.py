import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader


def main():
    authenticator.logout()

    # Define the pages
    main_page = st.Page("./pages/main_page.py", title="Main Page", icon="🎈")
    page_2 = st.Page("./pages/page_2.py", title="Page 2", icon="❄️")
    page_3 = st.Page("./pages/page_3.py", title="Page 3", icon="🎉")

    # Set up navigation
    pg = st.navigation(
        [main_page, page_2, page_3],
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
        # main()
        authenticator.logout()
        st.title("Welcome *{}*".format(st.session_state.get("name")))

    elif st.session_state.get("authentication_status") is False:
        st.error("Username or password is incorrect")
    elif st.session_state.get("authentication_status") is None:
        st.warning("Please enter your username and password")
except Exception as e:
    st.error(e)
