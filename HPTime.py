import streamlit as st

st.title("Health - Minutes Calculator")

data = []
index = 0

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
        break  # Dừng vòng lặp khi một trong hai input bằng 0


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
        st.code(f"{min_val} ~ {(max_val + min_val) / 2} ~ {max_val}")
    else:
        st.write("Không hợp lệ")