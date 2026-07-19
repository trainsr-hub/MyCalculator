# path: app.py

from datetime import datetime, timedelta
import streamlit as st

# Set page configuration with a premium dark-themed title and icon
st.set_page_config(
    page_title="Hatch Command Center",
    page_icon="🦖",
    layout="centered",
)

# Ultra-premium cyberpunk dark theme style overrides
st.markdown("""
<style>
    /* Dark Deep-Space base background */
    .stApp {
        background-color: #030712;
        color: #f3f4f6;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Header styling */
    .dashboard-header {
        text-align: center;
        padding: 20px 0 10px 0;
    }
    .dashboard-title {
        font-size: 2.2rem;
        font-weight: 900;
        letter-spacing: -0.5px;
        background: linear-gradient(135deg, #f3f4f6 0%, #9ca3af 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .dashboard-subtitle {
        font-size: 0.95rem;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 600;
    }
    
    /* Global Card Base with Glassmorphism */
    .premium-card {
        background: rgba(17, 24, 39, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        position: relative;
        overflow: hidden;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .premium-card:hover {
        transform: translateY(-2px);
    }
    
    /* Option 1 Style: Cyber Cyan (Speed & Stability) */
    .opt-speed {
        border-left: 4px solid #06b6d4;
        box-shadow: 0 4px 20px -5px rgba(6, 182, 212, 0.15);
    }
    .opt-speed .opt-badge {
        background: rgba(6, 182, 212, 0.1);
        color: #22d3ee;
        border: 1px solid rgba(6, 182, 212, 0.2);
    }
    .opt-speed .time-badge-text {
        background: linear-gradient(90deg, #22d3ee 0%, #06b6d4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 10px rgba(34, 211, 238, 0.3));
    }
    .opt-speed .active-window-bar {
        background: linear-gradient(90deg, #22d3ee 0%, #06b6d4 100%);
        box-shadow: 0 0 12px rgba(6, 182, 212, 0.8);
    }
    
    /* Option 2 Style: Sunset Crimson (Power & ROI) */
    .opt-roi {
        border-left: 4px solid #f43f5e;
        box-shadow: 0 4px 20px -5px rgba(244, 63, 94, 0.15);
    }
    .opt-roi .opt-badge {
        background: rgba(244, 63, 94, 0.1);
        color: #fda4af;
        border: 1px solid rgba(244, 63, 94, 0.2);
    }
    .opt-roi .time-badge-text {
        background: linear-gradient(90deg, #fda4af 0%, #f43f5e 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 10px rgba(244, 63, 94, 0.3));
    }
    .opt-roi .active-window-bar {
        background: linear-gradient(90deg, #fda4af 0%, #f43f5e 100%);
        box-shadow: 0 0 12px rgba(244, 63, 94, 0.8);
    }
    
    /* Expired Card Style (Subtle, Darkened) */
    .opt-expired {
        border-left: 4px solid #4b5563;
        background: rgba(17, 24, 39, 0.3);
        opacity: 0.6;
    }
    .opt-expired .opt-badge {
        background: rgba(75, 85, 99, 0.1);
        color: #9ca3af;
        border: 1px solid rgba(75, 85, 99, 0.2);
    }
    .opt-expired .time-badge-text {
        color: #4b5563;
    }
    
    /* Badges & Titles inside Cards */
    .card-meta {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;
    }
    .opt-badge {
        font-size: 0.75rem;
        font-weight: 800;
        letter-spacing: 1.5px;
        padding: 4px 10px;
        border-radius: 999px;
        text-transform: uppercase;
    }
    .card-subtitle {
        font-size: 0.75rem;
        color: #4b5563;
        font-weight: 700;
        letter-spacing: 1px;
    }
    
    /* Huge Centralized Window Typography */
    .window-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 16px;
        margin: 15px 0 25px 0;
    }
    .time-badge-text {
        font-size: 2.8rem;
        font-weight: 900;
        font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
        letter-spacing: -1.5px;
    }
    .window-arrow {
        font-size: 1.5rem;
        color: #374151;
        font-weight: 900;
        animation: breath 2.5s infinite ease-in-out;
    }
    
    /* Timeline Visual System */
    .timeline-wrapper {
        margin-top: 15px;
    }
    .timeline-labels {
        display: flex;
        justify-content: space-between;
        font-size: 0.7rem;
        color: #4b5563;
        font-weight: 700;
        margin-bottom: 6px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .timeline-labels .lbl-min {
        color: #9ca3af;
    }
    .timeline-labels .lbl-max {
        color: #d1d5db;
    }
    .timeline-track {
        height: 6px;
        background-color: #111827;
        border-radius: 999px;
        position: relative;
        border: 1px solid rgba(255, 255, 255, 0.02);
    }
    .active-window-bar {
        position: absolute;
        height: 100%;
        border-radius: 999px;
    }
    
    /* Keyframe Animations */
    @keyframes breath {
        0%, 100% { opacity: 0.4; transform: scale(0.95); }
        50% { opacity: 1; transform: scale(1.05); }
    }
    @keyframes pulse {
        0%, 100% { opacity: 0.8; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.02); }
    }
</style>
""", unsafe_allow_html=True)

