import streamlit as st

import requests
import time

import strava

if not all([st.secrets.strava.client_id,st.secrets.strava.client_secret]):
    raise ValueError("Missing Strava API credentials.")


# --- Main Program ---

st.markdown(
    """
    # Dashboard viewer for Strava
    This is a proof of concept of a [Streamlit](https://streamlit.io/) application that implements the [Strava API](https://developers.strava.com/) OAuth2 authentication flow.
    Based on the ideas found at [Aart Goossens Github](https://github.com/AartGoossens/streamlit-activity-viewer) and is licensed under an [MIT license](https://github.com/AartGoossens/streamlit-activity-viewer/blob/main/LICENSE).

    """
)