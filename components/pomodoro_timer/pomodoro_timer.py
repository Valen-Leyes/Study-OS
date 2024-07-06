# pomodoro_timer.py
import streamlit as st
import time

class PomodoroTimer:
    def __init__(self, work_duration=25, break_duration=5):
        self.work_duration = work_duration * 60  # Convert minutes to seconds
        self.break_duration = break_duration * 60  # Convert minutes to seconds
        self.current_duration = self.work_duration
        self.is_working = True
        self.is_timer_running = False

    def start_timer(self):
        self.is_timer_running = True
        start_time = time.time()
        while self.current_duration > 0:
            elapsed_time = time.time() - start_time
            self.current_duration = self.work_duration if self.is_working else self.break_duration
            self.current_duration -= elapsed_time
            if self.current_duration <= 0:
                self.is_working = not self.is_working
                start_time = time.time()
            self.display_timer()
            time.sleep(0.1)
        self.is_timer_running = False
        st.success("Time's up! Take a break." if self.is_working else "Break time is over. Let's get back to work!")

    def display_timer(self):
        minutes = int(self.current_duration // 60)
        seconds = int(self.current_duration % 60)
        timer_text = f"{minutes:02d}:{seconds:02d}"
        st.markdown(f"<h1 style='text-align: center; color: red;'>{timer_text}</h1>", unsafe_allow_html=True)

    def run(self):
        st.title("Pomodoro Timer")
        st.write("Work for 25 minutes, then take a 5-minute break. Repeat.")

        col1, col2 = st.columns(2)
        with col1:
            work_duration = st.number_input("Work Duration (minutes)", min_value=1, max_value=60, value=25, step=1)
        with col2:
            break_duration = st.number_input("Break Duration (minutes)", min_value=1, max_value=60, value=5, step=1)

        if st.button("Start Timer"):
            self.__init__(work_duration, break_duration)
            self.start_timer()