# Premium Dashboard Header
st.markdown("""
<div class="dashboard-header">
    <div class="dashboard-title">HATCH SCHEDULING SYSTEM</div>
    <div class="dashboard-subtitle">TACTICAL COMMAND PANEL</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# Utilities & Math
# ============================================================
def clamp(td: timedelta, lower: timedelta, upper: timedelta):
    """Clamps timedelta safely between boundaries."""
    return max(lower, min(td, upper))


def format_td(td: timedelta):
    """Formats timedelta to concise human readable strings, returns None if empty."""
    total_seconds = int(td.total_seconds())
    if total_seconds <= 0:
        return None
        
    total_minutes = total_seconds // 60
    days = total_minutes // (24 * 60)
    total_minutes %= (24 * 60)
    hours = total_minutes // 60
    minutes = total_minutes % 60

    parts = []
    if days:
        parts.append(f"{days}D")
    if hours:
        parts.append(f"{hours}H")
    if minutes:
        parts.append(f"{minutes}M")

    return "".join(parts) if parts else None


# ============================================================
# Calculations System
# ============================================================
ads = 0

# >>>>>>>>>>>>>>>>>>> CHANGED SECTION START <<<<<<<<<<<<<<<<<<<
# HACK/FIX: Injecting configuration expander and shifting execution time context
from zoneinfo import ZoneInfo
user_tz = ZoneInfo("Asia/Ho_Chi_Minh")

now = datetime.now(user_tz)

# Simulation parameters controller UI element positioned directly above the windows
with st.expander("⚙️ TIME SIMULATION PARAMETERS", expanded=False):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        sel_days = st.selectbox("Days", options=list(range(8)), index=0)
    with col2:
        sel_hours = st.selectbox("Hours", options=list(range(24)), index=0)
    with col3:
        sel_minutes = st.selectbox("Minutes", options=list(range(60)), index=0)
    with col4:
        sel_skip = st.selectbox("Skip", options=list(range(8)), index=0)

# Calculate dynamic duration_arc and apply attenuation algorithms
duration_arc = timedelta(days=sel_days, hours=sel_hours, minutes=sel_minutes)
duration_post_skip = duration_arc * (0.9 ** sel_skip)
duration_arc =  duration_post_skip - max(duration_arc * 0.05, timedelta(minutes=5))

# Apply time shift factor to the base calculation matrix
now = now + duration_arc
today = now.date()

# Define optimal targets with explicit timezone binding
target_min = datetime.combine(today, datetime.min.time(), tzinfo=user_tz).replace(hour=7, minute=30)
target_medium = datetime.combine(today, datetime.min.time(), tzinfo=user_tz).replace(hour=10, minute=0)
target_max = datetime.combine(today, datetime.min.time(), tzinfo=user_tz).replace(hour=23, minute=0)
# >>>>>>>>>>>>>>>>>>> CHANGED SECTION END <<<<<<<<<<<<<<<<<<<<<

# ===================================================================================================
# CODE MODIFICATION REPORT BLOCK (EXPANSION):
# 1. Added `st.expander` right above the execution calculations with `expanded=False`.
# 2. Implemented 4 single-value dropdown selectors using `st.selectbox` for Days, Hours, Minutes, and Skip.
# 3. Formed `duration_arc` via `timedelta` using the selected components.
# 4. Computed the exact mathematical attenuation requested: `duration_arc *= 0.9**skip` 
#    and `duration_arc -= max(duration_arc * 0.05, 5 minutes)`.
# 5. Shifted the reference execution time: `now = now + duration_arc` impacting all downstream card logic.
# ===================================================================================================

# Offset boundaries from this moment
bien_min = target_min - now
bien_max = target_max - now
bien_medium = target_medium - now

ZERO = timedelta()
SEVEN = timedelta(days=7)

results = []

# Generate exact parameters for 6 computational target cycles
for day in range(6):
    offset = timedelta(days=day)
    current_min = bien_min + offset
    current_medium = bien_medium + offset
    current_max = bien_max + offset

    # Speed modifications
    cal1_min = current_min / (0.9 ** ads)
    cal1_medium = current_medium / (0.9 ** ads)
    cal1_max = current_max / (0.9 ** ads)

    # Standard safe-buffer adaptations
    cal2_min = max(cal1_min + timedelta(minutes=5), cal1_min / 0.95)
    call2_medium = max(cal1_medium + timedelta(minutes=5), cal1_medium / 0.95)
    cal2_max = max(cal1_max + timedelta(minutes=5), cal1_max / 0.95)

    # Hard boundary clamping
    cal2_min = clamp(cal2_min, ZERO, SEVEN)
    cal2_medium = clamp(call2_medium, ZERO, SEVEN)
    cal2_max = clamp(cal2_max, ZERO, SEVEN)

    text_min = format_td(cal2_min)
    text_medium = format_td(call2_medium)
    text_max = format_td(cal2_max)

    results.append({
        "day": day,
        "min": text_min,
        "medium": text_medium,
        "max": text_max,
        "raw_min": cal2_min,
        "raw_medium": call2_medium,
        "raw_max": cal2_max
    })

# ============================================================
# Tab Rendering System
# ============================================================
# Split 6 results into 3 strategic phases
phase_titles = [
    "⏱️ Urgent Horizons",
    "📅 Upcoming Windows",
    "🔮 Strategic Cycles"
]
tabs = st.tabs(phase_titles)

# Distribute 2 calculations to each tab (Option 1 and Option 2)
chunks = [results[i:i + 2] for i in range(0, len(results), 2)]

for tab, chunk in zip(tabs, chunks):
    with tab:
        st.write("") # Micro spacer
        
        # Ensure we always represent two tactical choices (Option 1 & Option 2)
        for idx, row in enumerate(chunk):
            is_option_2 = (idx == 1)
            
            # Map logical option properties
            if not is_option_2:
                opt_title = "⚡ Option 1: Tốc độ & Ổn định"
                css_class = "opt-speed"
                sub_label = "Optimal Speed Window"
            else:
                opt_title = "🔥 Option 2: Sức mạnh & ROI"
                css_class = "opt-roi"
                sub_label = "Max Yield Window"

            # Check if the overall window is fully expired (Max has passed)
            if not row["max"]:
                # Render an extremely stylish Expired state to maintain visual symmetry
                expired_html = f"""<div class="premium-card opt-expired">
<div class="card-meta">
<span class="opt-badge">EXPIRED</span>
<span class="card-subtitle">{sub_label}</span>
</div>
<div class="window-container">
<span class="time-badge-text">--</span>
<span class="window-arrow">➔</span>
<span class="time-badge-text">--</span>
</div>
<div class="timeline-wrapper">
<div class="timeline-labels">
<span>OFFLINE</span>
<span>CYCLE COMPLETE</span>
</div>
<div class="timeline-track"></div>
</div>
</div>"""
                st.markdown(expired_html, unsafe_allow_html=True)
                continue

            # Calculate precise spatial percentage representation for the progress bar
            raw_min_sec = max(0.0, row["raw_min"].total_seconds())
            raw_max_sec = max(0.0, row["raw_max"].total_seconds())
            
            if raw_max_sec > 0:
                min_percent = (raw_min_sec / raw_max_sec) * 100
                active_width = 100 - min_percent
            else:
                min_percent = 0
                active_width = 0

            # Determine the window state and customize HTML output
            if not row["min"]:
                # MIN time has passed but MAX is still in the future -> WINDOW IS OPEN NOW!
                status_badge = f'<span class="opt-badge" style="background: rgba(34, 197, 94, 0.15); color: #4ade80; border: 1px solid rgba(34, 197, 94, 0.3); animation: pulse 2s infinite;"><span style="color: #22c55e; margin-right: 5px;">●</span> ACTIVE NOW</span>'
                
                # Skip the "-- ➔" part entirely! Display only the remaining Max window cap
                window_html = f"""
<div class="window-container">
<span class="time-badge-text">{row['max']}</span>
</div>
"""
                timeline_labels = f"""
<div class="timeline-labels">
<span style="color: #4ade80; font-weight: 800;">Static ~ {now.time().strftime("%H:%M")}</span>
<span class="lbl-min">{row['medium'] if row['medium'] else ""}</span>
<span class="lbl-max">MAX EXPIRED</span>
</div>
"""
            else:
                # Both MIN and MAX are in the future -> Upcoming window
                status_badge = f'<span class="opt-badge">{opt_title}</span>'
                window_html = f"""
<div class="window-container">
<span class="time-badge-text">{row['min']}</span>
<span class="window-arrow">➔</span>
<span class="time-badge-text">{row['max']}</span>
</div>
"""
                timeline_labels = f"""
<div class="timeline-labels">
<span >Hum ~ {now.time().strftime("%H:%M")}</span>
<span class="lbl-min">{row['medium']}</span>
<span class="lbl-max">MAX EXPIRED</span>
</div>
"""

            # Construct the final ultra-premium glassmorphic HTML card with 0-indentation
            card_html = f"""<div class="premium-card {css_class}">
<div class="card-meta">
{status_badge}
<span class="card-subtitle">{sub_label}</span>
</div>
{window_html}
<div class="timeline-wrapper">
{timeline_labels}
<div class="timeline-track">
<div class="active-window-bar" style="left: {min_percent}%; width: {active_width}%;"></div>
</div>
</div>
</div>"""

            st.markdown(card_html, unsafe_allow_html=True)

st.divider()
