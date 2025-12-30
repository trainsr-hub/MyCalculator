import streamlit as st
import random

def probability_test(p: float) -> bool:
    return random.random() < (p/100)

probel = st.number_input(
    "Nhập xác suất (0 → 100%):",
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    step=0.01
)
# --- Canh giữa button bằng columns ---
col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    if st.button("🎲 Roll Dice"):
        result = probability_test(probel)

        # --- Hiển thị kết quả bằng markdown thay vì True / False ---
        if result:
            st.markdown("## ✅ **SUCCESS**")
        else:
            st.markdown("## ❌ **FAIL**")