import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Health - Minutes Calculator")

data = []
index = 0

# ===== Dynamic Input Loop =====
while True:
    col1, col2 = st.columns(2)

    with col1:
        health = st.number_input(
            "Health",
            min_value=0,
            step=1,
            key=f"health_{index}"
        )

    with col2:
        minutes = st.number_input(
            "Minutes",
            min_value=0,
            step=1,
            key=f"minutes_{index}"
        )

    if health != 0 and minutes != 0:
        data.append((health, minutes))
        index += 1
    else:
        break  # stop loop when one equals 0


# ===== Calculation & Visualization =====
if data:

    max_values = []
    min_values = []

    for health, minutes in data:
        if minutes - 1 == 0 or minutes + 1 == 0:
            st.write("Không hợp lệ")
            st.stop()

        max_values.append(health / (minutes - 1))
        min_values.append(health / (minutes + 1))

    max_val = min(max_values)
    min_val = max(min_values)

    if min_val <= max_val:

        # Create figure (single plot only)
        fig, ax = plt.subplots()

        x_min, x_max = 0, 10
        y_min = min(min_values)
        y_max = max(max_values)

        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)

        x = np.linspace(x_min, x_max, 300)

        # ===== Draw individual tuple regions FIRST =====
        # (so they can be overridden later by sky blue region)
        colors = plt.cm.tab10(np.linspace(0, 1, len(data)))

        for i, (health, minutes) in enumerate(data):
            lower = health / (minutes + 1)
            upper = health / (minutes - 1)

            ax.fill_between(
                x,
                lower,
                upper,
                alpha=0.3,
                color=colors[i]
            )  # each later tuple overlays previous ones


        # ===== Hatch outside valid region =====
        ax.fill_between(
            x,
            y_min,
            min_val,
            hatch="/",
            edgecolor="gray",
            facecolor="none"
        )

        ax.fill_between(
            x,
            max_val,
            y_max,
            hatch="/",
            edgecolor="gray",
            facecolor="none"
        )

        # ===== Sky blue valid intersection region (draw LAST so it stays on top) =====
        ax.fill_between(
            x,
            min_val,
            max_val,
            color="skyblue",
            alpha=0.6
        )

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("Valid Range Visualization")

        st.pyplot(fig)

    else:
        st.write("Không hợp lệ")