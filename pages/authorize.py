import streamlit as st
from streamlit_oauth import OAuth2Component

STRAVA_CLIENT_ID = st.secrets.strava.client_id
STRAVA_CLIENT_SECRET = st.secrets.strava.client_secret

STRAVA_SCOPE = "read,activity:read,activity:read_all"

STRAVA_REDIRECT_URL = st.secrets.app.url + "/return"
STRAVA_AUTHORIZATION_URL = "https://www.strava.com/oauth/authorize"
STRAVA_TOKEN_URL = STRAVA_REFRESH_TOKEN_URL = STRAVA_REVOKE_TOKEN_URL = "https://www.strava.com/api/v3/oauth/token"

st.set_page_config(page_title="Authorization fake")

stravaOauth2Session = OAuth2Component(STRAVA_CLIENT_ID, 
                                      STRAVA_CLIENT_SECRET, 
                                      STRAVA_AUTHORIZATION_URL, 
                                      STRAVA_TOKEN_URL, 
                                      STRAVA_REFRESH_TOKEN_URL, 
                                      STRAVA_REVOKE_TOKEN_URL)
st.markdown("# Authorization Fake")

st.write(
    """This is a fake page to simulate the authorization request to Strava."""
)

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
        # st.session_state.token = result.get('token')
        st.rerun()
else:
    # If token exists in session state, show the token
    token = st.session_state['token']
    st.json(token)
    if st.button("Refresh Token"):
        # If refresh token button is clicked, refresh the token
        token = stravaOauth2Session.refresh_token(token)
        st.session_state.token = token
        st.rerun()
