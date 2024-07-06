import streamlit as st
import time
from utils import play_sound_effect
from config import BREAK_SFX, COMPLETE_SFX

class PomodoroTimer:
    def __init__(self, work_duration=25, break_duration=5):
        self.work_duration = work_duration * 60  # Convert minutes to seconds
        self.break_duration = break_duration * 60  # Convert minutes to seconds
        self.current_duration = self.work_duration
        self.is_working = True
        self.is_timer_running = False
        self.timer_container = st.empty()
        self.success_container = st.empty()

    def start_timer(self):
        self.is_timer_running = True
        start_time = time.time()
        
        while self.is_timer_running:
            elapsed_time = time.time() - start_time
            if self.is_working:
                self.current_duration = self.work_duration - elapsed_time
            else:
                self.current_duration = self.break_duration - elapsed_time
            
            if self.current_duration <= 0:
                if self.is_working:
                    self.success_container.success("Time's up! Take a break.")
                    self.is_working = not self.is_working
                    play_sound_effect(BREAK_SFX)  # Play break sound effect
                else:
                    self.success_container.success("Break time is over. Pomodoro completed!")
                    self.is_timer_running = False  # Stop the timer
                    self.current_duration = 0
                    play_sound_effect(COMPLETE_SFX)  # Play complete sound effect
                start_time = time.time()
            
            self.display_timer()
            time.sleep(0.1)

    def display_timer(self):
        minutes = int(self.current_duration // 60)
        seconds = int(self.current_duration % 60)
        timer_text = f"{minutes:02d}:{seconds:02d}"
        if self.is_working:
            color = 'red'
        else:
            color = 'green'
        self.timer_container.markdown(f"<h1 style='text-align: center; color: {color};'>{timer_text}</h1>", unsafe_allow_html=True)

    def run(self):
        st.header("Pomodoro Timer")
        desc = st.empty()

        col1, col2 = st.columns(2)
        with col1:
            work_duration = st.number_input("Work Duration (minutes)", min_value=1, max_value=60, value=25, step=1)
        with col2:
            break_duration = st.number_input("Break Duration (minutes)", min_value=1, max_value=60, value=5, step=1)

        desc.write(f"Study for {work_duration} minutes, then take a {break_duration}-minute break. Repeat.")

        if st.button("Start Timer"):
            self.__init__(work_duration, break_duration)
            self.start_timer()
