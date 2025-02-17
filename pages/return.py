import streamlit as st

st.set_page_config(page_title="Return fake")

st.markdown("# Return Fake")

st.write(
    """This is a fake page to simulate the return after authorization."""
)

st.write(st.query_params["code"])
st.write(st.query_params["scope"])