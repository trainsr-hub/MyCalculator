import streamlit as st
from datetime import datetime, timedelta
from .utils import format_duration, show_boxed_text


def render(Time_Now):
    # Selector chọn giờ mục tiêu
    gap_hour_str = st.selectbox(
        "Select Gap Hour",
        ["7", "22", "23"],
        key="tab2_gap_hour"
    )

    # Input số ngày cộng thêm
    gap_day = st.number_input(
        "Gap Day",
        min_value=0,
        max_value=3,
        value=0,
        step=1,
        key="tab2_gap_day"
    )

    gap_hour = int(gap_hour_str)  # convert string sang int

    # Tạo mốc thời gian mục tiêu
    target_time = (
        Time_Now.replace(hour=gap_hour, minute=0, second=0, microsecond=0)
        + timedelta(days=gap_day)
    )

    # Nếu target_time thuộc quá khứ (cùng ngày nhưng giờ đã qua)
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