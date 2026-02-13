import streamlit as st
from datetime import timedelta

def select_duration(num_selectors, key_prefix):

    cols = st.columns(num_selectors)
    days = 0

    if num_selectors == 3:
        with cols[0]:
            days = st.selectbox(
                "📅 Days",
                options=list(range(7, -1, -1)),
                index=7,
                key=f"{key_prefix}_days"
            )

        with cols[1]:
            hours = st.selectbox(
                "⏰ Hours",
                options=list(range(24, -1, -1)),
                index=24,
                key=f"{key_prefix}_hours"
            )

        with cols[2]:
            minutes = st.selectbox(
                "⏱️ Minutes",
                options=list(range(60, -1, -1)),
                index=60,
                key=f"{key_prefix}_minutes"
            )

    elif num_selectors == 2:
        with cols[0]:
            hours = st.selectbox(
                "⏰ Hours",
                options=list(range(24, -1, -1)),
                index=24,
                key=f"{key_prefix}_hours"
            )

        with cols[1]:
            minutes = st.selectbox(
                "⏱️ Minutes",
                options=list(range(60, -1, -1)),
                index=60,
                key=f"{key_prefix}_minutes"
            )

    else:
        raise ValueError("num_selectors must be 2 or 3")

    return timedelta(days=days, hours=hours, minutes=minutes)