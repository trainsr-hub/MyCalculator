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

    # Tạo các điểm nguyên
    x_points = np.arange(0, max_x + 1)
    y_points = total_seconds * (0.9 ** x_points)

    fig, ax = plt.subplots()

    # Vẽ step centered
    ax.step(x_points, y_points, where="mid")

    # Clamp bằng cách mở rộng x sang hai bên
    ax.set_xlim(-0.5, max_x + 0.5)

    for n, y in zip(x_points, y_points):

        current_seconds = y
        current_time = Time_Now + timedelta(seconds=current_seconds)
        hour = current_time.hour

        if 7 <= hour < 22:
            fill_color = "lime"
        elif 0 <= hour < 7:
            fill_color = "red"
        else:
            fill_color = "orange"

        # Fill tự động theo step-mid
        ax.fill_between(
            [n],
            [y],
            0,
            step="mid",
            color=fill_color,
            alpha=1
        )

        text_label = current_time.strftime("%H:%M")

        ax.text(
            n,
            y + y_points.max() * 0.02,
            text_label,
            ha="center",
            va="center",
            fontsize=10,
            color="black",
            zorder=5
        )

    ax.set_ylim(0, y_points.max() * 1.05)

    max_days = math.ceil(total_days)
    ax.set_yticks([d * 86400 for d in range(0, max_days + 1)])
    ax.set_yticklabels([f"{d}D" for d in range(0, max_days + 1)])

    ax.set_xlabel("Quảng cáo")

    st.pyplot(fig)

    return [timedelta(seconds=s) for s in y_points]