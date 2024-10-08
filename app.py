import streamlit as st
from components.quotes.quotes_display import QuotesDisplay
from components.quotes.quotes import define_quotes
from components.study_plan.study_plan_display import StudyPlanDisplay
from components.study_plan.study_plan import define_study_plan
from components.visual_effects.visual_effects_manager import VisualEffectsManager
from components.pomodoro_timer.pomodoro_timer import PomodoroTimer
from components.exam_turn.exam_turn import availability_checker
from components.meme.meme import meme_display
from utils import load_completed_topics, save_completed_topics, play_lofi_music, play_sound_effect

LOGIN_URL = st.secrets["LOGIN_URL"]
LOGIN_PAYLOAD = {
    "usuario": st.secrets["LOGIN_USER"],
    "password": st.secrets["LOGIN_PASSWORD"],
    "login": st.secrets["LOGIN_BUTTON"]
}
TARGET_URL = st.secrets["TARGET_URL"]
STRING_TO_SEARCH = st.secrets["STRING_TO_SEARCH"]

def display_page_title_and_header():
    """
    Set the page title and display the title.
    """
    st.set_page_config(page_title="Plan de Estudio 📚")
    st.title("Plan de Estudio 📚")

def play_background_music():
    """
    Play lofi music in the background.
    """
    play_lofi_music()

def display_pomodoro_timer():
    """
    Display a pomodoro timer.
    """
    pomodoro_timer = PomodoroTimer()
    pomodoro_timer.run()

def display_random_quote():
    """
    Display a random quote.
    """
    quotes = define_quotes()
    quotes_display = QuotesDisplay(quotes)
    quotes_display.display()

def load_and_filter_study_plan(unfiltered_completed_topics):
    """
    Define the study plan and load completed topics.
    Filter the study plan based on the selected day and subject.
    """
    subjects = ["AEDII", "LyMC"]  # Add more subjects as needed
    subject = st.selectbox("Selecciona una materia:", subjects)
    subject = subject.lower()

    study_plan = define_study_plan(subject)
    completed_topics_copy = unfiltered_completed_topics.copy()

    days = ["Todos"] + list(study_plan.keys())
    day = st.selectbox("Selecciona un día:", days)

    if day != "Todos":
        study_plan = {day: study_plan[day]}
        completed_topics = []
        study_plan_day = study_plan[day]
        for session, topics in study_plan_day["Sesiones"].items():
            for topic in topics:
                if topic in completed_topics_copy:
                    completed_topics.append(topic)
    else:
        completed_topics = completed_topics_copy

    return study_plan, completed_topics, day, completed_topics_copy

def display_study_plan(study_plan, completed_topics, day):
    """
    Display the study plan.
    """
    study_plan_display = StudyPlanDisplay(study_plan, completed_topics, day)
    visual_effects_manager = VisualEffectsManager()
    changes_made = study_plan_display.display()
    return changes_made, visual_effects_manager

def display_good_luck_message():
    """
    Display a message of good luck.
    """
    st.markdown("---")
    st.markdown("¡Buena suerte en tu estudio! 🍀")

def save_completed_topics_and_play_sound_effect(completed_topics, completed_topics_copy, visual_effects_manager):
    """
    If changes were made, save the completed topics and play a sound effect.
    """
    sfx = visual_effects_manager.add_visual_effects(completed_topics)
    play_sound_effect(sfx)
    for topic in completed_topics:
        if topic not in completed_topics_copy:
            completed_topics_copy.append(topic)
    save_completed_topics(completed_topics_copy)

def main():
    """
    The main function that runs the application.
    """
    display_page_title_and_header()
    play_background_music()
    availability_checker(LOGIN_URL, LOGIN_PAYLOAD, TARGET_URL, STRING_TO_SEARCH)
    meme_display()
    display_pomodoro_timer()
    display_random_quote()
    study_plan, completed_topics, day, unfiltered_completed_topics = load_and_filter_study_plan(load_completed_topics())
    changes_made, visual_effects_manager = display_study_plan(study_plan, completed_topics, day)
    display_good_luck_message()

    if changes_made:
        save_completed_topics_and_play_sound_effect(completed_topics, unfiltered_completed_topics, visual_effects_manager)

if __name__ == "__main__":
    main()
