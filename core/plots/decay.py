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

    # ===== HORIZONTAL LINE (7h) =====
    y_7 = ymax_old * (7/24)
    ax.axhline(y=y_7, linestyle="-", linewidth=1)

    # ===== FILL EACH STEP =====
    prev_day = 0  # theo dõi số ngày trước đó

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

        # ===== COLOR LOGIC =====
        if 7 <= hour < 22:
            fill_color = "lime"
        elif 0 <= hour < 7:
            fill_color = "red"
        else:
            fill_color = "orange"

        # ===== TÔ PHẦN DƯỚI =====
        ax.fill_between(x_fill, y_fill, 0, color=fill_color, alpha=1)

        # ===== TÔ PHẦN TRÊN (light blue) =====
        ax.fill_between(
            x_fill,
            y_fill,
            ymax_old,
            color="lightblue",
            alpha=1
        )

        # ===== TEXT GIỜ =====
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

        # ===== +nD LOGIC (DỰA TRÊN 24H THỰC) =====
        delta_seconds = (current_time - Time_Now).total_seconds()
        day_diff = (current_time.date() - Time_Now.date()).days

        if day_diff != prev_day:
            ax.text(
                n,
                ymax_old * 0.125,
                f"+{day_diff}D",
                ha='center',
                va='center',
                fontsize=11,
                color='blue',
                zorder=6
            )

        prev_day = day_diff

    # ===== Y SCALE =====
    ax.set_ylim(0, ymax_old * 1.05 if ymax_old > 0 else 1)
    ax.set_xlim(-0.5, max_x + 0.5)
    ax.set_xlabel("Quảng cáo")
    ax.set_yticks([])

    st.pyplot(fig)

    return []