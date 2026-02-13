import streamlit as st
from datetime import timedelta

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

    return timedelta(days=days, hours=hours, minutes=minutes)




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