import streamlit as st
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt
import math


def plot_decay_timedelta(Time_Now, Timedeltax, max_x=7, n_times=None):
    free_time = max(Timedeltax * 0.05, timedelta(minutes=5))
    Timedelta = Timedeltax - free_time

    total_seconds = Timedelta.total_seconds()
    total_days = total_seconds / 86400

    x_points = np.arange(0, max_x + 1)
    y_points = total_seconds * (0.9 ** x_points)

    y_max_old = y_points.max()

    # Tạo mảng y mới theo công thức yêu cầu
    y_scaled = []

    current_times = []

    for y in y_points:
        current_time = Time_Now + timedelta(seconds=y)
        current_times.append(current_time)

        hour_fraction = current_time.hour + current_time.minute / 60

        # ---- chỉnh cao độ theo yêu cầu ----
        new_y = y_max_old * (hour_fraction / 24)  # y mới = ymax cũ * (giờ+phút)/24
        y_scaled.append(new_y)

    y_scaled = np.array(y_scaled)

    fig, ax = plt.subplots()

    # Vẽ step với y mới
    ax.step(x_points, y_scaled, where="mid")

    for n, y_new, current_time in zip(x_points, y_scaled, current_times):

        hour = current_time.hour

        if 7 <= hour < 22:
            fill_color = "lime"
        elif 0 <= hour < 7:
            fill_color = "red"
        else:
            fill_color = "orange"

        ax.fill_between(
            [n],
            [y_new],
            0,
            step="mid",
            color=fill_color,
            alpha=1
        )

        ax.text(
            n,
            y_new + y_scaled.max() * 0.02,
            current_time.strftime("%H:%M"),
            ha='center',
            va='center',
            fontsize=10,
            color='black',
            zorder=5
        )

    ax.set_ylim(0, y_scaled.max() * 1.05)

    max_days = math.ceil(total_days)
    ax.set_yticks([d * 86400 for d in range(0, max_days + 1)])
    ax.set_yticklabels([f"{d}D" for d in range(0, max_days + 1)])

    ax.set_xlim(-0.5, max_x + 0.5)
    ax.set_xlabel("Quảng cáo x")

    st.pyplot(fig)
    st.markdown("---")

    return [timedelta(seconds=s) for s in y_points]