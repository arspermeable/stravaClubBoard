import streamlit as st

def authenticate(header=None, stop_if_unauthenticated=True):
    query_params = st.experimental_get_query_params()
    authorization_code = query_params.get("code", [None])[0]

    if authorization_code is None:
        authorization_code = query_params.get("session", [None])[0]

    if authorization_code is None:
        if stop_if_unauthenticated:
            st.stop()
        return
    else:
        strava_auth = exchange_authorization_code(authorization_code)
        st.experimental_set_query_params(session=authorization_code)

        return strava_auth


st.set_page_config(page_title="Return fake")

st.markdown("# Return Fake")

st.write(
    """This is a fake page to simulate the return after authorization."""
)

st.write(st.query_params["code"])
st.write(st.query_params["scope"])