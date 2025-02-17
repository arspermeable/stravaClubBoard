import streamlit as st
import requests

STRAVA_CLIENT_ID = st.secrets.strava.client_id
STRAVA_CLIENT_SECRET = st.secrets.strava.client_secret
STRAVA_REDIRECT_URL = st.secrets.app.url + "/return"

STRAVA_AUTHORIZATION_URL = "https://www.strava.com/oauth/authorize"

def authorization():
    from requests_oauthlib import OAuth2Session

    scope = ['read','activity:read','activity:read_all']
    stravaSession = OAuth2Session(client_id = STRAVA_CLIENT_ID, redirect_uri=STRAVA_REDIRECT_URL)
    stravaSession.scope = ["read","activity:read","activity:read_all"]
    authorization_url, state = stravaSession.authorization_url(STRAVA_AUTHORIZATION_URL)

    return authorization_url


st.set_page_config(page_title="Authorization fake")

st.markdown("# Authorization Fake")

st.write(
    """This is a fake page to simulate the authorization request to Strava."""
)

st.markdown('<a href="" target="_self">...</a>', unsafe_allow_html=True)

authorization_url = authorization()
st.link_button("Authorize Strava access",authorization_url)

