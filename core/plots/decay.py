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

    # ===== DECAY LAYER =====
    # y = (T * decay) - free
    y_curve = (total_seconds_original * (0.9 ** np.floor(x_curve1))) - free_seconds
    y_points = (total_seconds_original * (0.9 ** x_points)) - free_seconds

    # Clamp negative values
    y_curve = np.maximum(y_curve, 0)
    y_points = np.maximum(y_points, 0)

    total_days = y_curve.max() / 86400 if y_curve.max() > 0 else 0

    fig, ax = plt.subplots()

    # ===== STEP PLOT =====
    y_step = (
        total_seconds_original *
        (0.9 ** (np.floor(x_curve1 + 0.5) - 0.5))
    ) - free_seconds

    y_step = np.maximum(y_step, 0)

    ax.plot(x_curve1, y_step, drawstyle="steps-mid")

    # ===== FILL EACH STEP =====
    for n in range(0, max_x + 1):

        left = max(n - 0.5, -0.5)
        right = min(n + 0.5, max_x + 0.5)

        x_fill = np.array([left, right])

        current_seconds = (
            total_seconds_original * (0.9 ** n)
        ) - free_seconds

        current_seconds = max(current_seconds, 0)

        y_fill = np.array([
            (
                total_seconds_original *
                (0.9 ** (n - 0.5))
            ) - free_seconds
        ] * 2)

        y_fill = np.maximum(y_fill, 0)

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
            y_fill[0] + y_curve.max() * 0.02,
            text_label,
            ha='center',
            va='center',
            fontsize=10,
            color='black',
            zorder=5
        )

    # ===== Y SCALE =====
    ax.set_ylim(0, y_curve.max() * 1.05 if y_curve.max() > 0 else 1)

    max_days = math.ceil(total_days)

    ax.set_yticks([d * 86400 for d in range(0, max_days + 1)])
    ax.set_yticklabels([f"{d}D" for d in range(0, max_days + 1)])

    ax.set_xlim(-0.5, max_x + 0.5)
    ax.set_xlabel("Quảng cáo")

    st.pyplot(fig)

    return [timedelta(seconds=s) for s in y_points]