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

    # ===== X DOMAIN =====
    x_curve1 = np.linspace(-0.5, max_x + 0.5, 400)
    x_points = np.arange(0, max_x + 1)

    # ===== DECAY LAYER (OLD SCALE) =====
    y_curve_old = (total_seconds_original * (0.9 ** np.floor(x_curve1))) - free_seconds
    y_curve_old = np.maximum(y_curve_old, 0)

    ymax_old = y_curve_old.max()

    fig, ax = plt.subplots()

    # ===== STEP PLOT (NEW SCALE) =====
    y_step_new = []

    for x in x_curve1:
        n = math.floor(x + 0.5) - 0.5
        current_seconds = (total_seconds_original * (0.9 ** n)) - free_seconds
        current_seconds = max(current_seconds, 0)

        current_time = Time_Now + timedelta(seconds=current_seconds)

        total_minutes = current_time.hour * 60 + current_time.minute
        ratio = total_minutes / (24 * 60)

        y_new = ymax_old * ratio
        y_step_new.append(y_new)

    ax.plot(x_curve1, y_step_new, drawstyle="steps-mid")

    # ===== FILL EACH STEP =====
    for n in range(0, max_x + 1):

        left = max(n - 0.5, -0.5)
        right = min(n + 0.5, max_x + 0.5)

        x_fill = np.array([left, right])

        current_seconds = (total_seconds_original * (0.9 ** n)) - free_seconds
        current_seconds = max(current_seconds, 0)

        current_time = Time_Now + timedelta(seconds=current_seconds)

        # ===== NEW Y CALCULATION =====
        total_minutes = current_time.hour * 60 + current_time.minute
        ratio = total_minutes / (24 * 60)
        y_new = ymax_old * ratio

        y_fill = np.array([y_new] * 2)

        # ===== COLOR LOGIC =====
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

    # ===== NEW Y SCALE =====
    ax.set_ylim(0, ymax_old * 1.05 if ymax_old > 0 else 1)

    ax.set_xlim(-0.5, max_x + 0.5)
    ax.set_xlabel("Quảng cáo")

    st.pyplot(fig)

    return []