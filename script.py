import streamlit_authenticator as stauth
import yaml

data: dict = {
    "credentials": {"usernames": {}},
    "cookie": {
        "cookie_expiry_days": 30,
        "key": "random_signature_key",
        "name": "random_cookie_name",
    },
}

accounts = {
    "jsmith": {
        "email": "jsmith@gmail.com",
        "name": "John Smith",
        "first_name": "John",
        "last_name": "Smith",
        "password": "abc123",
        "logged_in": False,
    },
    "rbriggs": {
        "email": "rbriggs@gmail.com",
        "name": "Rebecca Briggs",
        "first_name": "Rebecca",
        "last_name": "Briggs",
        "password": "def456",
        "logged_in": False,
    },
}

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

with open("config.yaml", "w") as f:

    yaml.dump(data, f)
