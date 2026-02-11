import streamlit as st  
from datetime import timedelta, datetime  # ← thêm dòng này để dùng timedelta  
import numpy as np  
import matplotlib.pyplot as plt  

  
Time_Now = datetime.now() + timedelta(hours=7)  



def plot_decay_timedelta(Timedeltax, max_x=7, n_times=None):
    global Time_Now
    free_time = max(Timedeltax * 0.05, timedelta(minutes=5))
    Timedelta = Timedeltax - free_time

    # ===== TẠO X LINSPACE MỊN =====
    x_curve1 = np.linspace(-0.5, max_x + 0.5, 400)  # đường cong mượt
    x_curve = np.floor(x_curve1)
    x_points = np.arange(0, max_x + 1)    # các điểm nguyên

    total_seconds = Timedelta.total_seconds()
    total_days = total_seconds/86400
  # đổi sang ngày ngay từ đầu

    y_curve = total_seconds * (0.9 ** np.floor(x_curve))
    y_points = total_seconds * (0.9 ** x_points)

    fig, ax = plt.subplots()

    # ===== VẼ ĐƯỜNG MƯỢT =====
    # ax.plot(x_curve, y_curve)
    ax.plot(x_curve, total_seconds * (0.9 ** np.ceil(x_curve - 0.5)), drawstyle="steps-pre")
    # ===== TÔ TỪNG STEP =====
    for n in range(0, max_x + 1):

        left = n - 0.5
        right = n + 0.5

        left = max(left, -0.5)
        right = min(right, max_x + 0.5)

        x_fill = np.linspace(left, right, 50)
        y_fill = total_seconds * (0.9 ** x_fill)

        current_seconds = total_seconds * (0.9 ** n)
        current_time = Time_Now + timedelta(seconds=current_seconds)

        hour = current_time.hour

        if 7 <= hour < 22:
            fill_color = "lime"
        elif 0 <= hour < 7:
            fill_color = "red"
        else:
            fill_color = "orange"

        ax.fill_between(
            x_fill,
            y_fill,
            0,
            color=fill_color,
            alpha=1
        )

        # ===== TEXT =====
        text_label = day_diff = current_time.strftime("%H:%M")  # giờ:phút định dạng 12h

        ax.text(
            n,
            current_seconds / 2,
            text_label,
            ha='center',
            va='center',
            fontsize=10,
            color='black',
            zorder=5
        )

