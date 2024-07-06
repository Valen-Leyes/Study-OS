# visual_effects_manager.py
import streamlit as st
from config import BALLOONS_SFX, SNOW_SFX

class VisualEffectsManager:
    def __init__(self):
        pass

    def add_balloons(self):
        st.balloons()

    def add_snow(self):
        st.snow()

    def add_visual_effects(self, completed_topics):
        mod = len(completed_topics) % 4
        if mod == 0:
            self.add_balloons()
            return BALLOONS_SFX
        else:
            self.add_snow()
            return SNOW_SFX
