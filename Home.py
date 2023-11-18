import streamlit as st
import plotly.graph_objects as go

st.title("Wanderlust OpenAI Recreate")

left_col,right_col=st.columns(2)

with left_col:
    st.subheader("Conversation")

with right_col:
    fig=go.Figure(go.Scattermapbox())
    fig.update_layout(
        mapbox=dict(
            accesstoken=st.secrets["MAPBOX_TOKEN"],
            center=go.layout.mapbox.Center(
            lat=st.session_state[map_state]["latitude"],
            lon=st.session_state[map_state]["longitude"],
            ),
            pitch=0,
            zoom=st.session_state[map_state]["zoom"],
        ),
        margin=dict(l=0,r=0,t=0,b=0)
    )
