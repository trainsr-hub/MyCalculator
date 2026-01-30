import streamlit as st
from datetime import timedelta  # ← thêm dòng này để dùng timedelta

def show_boxed_text(
    label,
    value,
    font_size="20px",
    text_color="white",
    bg_color="#333333"
):
    # Hiển thị text được canh giữa, có nền và style tuỳ chỉnh
    st.markdown(
        f"""
        <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: {bg_color};
            color: {text_color};
            font-size: {font_size};
            padding: 12px;
            border-radius: 8px;
            margin: 6px 0;
            font-weight: 600;
        ">
            {label}: {value}
        </div>
        """,
        unsafe_allow_html=True
    )

def select_duration(num_selectors, key_prefix):
    # Tạo số cột tương ứng (2 hoặc 3)
    cols = st.columns(num_selectors)

    days = 0  # mặc định khi chỉ có 2 selector

    if num_selectors == 3:
        with cols[0]:
            days = st.selectbox(
                "📅 Days",
                options=list(range(0, 8)),
                key=f"{key_prefix}_days"  # key duy nhất
            )

        with cols[1]:
            hours = st.selectbox(
                "⏰ Hours",
                options=list(range(0, 25)),
                key=f"{key_prefix}_hours"
            )

        with cols[2]:
            minutes = st.selectbox(
                "⏱️ Minutes",
                options=list(range(0, 61)),
                key=f"{key_prefix}_minutes"
            )

    elif num_selectors == 2:
        with cols[0]:
            hours = st.selectbox(
                "⏰ Hours",
                options=list(range(0, 25)),
                key=f"{key_prefix}_hours"
            )

        with cols[1]:
            minutes = st.selectbox(
                "⏱️ Minutes",
                options=list(range(0, 61)),
                key=f"{key_prefix}_minutes"
            )

    else:
        raise ValueError("num_selectors must be 2 or 3")

    # Convert các giá trị đã chọn thành duration chuẩn
    return timedelta(
        days=days,
        hours=hours,
        minutes=minutes
    )


def format_duration(td):
    # Chuyển timedelta thành chuỗi "Xd Yh Zm", chỉ hiển thị phần khác 0
    total_minutes = int(td.total_seconds() // 60)

    d, rem_min = divmod(total_minutes, 1440)
    h, m = divmod(rem_min, 60)

    return " ".join(
        f"{v}{k}" for v, k in [(d, "d"), (h, "h"), (m, "m")] if v
    ) or "0m"

def tab1hatchingtime():

    duration = select_duration(3, "hatchingtime")

    if duration != timedelta(0):
      ads = st.selectbox("🎬 Ads", options=list(range(0, 8)))
    else:
      ads = 1
    Now_Time = duration * 0.9**ads
    Free_Time = max(duration * 0.05, timedelta(minutes=5))

    show_boxed_text("Duration", format_duration(Now_Time), "30px", bg_color="#0000ff")
    show_boxed_text("Free", format_duration(Free_Time), "30px", bg_color="#008000")





def main():
    # Hàm main khởi tạo giao diện chính của app
    st.title("Streamlit App")

    # Tạo tabs
    tabs = st.tabs(["Hatching Time"])

    # Gán nội dung cho tab đầu tiên
    with tabs[0]:
        tab1hatchingtime()

if __name__ == "__main__":
    main()
