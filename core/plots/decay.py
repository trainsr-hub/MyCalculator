import streamlit as st  
from datetime import timedelta  
import numpy as np  
import matplotlib.pyplot as plt  
import math  
  
  
def plot_decay_timedelta(Time_Now, Timedeltax, max_x=7, n_times=None):  
    free_time = max(Timedeltax * 0.05, timedelta(minutes=5))  
    Timedelta = Timedeltax - free_time  
  
    x_curve1 = np.linspace(-0.5, max_x + 0.5, 400)  
    x_curve = np.floor(x_curve1)  
    x_points = np.arange(0, max_x + 1)  
  
    total_seconds = Timedelta.total_seconds()  
    total_days = total_seconds / 86400  
  
    y_curve = total_seconds * (0.9 ** np.floor(x_curve))  
    y_points = total_seconds * (0.9 ** x_points)  
  
    fig, ax = plt.subplots()  
  
    ax.plot(  
        x_curve1,  
        total_seconds * (0.9 ** (np.floor(x_curve1 + 0.5) - 0.5)),  
        drawstyle="steps-mid"  
    )  
  
    for n in range(0, max_x + 1):  
        left = max(n - 0.5, -0.5)  
        right = min(n + 0.5, max_x + 0.5)  
  
        x_fill = np.array([left, right])  
        y_fill = np.array([total_seconds * (0.9 ** (n - 0.5))] * 2)  
  
        current_seconds = total_seconds * (0.9 ** n)  
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
            total_seconds * (0.9 ** (n - 0.5)) + y_curve.max() * 0.02,  
            text_label,  
            ha='center',  
            va='center',  
            fontsize=10,  
            color='black',  
            zorder=5  
        )  
  
    ax.set_ylim(0, y_curve.max() * 1.05)  
  
    max_days = math.ceil(total_days)  
    ax.set_yticks([d * 86400 for d in range(0, max_days + 1)])  
    ax.set_yticklabels([f"{d}D" for d in range(0, max_days + 1)])  
  
    ax.set_xlim(-0.5, max_x + 0.5)  
    ax.set_xlabel("Quảng cáo")  
  
    st.pyplot(fig)  
  
    return [timedelta(seconds=s) for s in y_points]