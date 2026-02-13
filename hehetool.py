import streamlit as st  
from datetime import timedelta, datetime  # ← thêm dòng này để dùng timedelta  
import numpy as np  
import matplotlib.pyplot as plt  
from hehetool import plot_decay_timedelta

Time_Now = datetime.now() + timedelta(hours=7)  # current time + 7 hours



def plot_decay_timedelta(Timedeltax, max_x=7, n_times=None):
    global Time_Now
    free_time = max(Timedeltax * 0.05, timedelta(minutes=5))
    Timedelta = Timedeltax - free_time

    # ===== TẠO X LINSPACE MỊN =====
    x_curve1 = np.linspace(-0.5, max_x + 0.5, 400)
    x_curve = np.floor(x_curve1)
    x_points = np.arange(0, max_x + 1)

    total_seconds = Timedelta.total_seconds()
    total_days = total_seconds / 86400

    y_curve = total_seconds * (0.9 ** np.floor(x_curve))
    y_points = total_seconds * (0.9 ** x_points)

    fig, ax = plt.subplots()

    # ===== PRECOMPUTE STEP DATA =====
    step_data = []

    for n in range(0, max_x + 1):

        left = max(n - 0.5, -0.5)
        right = min(n + 0.5, max_x + 0.5)

        digital_height = total_seconds * (0.9 ** (n - 0.5))
        current_seconds = total_seconds * (0.9 ** n)
        current_time = Time_Now + timedelta(seconds=current_seconds)

        hour = current_time.hour

        if 7 <= hour < 22:
            fill_color = "lime"
        elif 0 <= hour < 7:
            fill_color = "red"
        else:
            fill_color = "orange"

        step_data.append({
            "n": n,
            "left": left,
            "right": right,
            "height": digital_height,
            "current_time": current_time,
            "fill_color": fill_color
        })

    # ===== VẼ ĐƯỜNG MƯỢT =====
    ax.plot(
        x_curve1,
        total_seconds * (0.9 ** (np.floor(x_curve1 + 0.5) - 0.5)),
        drawstyle="steps-mid"
    )

    # ===== TÔ + TEXT =====
    for step in step_data:

        x_fill = np.array([step["left"], step["right"]])
        y_fill = np.array([step["height"]] * 2)

        ax.fill_between(
            x_fill,
            y_fill,
            0,
            color=step["fill_color"],
            alpha=1
        )

        text_label = step["current_time"].strftime("%H:%M")

        ax.text(
            step["n"],
            step["height"] + y_curve.max() * 0.02,
            text_label,
            ha='center',
            va='center',
            fontsize=10,
            color='black',
            zorder=5
        )

    # ===== NEW SCALED STEP PLOT =====
    ymax_old = y_curve.max()
    scaled_y = []

    for step in step_data:
        ct = step["current_time"]
        total_minutes = ct.hour * 60 + ct.minute
        scale_factor = total_minutes / (24 * 60)
        scaled_y.append(ymax_old * scale_factor)

    scaled_y = np.array(scaled_y)

    ax.plot(
        x_points,
        scaled_y,
        drawstyle="steps-mid",
        linestyle="--"
    )

    # ===== AUTO SCALE Y =====
    ax.set_ylim(0, y_curve.max() * 1.05)

    import math
    max_days = math.ceil(total_days)

    ax.set_yticks([d * 86400 for d in range(0, max_days + 1)])
    ax.set_yticklabels([f"{d}D" for d in range(0, max_days + 1)])

    for d in range(1, max_days + 1):
        ax.hlines(
            d * 86400,
            -0.5,
            min(
                math.log((d * 86400) / total_seconds) / math.log(0.9),
                max_x + 0.5
            ),
            linestyles="solid",
            color="black",
            alpha=0
        )

    ax.set_xlim(-0.5, max_x + 0.5)
    ax.set_xlabel("Quảng cáo")

    st.pyplot(fig)

    return [timedelta(seconds=s) for s in y_points]