import streamlit as st

import requests
import json
import os  
import time

import strava

if not all([st.secrets.strava.client_id,st.secrets.strava.client_secret]):
    raise ValueError("Missing Strava API credentials.")

CLIENT_ID = st.secrets.strava.client_id 
CLIENT_SECRET = st.secrets.strava.client_secret

# --- Functions ---

def refresh_access_token():
    token_url = "https://oauth.strava.com/api/v3/oauth/token"
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        # 'refresh_token': REFRESH_TOKEN,
        'grant_type': 'refresh_token'
    }
    try:
        response = requests.post(token_url, data=payload).json()
        access_token = response['access_token']
        # Store access token securely (e.g., in a file or database)
        # For this example, we'll just return it:
        return access_token
    except requests.exceptions.RequestException as e:
        print(f"Error refreshing token: {e}")
        raise requests.exceptions.RequestException("Error refreshing token.")
        return None  # Or raise the exception


def get_athlete_profile(access_token):
    api_url = "https://www.strava.com/api/v3/athlete"
    headers = {"Authorization": f"Bearer {access_token}"}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting athlete profile: {e}")
        return None

def get_activities(access_token, after=None, before=None):  # Add after/before if needed
    api_url = "https://www.strava.com/api/v3/athlete/activities"
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {}  # Add after/before parameters here if needed

    if not all([after,before]):
        # Defaults to one week since now:
        now = int(time.time())
        params['before']= now
        params['after'] = now - (7 * 24 * 60 * 60) # 7 days ago
    else:
        if after:
            params['after'] = after
        if before:
            params['before'] = before

    try:
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting activities: {e}")
        return None

# --- Main Program ---

st.markdown(
    """
    # Dashboard viewer for Strava
    This is a proof of concept of a [Streamlit](https://streamlit.io/) application that implements the [Strava API](https://developers.strava.com/) OAuth2 authentication flow.
    Based on the ideas found at [Aart Goossens Github](https://github.com/AartGoossens/streamlit-activity-viewer) and is licensed under an [MIT license](https://github.com/AartGoossens/streamlit-activity-viewer/blob/main/LICENSE).

    """
)

strava_auth = strava.authenticate(header=Nune, stop_if_unauthenticated=False)
# header=strava_header

if strava_auth is None:
    st.markdown("Click the \"Connect with Strava\" button at the top to login with your Strava account and get started.")
    st.stop()


st.write(
    "Hemos llegado al final! strava client_id: ",CLIENT_ID
)
