import streamlit as st
from datetime import datetime, timedelta

from utils.ui_utils import select_duration, show_boxed_text
from utils.time_utils import format_duration
from utils.plot_utils import plot_decay_timedelta


def render():

    time_now = datetime.now() + timedelta(hours=7)

    duration = select_duration(3, "hatchingtime")

    if duration != timedelta(0):
        ads = st.number_input("🎬 Ads", min_value=0, value=0, max_value=10, step=1)
    else:
        ads = 1

    now_time = duration * 0.9**ads
    free_time = max(duration * 0.05, timedelta(minutes=5))
    timer = max(timedelta(0), now_time - free_time)

    col1, col2 = st.columns(2)

    finish_time = time_now + timer
    finish_at = finish_time.strftime("%I:%M %p")

    with col1:
        show_boxed_text("Duration", format_duration(now_time), "30px", bg_color="#0000ff")

    with col2:
        show_boxed_text("Timer", format_duration(timer), "30px", bg_color="#8f8f8f")

    plot_decay_timedelta(duration, time_now)