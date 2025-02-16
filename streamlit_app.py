import streamlit as st

import requests
import json
import os  
import time

CLIENT_ID = os.environ.get("STRAVA_CLIENT_ID")
CLIENT_SECRET = os.environ.get("STRAVA_CLIENT_SECRET")
REFRESH_TOKEN = os.environ.get("STRAVA_REFRESH_TOKEN")

CLIENT_ID = "148919"
CLIENT_SECRET = "905902bb785f877dd9e8932d19228378d6c74bc0"
REFRESH_TOKEN = "74bd46d8a7a00f5066b3f25e75e995195f6d6385"

if not all([CLIENT_ID]):
    raise ValueError("Missing Strava API credentials (CLIENT_ID).")
if not all([CLIENT_SECRET]):
    raise ValueError("Missing Strava API credentials (CLIENT_SECRET).")
if not all([REFRESH_TOKEN]):
    raise ValueError("Missing Strava API credentials (REFRESH_TOKEN).")

# --- Functions ---

def refresh_access_token():
    token_url = "https://oauth.strava.com/api/v3/oauth/token"
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'refresh_token': REFRESH_TOKEN,
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

st.title("🎈 My new Strava app")

access_token = refresh_access_token() # Get initial token
st.write(access_token)

if access_token:
    athlete_profile = get_athlete_profile(access_token)
    if athlete_profile:
        print("Athlete Profile:")
        print(json.dumps(athlete_profile, indent=4)) # Pretty print the JSON

    activities = get_activities(access_token)
    if activities:
        print("\nActivities:")
        for activity in activities:
            print(f"- {activity.get('name', 'No Name')} ({activity.get('type')})") # Safer access to name/type
else:
    print("Failed to get access token. Exiting.")


# ... process activities_last_week (default)
activities_last_week = get_activities(access_token)


st.write(
    "Hemos llegado al final! Access token: ",access_token
)
