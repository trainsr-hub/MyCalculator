import streamlit as st
from datetime import datetime, timedelta
from .utils import format_duration, show_boxed_text, select_duration


def render(Time_Now):

    with st.expander("Start Time"):
        start_time = select_duration(3, "gap_Tatrtime")

    # xử lý start_time
    if Time_Now == Time_Now + start_time:
        # convert timedelta -> hour/minute
        total_seconds = int(start_time.total_seconds())
        start_hour = total_seconds // 3600
        start_minute = (total_seconds % 3600) // 60

        # thay giờ và phút của Time_Now
        Time_Now = Time_Now.replace(hour=start_hour, minute=start_minute)  # modified time

    # Selector chọn giờ mục tiêu
    gap_hour_str = st.selectbox(
        "Select Gap Hour",
        ["7", "22", "23"],
        key="tab2_gap_hour"
    )

    gap_day = st.number_input(
        "Gap Day",
        min_value=0,
        max_value=3,
        value=0,
        step=1,
        key="tab2_gap_day"
    )

    gap_hour = int(gap_hour_str)

    target_time = (
        Time_Now.replace(hour=gap_hour, minute=0, second=0, microsecond=0)
        + timedelta(days=gap_day)
    )

    if target_time < Time_Now:
        Time_Gap = timedelta(0)
    else:
        Time_Gap = target_time - Time_Now

    show_boxed_text(
        "Static",
        format_duration(Time_Gap / 0.95),
        "30px",
        bg_color="#008000"
    )
