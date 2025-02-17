import streamlit as st
from streamlit_oauth import OAuth2Component
from httpx_oauth.oauth2 import OAuth2

#STRAVA_CLIENT_ID = st.secrets.strava.client_id
#STRAVA_CLIENT_SECRET = st.secrets.strava.client_secret
STRAVA_CLIENT_ID = "148919"
STRAVA_CLIENT_SECRET = "905902bb785f877dd9e8932d19228378d6c74bc0"

STRAVA_SCOPE = "read,activity:read,activity:read_all"

STRAVA_REDIRECT_URL = "https://stravaclubboard.streamlit.app/component/streamlit_oauth.authorize_button"
STRAVA_AUTHORIZE_URL = "https://www.strava.com/oauth/authorize"
STRAVA_TOKEN_URL = "https://www.strava.com/api/v3/oauth/token"
STRAVA_REFRESH_TOKEN_URL = "https://www.strava.com/api/v3/oauth/token"
STRAVA_REVOKE_TOKEN_URL = "https://www.strava.com/api/v3/oauth/deauthorize"

# --- Main Program ---

st.set_page_config(page_title="Authorization fake")

st.markdown(
    """
    # Dashboard viewer for Strava
    This is a proof of concept of a [Streamlit](https://streamlit.io/) application that implements the [Strava API](https://developers.strava.com/) OAuth2 authentication flow.
    """
)

st.write("This is a simple page to simulate the authorization request to Strava.")

stravaOauth2Session = OAuth2Component(STRAVA_CLIENT_ID, 
                                      STRAVA_CLIENT_SECRET, 
                                      STRAVA_AUTHORIZE_URL, 
                                      STRAVA_TOKEN_URL, 
                                      STRAVA_REFRESH_TOKEN_URL, 
                                      STRAVA_REVOKE_TOKEN_URL)

blocked_code = '''
stravaOauth2 = OAuth2(STRAVA_CLIENT_ID,
                      STRAVA_CLIENT_SECRET,
                      STRAVA_AUTHORIZE_URL,
                      STRAVA_TOKEN_URL,
                      refresh_token_endpoint=STRAVA_REFRESH_TOKEN_URL,
                      revoke_token_endpoint=STRAVA_REVOKE_TOKEN_URL,
                      token_endpoint_auth_method="client_secret_basic",
                      revocation_endpoint_auth_method="client_secret_basic" )
'''
result = stravaOauth2Session.authorize_button(name="Authorize", 
                                                redirect_uri=STRAVA_REDIRECT_URL, 
                                                scope=STRAVA_SCOPE,
                                                extras_params={"approval_prompt":"force"})

#if result and 'token' in result:
#    st.write(result.get('token'))
#

blocked_code = '''
# Check if token exists in session state
if 'token' not in st.session_state:
    # If not, show authorize button
    result = stravaOauth2Session.authorize_button(name="Authorize", 
                                                  redirect_uri=STRAVA_REDIRECT_URL, 
                                                  scope=STRAVA_SCOPE,
                                                  extras_params={"approval_prompt":"force"})
    st.write("fila 1")
    if result and 'token' in result:
        st.write("fila 2")
        # If authorization successful, save token in session state
        st.session_state.token = result.get('token')
        st.rerun()
else:
    # If token exists in session state, show the token
    st.write("fila 3")
    token = st.session_state['token']
    st.json(token)
    if st.button("Refresh Token"):
        st.write("fila 4")
        # If refresh token button is clicked, refresh the token
        token = stravaOauth2Session.refresh_token(token)
        st.session_state.token = token
        st.rerun()

st.write("fila 5")
'''

blocked_code = '''

import base64

import altair as alt
import streamlit as st

import strava
#from pandas.api.types import is_numeric_dtype


st.set_page_config(
    page_title="Streamlit Activity Viewer for Strava",
    page_icon=":circus_tent:",
)

strava_header = strava.header()

st.markdown(
    """
    # Streamlit oAuth2 for Strava
    I've learned this from [GitHub](https://github.com/AartGoossens/streamlit-activity-viewer) licensed under [MIT license](https://github.com/AartGoossens/streamlit-activity-viewer/blob/main/LICENSE).
    """
)

strava_auth = strava.authenticate(header=strava_header, stop_if_unauthenticated=False)

if strava_auth is None:
    st.markdown("NOT LOGGED IN.")
    st.stop()
else:
    st.markdown("This is correctly connected with Strava.")


st.write("Auth:")
st.write(strava_auth)

activity = strava.select_strava_activity(strava_auth)
data = strava.download_activity(activity, strava_auth)

'''
