import streamlit as st
from streamlit_oauth import OAuth2Component
#from myoauth import OAuth2Component

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
                                      STRAVA_REVOKE_TOKEN_URL,
                                      token_endpoint_auth_method = "client_secret_post",
                                      revocation_endpoint_auth_method = "client_secret_post")

# Check if token exists in session state
if 'token' not in st.session_state:
    # If not, show authorize button
    st.write("You are not authorized. Press button to proceed.")
    result = stravaOauth2Session.authorize_button(name="Authorize", 
                                                  redirect_uri=STRAVA_REDIRECT_URL, 
                                                  scope=STRAVA_SCOPE,
                                                  extras_params={"approval_prompt":"force"})
    if result and 'token' in result:
        st.write(result)
        # If authorization successful, save token in session state
        st.session_state.token = result.get('token')
        st.rerun()
else:
    # If token exists in session state, show the token
    token = st.session_state['token']
    #st.json(token)
    st.write("You are authorized until " + token.expires_at)
    st.write(token.athlete.firstname + " " + token.athlete.lastname)
    if st.button("Refresh Token"):
        st.write("fila 4")
        # If refresh token button is clicked, refresh the token
        token = stravaOauth2Session.refresh_token(token)
        st.session_state.token = token
        st.rerun()
