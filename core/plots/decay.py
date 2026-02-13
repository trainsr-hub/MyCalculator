import streamlit as st
from datetime import timedelta
import numpy as np
import matplotlib.pyplot as plt
import math


def plot_decay_timedelta(Time_Now, Timedeltax, max_x=7, n_times=None):

    # ===== BASE VALUES =====
    free_time = max(Timedeltax * 0.05, timedelta(minutes=5))

    total_seconds_original = Timedeltax.total_seconds()
    free_seconds = free_time.total_seconds()

    x_points = np.arange(0, max_x + 1)

    # ===== OLD MAX (dùng làm chuẩn scale) =====
    y_old = (total_seconds_original * (0.9 ** x_points)) - free_seconds
    y_old = np.maximum(y_old, 0)
    ymax_old = y_old.max()

    fig, ax = plt.subplots()

    # ===== TÍNH Y MỚI CHO MỖI STEP =====
    y_steps = []

    for n in x_points:

        current_seconds = (total_seconds_original * (0.9 ** n)) - free_seconds
        current_seconds = max(current_seconds, 0)

        current_time = Time_Now + timedelta(seconds=current_seconds)

        total_minutes = current_time.hour * 60 + current_time.minute
        ratio = total_minutes / (24 * 60)

        y_new = ymax_old * ratio
        y_steps.append(y_new)

    y_steps = np.array(y_steps)

    # ===== STEP LINE =====
    ax.step(
        x_points,
        y_steps,
        where="mid"
    )

    # ===== 2 HORIZONTAL LINES =====
    y_7 = ymax_old * (7/24)

    ax.axhline(y=y_7, linestyle="-", linewidth=1)

    # ===== FILL EACH STEP =====
    for n in range(0, max_x + 1):

        left = n - 0.5
        right = n + 0.5

        y_new = y_steps[n]

        x_fill = np.array([left, right])
        y_fill = np.array([y_new, y_new])

        current_seconds = (total_seconds_original * (0.9 ** n)) - free_seconds
        current_seconds = max(current_seconds, 0)

        current_time = Time_Now + timedelta(seconds=current_seconds)
        hour = current_time.hour

        if 7 <= hour < 22:
            fill_color = "lime"
        elif 0 <= hour < 7:
            fill_color = "red"
        else:
            fill_color = "orange"

        ax.fill_between(x_fill, y_fill, 0, color=fill_color, alpha=1)

        text_label = current_time.strftime("%H:%M")

        ax.text(
            n,
            y_new + ymax_old * 0.02,
            text_label,
            ha='center',
            va='center',
            fontsize=10,
            color='black',
            zorder=5
        )

    # ===== Y SCALE =====
    ax.set_ylim(0, ymax_old * 1.05 if ymax_old > 0 else 1)
    ax.set_xlim(-0.5, max_x + 0.5)
    ax.set_xlabel("Quảng cáo")
    ax.set_yticks([])

    # ===== HATCH ZONES =====

    ax.fill_between(
        [-0.5, max_x + 0.5],
        0,
        y_7,
        hatch="/",
        facecolor="none",
        edgecolor="gray",
        linewidth=0
    )  # Vùng phía dưới 7h

    st.pyplot(fig)

    return []