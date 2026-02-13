import streamlit as st
from datetime import timedelta

from utils.ui_utils import select_duration, show_boxed_text
from utils.time_utils import format_duration


def render():

    gap_duration = select_duration(2, "tab2_gap")
    st.markdown("---")

    B_duration = select_duration(3, "tab2_B")

    result1 = (max(timedelta(minutes=5), 0.95 * B_duration) + gap_duration) / 0.95

    show_boxed_text(
        "Static",
        format_duration(result1),
        "30px",
        bg_color="#008000"
    )