import streamlit as st
from .utils import show_boxed_text, show_graph

def render():
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

    selected_rank = st.selectbox("Rank", options=list(Rank.keys()), index=1)
    selected_flock = st.selectbox("Flock", options=list(Flock.keys()), index=0)

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

    defaultATK3 = remain_Fero/9 if (850 - Main_Attack < 266) else max(320, 850 - Main_Attack)
    Health3 = st.number_input("3rd Health", min_value=0,
                              value=min(1300, max(int(remain_Fero/3), 2100 - Main_Health)),
                              step=50)

    Attack3 = st.number_input("3rd Attack", min_value=0,
                              value=max(0, int(defaultATK3)),
                              step=15)

    show_boxed_text(
        "Remaining",
        f"{int(remain_Fero - Health3 - Attack3 * 3.2)}",
        "30px",
        bg_color="#fc6a03"
    )

    show_graph(int(remain_Fero), Attack3, Health3, Main_Attack)