import streamlit as st          
from datetime import timedelta, datetime  # ← thêm dòng này để dùng timedelta          
import numpy as np          
import matplotlib.pyplot as plt          

Time_Now = datetime.now() + timedelta(hours=7)

# Re-export plot function from subpackage
from .plots.decay import plot_decay_timedelta        


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
    # HATCH VÀNG (ngoài hatch đen)
    # =========================

    if Optimal_x is not None:

        golden_start = max(max(400, 800 - Optimal_x), deadzone_x_neo)
        golden_end   = min(700, 1200 - Optimal_x)

        # Giới hạn trong miền hiển thị
        golden_start = max(0, min(x_max, golden_start))
        golden_end   = max(0, min(x_max, golden_end))

        if golden_start < golden_end:

            # mask vùng golden
            golden_mask = (x >= golden_start) & (x <= golden_end)

            # Loại bỏ phần overlap với hatch đen
            if real_x > deadzone_x:
                golden_mask &= (x > deadzone_x_neo)

            ax.fill_between(
                x[golden_mask],
                0,
                y[golden_mask],
                hatch='*',          
                facecolor='none',
                edgecolor='#8a2be2',       # màu vàng golden
                linewidth=0
            )


# =========================
            # 2 ĐƯỜNG VIỀN GIỚI HẠN THEO VÙNG GOLDEN
            # =========================

            y_start = C - 3.2 * golden_start  # chiều cao tại golden_start
            y_end   = C - 3.2 * golden_end    # chiều cao tại golden_end

            # Vẽ đoạn thẳng đứng từ 0 -> y(x)
            ax.plot(
                [golden_start, golden_start],
                [0, y_start],
                color='gold',
                linewidth=2
            )

            ax.plot(
                [golden_end, golden_end],
                [0, y_end],
                color='gold',
                linewidth=2
            )

            # =========================
            # CHÚ THÍCH KHOẢNG GOLDEN
            # =========================

            # đặt annotation ở giữa vùng golden
            mid_x = (golden_start + golden_end) / 2
            mid_y = (C - 3.2 * mid_x) * 0.5   # nằm trong vùng non-red

            ax.annotate(
                f"{int(golden_start)} ~ {int(golden_end)}",
                (mid_x, mid_y),
                ha='center',
                color="black",   # text xanh dương
                bbox=dict(
                    facecolor="white",   # khung trắng
                    edgecolor="black",
                    boxstyle="round,pad=0.3"
                )
            )

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
            f"\n({x_point}, {y_point})",          
            (x_point, y_point),
            color="black",          
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
            color="black",          
            xytext=(5, -25),          
            textcoords="offset points"          
        )          

        x_intersect = int((C - y_point) / 3.2)          
        ax.scatter(x_intersect, y_point, zorder=6)          

        ax.annotate(          
            f"Damage to\n({x_intersect}, {y_point})",          
            (x_intersect, y_point),  
            color="black",        
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