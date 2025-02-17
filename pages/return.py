import streamlit as st
import requests

STRAVA_CLIENT_ID = st.secrets.strava.client_id
STRAVA_CLIENT_SECRET = st.secrets.strava.client_secret
STRAVA_TOKEN_URL = "https://www.strava.com/api/v3/oauth/token"

def refresh_access_token(code):
    token_url = "https://oauth.strava.com/api/v3/oauth/token"
    payload = {
        'client_id':STRAVA_CLIENT_ID,
        'client_secret': STRAVA_CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code'
    }
    try:
        response = requests.post(token_url, data=payload).json()
        access_token = response['access_token']
        refress_token = response['refresh_token']
        # Store access token securely (e.g., in a file or database)
        # For this example, we'll just return it:
        return access_token, refress_token
    except requests.exceptions.RequestException as e:
        print(f"Error refreshing token: {e}")
        raise requests.exceptions.RequestException("Error refreshing token.")
        return None  # Or raise the exception


st.set_page_config(page_title="Return fake")

st.markdown("# Return Fake")

st.write(
    """This is a fake page to simulate the return after authorization."""
)

authorization_code = st.query_params.code

if authorization_code is None:
    authorization_code = st.query_params.session

if authorization_code is None:
    st.stop()
else:
    st.write("Code:" + authorization_code)
    st.write("Scope authorized" + st.query_params["scope"])

    access_token, refress_token = refresh_access_token(authorization_code)