import streamlit as st
from core import tab_hatching, tab_gap, tab_team

def main():
    st.title("Streamlit App")

    tabs = st.tabs(["Hatching Time", "Timers' Gap Balance", "Team Building"])

    with tabs[0]:
        tab_hatching.render()

    with tabs[1]:
        tab_gap.render()

    with tabs[2]:
        tab_team.render()

if __name__ == "__main__":
    main()