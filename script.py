import streamlit_authenticator as stauth
import yaml

data: dict = {
    "credentials": {"usernames": {}},
    "cookie": {
        "expiry_days": 30,
        "key": "random_signature_key",
        "name": "random_cookie_name",
},}

accounts = {
    "jsmith": {"email": "jsmith@gmail.com", "name": "John Smith", "password": "abc123"},
    "rbriggs": {
        "email": "rbriggs@gmail.com",
        "name": "Rebecca Briggs",
        "password": "def456",
},}

hasher = stauth.Hasher()

hashed_accounts = {
    account: {
        **accounts[account],
        "password": hasher.hash(accounts[account]["password"]),
    }
    for account in accounts
}

print(hashed_accounts)

data["credentials"]["usernames"] = hashed_accounts

with open("hashed_accounts.yaml", "w") as f:

    yaml.dump(data, f)