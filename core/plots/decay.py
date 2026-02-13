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

    # vẫn dùng decay để tính current_time
    decay_values = total_seconds * (0.9 ** x_points)

    # y_max cũ (chuẩn tham chiếu)
    y_max_old = decay_values.max()

    y_points = []

    fig, ax = plt.subplots()

    for n, decay_sec in zip(x_points, decay_values):

        current_time = Time_Now + timedelta(seconds=decay_sec)

        # ---- PHẦN CAO ĐỘ MỚI ----
        hour_fraction = (
            current_time.hour + current_time.minute / 60
        ) / 24

        y_new = y_max_old * hour_fraction
        y_points.append(y_new)
        # -------------------------

    y_points = np.array(y_points)

    ax.step(x_points, y_points, where="mid")

    for n, y in zip(x_points, y_points):

        current_time = Time_Now + timedelta(seconds=decay_values[n])
        hour = current_time.hour

        if 7 <= hour < 22:
            fill_color = "lime"
        elif 0 <= hour < 7:
            fill_color = "red"
        else:
            fill_color = "orange"

        ax.fill_between(
            [n],
            [y],
            0,
            step="mid",
            color=fill_color,
            alpha=1
        )

        ax.text(
            n,
            y + y_points.max() * 0.02,
            current_time.strftime("%H:%M"),
            ha='center',
            va='center',
            fontsize=10,
            color='black',
            zorder=5
        )

    ax.set_ylim(0, y_points.max() * 1.05)

    ax.set_xlim(-0.5, max_x + 0.5)
    ax.set_xlabel("Quảng cáo")

    st.pyplot(fig)

    return y_points