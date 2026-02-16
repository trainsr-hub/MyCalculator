import streamlit as st
from datetime import timedelta, datetime
from .utils import (
    select_duration,
    format_duration,
    show_boxed_text,
    plot_decay_timedelta
)

def render(Time_Now):
    duration = select_duration(3, "hatchingtime")
    default_ads = 7 if duration >= timedelta(days=5) else 0  # 7 when duration ≥ 5 days, otherwise 0

    if duration != timedelta(0):
        ads = st.number_input("🎬 Ads", min_value=0, value=default_ads, max_value=10, step=1)
    else:
        ads = 1

    Now_Time = duration * 0.9**ads
    Free_Time = max(duration * 0.05, timedelta(minutes=5))
    Timer = max(timedelta(0), Now_Time - Free_Time)

    col1, col2 = st.columns(2)

    finish_time = Time_Now + Timer
    colorfree = "#008000" if datetime(1,1,1,7).time() <= finish_time.time() <= datetime(1,1,1,22).time() else "#FF0000"

    finish_at = finish_time.strftime("%I:%M %p") + (
        f" + {(finish_time.date() - Time_Now.date()).days} Days"
        if finish_time.date() != Time_Now.date() else ""
    )

    with col1:
        show_boxed_text("Duration", format_duration(Now_Time), "30px", bg_color="#0000ff")

    with col2:
        show_boxed_text("Timer", format_duration(Timer), "30px", bg_color="#8f8f8f")

    plot_decay_timedelta(Time_Now, Timedeltax=duration, max_x = max(7, ads),n_times=0)

    show_boxed_text("Free", f"{format_duration(Free_Time)}", "30px", bg_color=colorfree, description=finish_at)