import streamlit as st
from components.quotes.quotes_display import QuotesDisplay
from components.quotes.quotes import define_quotes
from components.study_plan.study_plan_display import StudyPlanDisplay
from components.study_plan.study_plan import define_study_plan
from components.visual_effects.visual_effects_manager import VisualEffectsManager
from components.pomodoro_timer.pomodoro_timer import PomodoroTimer
from utils import load_completed_topics, save_completed_topics, play_lofi_music, play_sound_effect

def main():
    """
    The main function that runs the application.
    """
    # Set the page title and display the title
    st.set_page_config(page_title="Plan de Estudio 📚")
    st.title("Plan de Estudio 📚")

    # Play lofi music in the background
    play_lofi_music()

    # Display a pomodoro timer
    pomodoro_timer = PomodoroTimer()
    pomodoro_timer.run()

    # Display a random quote
    quotes = define_quotes()
    quotes_display = QuotesDisplay(quotes)
    quotes_display.display()

    # Define the study plan and load completed topics
    study_plan = define_study_plan()
    completed_topics = load_completed_topics()

    # Display the study plan
    study_plan_display = StudyPlanDisplay(study_plan, completed_topics)
    visual_effects_manager = VisualEffectsManager()
    changes_made = study_plan_display.display()

    # Display a message of good luck
    st.markdown("---")
    st.markdown("¡Buena suerte en tu estudio! 🍀")

    # If changes were made, save the completed topics and play a sound effect
    if changes_made:
        sfx = visual_effects_manager.add_visual_effects(completed_topics)
        play_sound_effect(sfx)
        save_completed_topics(completed_topics)

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