# ===== VẼ 2 ĐƯỜNG X = n_times ± 0.5 =====
    if isinstance(n_times, int) and n_times <= max_x:

        for x_line in (n_times - 0.5, n_times + 0.5):

            if -0.5 <= x_line <= max_x + 0.5:

                y_top = total_seconds * (0.9 ** x_line)

                ax.vlines(
                    x_line,
                    ymin=0,
                    ymax=y_top,
                    linestyles="solid",
                    linewidth=2,
                    color="white",
                    zorder=6
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
# ===== DOT + TEXT TẠI GIAO ĐIỂM y = n =====
    for d in range(1, max_days + 1):

        target_seconds = d * 86400

        if target_seconds >= total_seconds:
            continue

        x_intersect = math.log(
            target_seconds / total_seconds
        ) / math.log(0.9)

        if -0.5 <= x_intersect <= max_x + 0.5:

            ax.scatter(
                x_intersect,
                target_seconds,
                color="white",
                edgecolor="black",
                zorder=7
            )

            # ===== TEXT =====
            ax.text(
                x_intersect,
                target_seconds,
                f"{d}D",
                ha="left",      # đẩy text sang phải một chút
                va="bottom",    # đẩy lên trên một chút
                fontsize=12,
                color="black",
                zorder=8
            )
    ax.set_xlim(-0.5, max_x + 0.5)
    # ax.yaxis.set_visible(False)

    ax.set_xlabel("Quảng cáo")

    st.pyplot(fig)

    return [timedelta(seconds=s) for s in y_points]


def show_legend():  
  
    html = """<div style="border:1px solid #444;  
padding:15px;  
border-radius:10px;  
background-color:#111;  
margin-top:15px;">  

<div>  
<span style="display:inline-block;width:15px;height:15px;background:#00ffff;opacity:1;border-radius:3px;"></span>  
<b> Linh xe ôm</b>
</div>  

<div style="margin-bottom:8px;">  
<span style="display:inline-block;width:15px;height:15px;background:blue;opacity:1;border-radius:3px;"></span>  
<b> Cặp đôi hoàn hảo</b> — Carry
</div>  
  
<div style="margin-bottom:8px;">  
<span style="display:inline-block;width:15px;height:15px;background:yellow;opacity:1;border-radius:3px;"></span>  
<b> Cặp đôi hoàn hảo</b> — Support
</div>  

<div style="margin-bottom:8px;">  
<span style="display:inline-block;width:15px;height:15px;background:lime;opacity:1;border-radius:3px;"></span>  
<b> Team 2</b> — Cân bằng nhưng không cân mọi kèo  
</div>  

<div style="margin-bottom:8px;">  
<span style="display:inline-block;width:15px;height:15px;background:purple;opacity:1;border-radius:3px;"></span>  
<b> Carry & Cảm Tử</b> - Carry
</div>
  
<div style="margin-bottom:8px;">  
<span style="display:inline-block;width:15px;height:15px;background:red;opacity:1;border-radius:3px;"></span>  
<b> Carry & Cảm Tử</b> - Cảm Tử
</div>  

<div style="margin-bottom:8px;">  
<span style="display:inline-block;width:15px;height:15px;background:gray;opacity:0.6;border-radius:3px;"></span>  
Đồng nát
</div>  
  
</div>"""  
  
    st.markdown(html, unsafe_allow_html=True)  
  
def show_graph(C, x_point=None, y_point=None, Optimal_x=None):  
  
    if C <= 0:  
        st.warning("No positive solution region.")  
        return  
  
    x_max = max(C / 3.2, x_point + 25)  
    real_x = C / (1 + 3.2)
    real_minx = C / (10 + 3.2)
    y_max = max(C, y_point)
    y_max_real = y_max - real_minx * 3.2
    deadzone_x = max(850 - Optimal_x, 0)
  
    x = np.linspace(0, x_max, 400)  
    y = C - 3.2 * x  
  
    fig, ax = plt.subplots()  
  
    # =========================  
    # VÙNG NON-RED (≤ C)  
    # =========================  
  
    if Optimal_x is not None:  
  
        # Giới hạn các mốc trong [0, x_max]  
        x1 = max(0, min(x_max, Optimal_x / 2))  
        x2 = max(0, min(x_max, Optimal_x / 1.5))  
        x3 = max(0, min(x_max, Optimal_x / 1.13))  
        x4 = max(0, min(x_max, Optimal_x * 1.13))  
        x5 = max(0, min(x_max, Optimal_x * 1.5))  
        x6 = max(0, min(x_max, Optimal_x * 2))  
  
        # Mask từng đoạn  
        mask1 = (x > 0) & (x <= x1)  
        mask2 = (x > x1) & (x <= x2)  
        mask3 = (x > x2) & (x <= x3)  
        mask4 = (x > x3) & (x <= x4)  
        mask5 = (x > x4) & (x <= x5)  
        mask6 = (x > x5) & (x <= x6)  
        mask7 = (x > x6) & (x <= x_max)  
        deadzone_x_neo = min(deadzone_x, x6)
  
        ax.fill_between(  
            x[mask1],  
            0,  
            y[mask1],  
            color="#00ffff",  
            alpha=1
        )  
  
  
        ax.fill_between(  
            x[mask2],  
            0,  
            y[mask2],  
            color="purple",  
            alpha=0.7
        )  
  
        ax.fill_between(  
            x[mask3],  
            0,  
            y[mask3],  
            color="blue",  
            alpha=1  
        )  
  
        ax.fill_between(  
            x[mask4],  
            0,  
            y[mask4],  
            color="lime",
            alpha=1  
        )  
  
        ax.fill_between(  
            x[mask5],  
            0,  
            y[mask5],  
            color="yellow",  
            alpha=1
        )  
        ax.fill_between(  
            x[mask6],  
            0,  
            y[mask6],  
            color="red",  
            alpha=1  
        )  
        ax.fill_between(  
            x[mask7],  
            0,  
            y[mask7],  
            color="gray",  
            alpha=0.6
        )  
    else:  
        ax.fill_between(x, 0, y, alpha=0.3)  
    if real_x > deadzone_x: ax.fill_between(x[x <= deadzone_x_neo], 0, y[x <= deadzone_x_neo], hatch='/', facecolor='none', edgecolor='black')
    # =========================  
    # VÙNG RED (> C)  
    # =========================  
    ax.fill_between(x, y, y_max, color="red", alpha=0.4)  
  
    ax.plot(x, y)
  
    # =========================  
    # PHẦN ĐIỂM & GIAO  
    # =========================  
  
    if x_point is not None and y_point is not None:  
  
        ax.scatter(x_point, y_point, s=100, zorder=5)  
  
        ax.annotate(  
            f"({x_point}, {y_point})",  
            (x_point, y_point),  
            xytext=(5, 5),  
            textcoords="offset points"  
        )  
  
        ax.axvline(x=x_point, linestyle="--")  
        ax.axhline(y=y_point, linestyle="--")  
  
        y_intersect = int(C - 3.2 * x_point)  
        ax.scatter(x_point, y_intersect, zorder=6)  
  
        ax.annotate(  
            f"Máu trâu\n({x_point}, {y_intersect})",  
            (x_point, y_intersect),  
            xytext=(5, -25),  
            textcoords="offset points"  
        )  
  
        x_intersect = int((C - y_point) / 3.2)  
        ax.scatter(x_intersect, y_point, zorder=6)  
  
        ax.annotate(  
            f"Damage to\n({x_intersect}, {y_point})",  
            (x_intersect, y_point),  
            xytext=(5, 10),  
            textcoords="offset points"  
        )  
 
    ax.set_xlim(min(y_max, real_minx), real_x)  
    ax.set_ylim(min(y_max, real_minx), y_max_real) 
  
    ax.set_title(f"3.2x + y = {int(C)}")  
    ax.set_xlabel("ATK")  
    ax.grid(False)  
  
    st.pyplot(fig)  
    show_legend()  
  
  
def show_boxed_text(  
    label,  
    value,  
    font_size="20px",  
    text_color="white",  
    bg_color="#333333",
    description=None  # new optional parameter, default keeps old calls working
):  
    # extract numeric part from font_size to calculate 1/4 size for description
    try:
        base_size = float(font_size.replace("px", ""))  # assume px unit
        desc_size = f"{base_size / 2}px" 
    except ValueError:
        desc_size = "12px"  # fallback size if font_size is not numeric
    
    st.markdown(  
        f"""  
        <div style="  
            display: flex;  
            flex-direction: column;  /* stack value and description vertically */
            justify-content: center;  
            align-items: center;  /* center horizontally */
            background-color: {bg_color};  
            color: {text_color};  
            padding: 12px;  
            border-radius: 8px;  
            margin: 6px 0;  
        ">  
            <div style="font-size: {font_size}; font-weight: 600;">
                {label}: {value}
            </div>
            {f'<div style="font-size: {desc_size}; opacity: 0.85; margin-top: 4px;">{description}</div>' if description else ''}
        </div>  
        """,  
        unsafe_allow_html=True  
    )
  
def select_duration(num_selectors, key_prefix):  
  
    cols = st.columns(num_selectors)  
    days = 0  
  
    if num_selectors == 3:  
        with cols[0]:  
            days = st.selectbox(  
                "📅 Days",  
                options=list(range(7, -1, -1)), 
                index=7, 
                key=f"{key_prefix}_days"  
            )  
  
        with cols[1]:  
            hours = st.selectbox(  
                "⏰ Hours",  
                options=list(range(24, -1, -1)), 
                index=24, 
                key=f"{key_prefix}_hours"  
            )  
  
        with cols[2]:  
            minutes = st.selectbox(  
                "⏱️ Minutes",  
                options=list(range(60, -1, -1)),  
                index=60,
                key=f"{key_prefix}_minutes"  
            )  
  
    elif num_selectors == 2:  
        with cols[0]:  
            hours = st.selectbox(  
                "⏰ Hours",  
                options=list(range(24, -1, -1)), 
                index=24, 
                key=f"{key_prefix}_hours"  
            )  
  
        with cols[1]:  
            minutes = st.selectbox(  
                "⏱️ Minutes",  
                options=list(range(60, -1, -1)),  
                index=60,
                key=f"{key_prefix}_minutes"  
            )  
  
    else:  
        raise ValueError("num_selectors must be 2 or 3")  
  
    return timedelta(  
        days=days,  
        hours=hours,  
        minutes=minutes  
    )  
  
  
def format_duration(td):  
    total_minutes = int(td.total_seconds() // 60)  
  
    d, rem_min = divmod(total_minutes, 1440)  
    h, m = divmod(rem_min, 60)  
  
    return " ".join(  
        f"{v}{k}" for v, k in [(d, "d"), (h, "h"), (m, "m")] if v  
    ) or "0m"  
  
  
def tab1hatchingtime():  
    global Time_Now  
    duration = select_duration(3, "hatchingtime")  
  
    if duration != timedelta(0):  
        ads = st.number_input("🎬 Ads", min_value=0, value=0, max_value=10, step=1) 
    else:  
        ads = 1  
  
    Now_Time = duration * 0.9**ads  
    Free_Time = max(duration * 0.05, timedelta(minutes=5))  
    Timer = max(timedelta(0), Now_Time - Free_Time)  
  
    col1, col2 = st.columns(2)
    # Tính thời điểm hoàn thành nếu bắt đầu Timer ngay bây giờ  
    finish_time = Time_Now + Timer  
    colorfree = "#008000" if datetime(1,1,1,7).time() <= finish_time.time() <= datetime(1,1,1,22).time() else "#FF0000"
    finish_at = finish_time.strftime("%I:%M %p") + (f" + {(finish_time.date() - Time_Now.date()).days} Days" if finish_time.date() != Time_Now.date() else "")
  
  
    with col1:  
        show_boxed_text("Duration", format_duration(Now_Time), "30px", bg_color="#0000ff")  
  
    with col2:  
        show_boxed_text("Timer", format_duration(Timer), "30px", bg_color="#8f8f8f")  
    plot_decay_timedelta(Timedeltax=duration, n_times=ads)
    show_boxed_text("Free", f"{format_duration(Free_Time)}", "30px", bg_color=colorfree, description=finish_at)
    
  

  
def tab2():  
  
    gap_duration = select_duration(2, "tab2_gap")  
    st.markdown("---")  
  
    B_duration = select_duration(3, "tab2_B")  
  
    result1 = (max(timedelta(minutes=5), 0.95 * B_duration) + gap_duration) / 0.95  
  
    show_boxed_text(  
        "Static",  
        format_duration(result1),  
        "30px",  
        bg_color="#008000"  
    )  
  
  
def tab3():  
  
    Rank = {  
        "Dominator 2K5 ~ Tape": 7100,  
        "Dominator 1K5 ~ I-Rex": 6722  
    }  
    BasePower = {  
        "Dominator 2K5 ~ Tape": (3076, 972),  
        "Dominator 1K5 ~ I-Rex": (2517, 962)  
    }  
  
    Flock = {  
        "Sinosauropteryx lv1": (477, 149),  
        "Preondactylus lv1": (282, 171),  
        "Compsognathus lv1": (249, 95),  
        "Sinosauropteryx lv5": (583, 182),  
        "Rodrigues Solitaire lv10": (715, 224),  
        "Tuojiangosaurus lv1": (42, 13)  
    }  
  
    selected_rank = st.selectbox(  
        "Rank",  
        options=list(Rank.keys()),  
        index=1  
    )  
  
    selected_flock = st.selectbox(  
        "Flock",  
        options=list(Flock.keys()),  
        index=0  
    )  
  
    st.markdown("---")  
  
    col1, col2 = st.columns(2)  
  
    with col1:  
        Health = st.number_input("Flock Health", min_value=0, value=Flock[selected_flock][0], step=50)  
  
    with col2:  
        Attack = st.number_input("Flock Attack", min_value=0, value=Flock[selected_flock][1], step=25)  
  
    st.markdown("---")  
  
    Main_Health = st.number_input("Ace Health", min_value=0, value=0, step=50)  
    Main_Attack = st.number_input("Ace Attack", min_value=0, value=0, step=25)  
  
    max_Fero = Rank[selected_rank]  
    Team_Fero = int(Health + Main_Health + 3.2 * Attack + 3.2 * Main_Attack)  
    remain_Fero = max_Fero - Team_Fero  
  
    st.markdown("---")  
    defaultATK3 = remain_Fero/9 if (850 - Main_Attack < remain_Fero/35) else 850 - Main_Attack
    Health3 = st.number_input("3rd Health", min_value=0, value=max(0, int(remain_Fero/3)), step=50)  
    Attack3 = st.number_input("3rd Attack", min_value=0, value=max(0, int(defaultATK3)), step=15)  
  
    show_boxed_text(  
        "Remaining",  
        f"{int(remain_Fero - Health3 - Attack3 * 3.2)}",  
        "30px",  
        bg_color="#fc6a03"  
    )  
  
    show_graph(int(remain_Fero), Attack3, Health3, Main_Attack)  
  
  
def main():  
  
    st.title("Streamlit App")  
  
    tabs = st.tabs(["Hatching Time", "Timers' Gap Balance", "Team Building"])  
  
    with tabs[0]:  
        tab1hatchingtime()  
  
    with tabs[1]:  
        tab2()  
  
    with tabs[2]:  
        tab3()  
  
  
if __name__ == "__main__":  
    main()