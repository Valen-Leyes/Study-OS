import streamlit as st
from study_plan import define_study_plan
from study_plan_display import StudyPlanDisplay
from visual_effects_manager import VisualEffectsManager
from utils import play_zen_music, play_sound_effect, load_completed_topics, save_completed_topics

def main():
    st.set_page_config(page_title="Plan de Estudio 📚")
    st.title("Plan de Estudio 📚")

    play_zen_music()

    study_plan = define_study_plan()
    completed_topics = load_completed_topics()
    study_plan_display = StudyPlanDisplay(study_plan, completed_topics)
    visual_effects_manager = VisualEffectsManager()

    changes_made = study_plan_display.display()

    st.markdown("---")
    st.markdown("¡Buena suerte en tu estudio! 🍀")

    if changes_made:
        sfx = visual_effects_manager.add_visual_effects(completed_topics)
        play_sound_effect(sfx)
        save_completed_topics(completed_topics)

if __name__ == "__main__":
    main()
