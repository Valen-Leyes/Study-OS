# study_plan_display.py
import streamlit as st

class StudyPlanDisplay:
    def __init__(self, study_plan, completed_topics):
        self.study_plan = study_plan
        self.completed_topics = completed_topics
        # Create an empty container for the progress bar
        self.progress_bar_container = st.empty()
        # Calculate the total topics
        self.total_topics = sum(len(topics) for sessions in self.study_plan.values() for topics in sessions.values())
        # Display the initial progress bar
        self.update_progress_bar()

    def update_progress_bar(self):
        # Calculate the progress
        progress = len(self.completed_topics) / self.total_topics
        # Update the progress bar
        self.progress_bar_container.progress(progress)

    # Display the study plan and checkboxes to mark topics as completed
    def display(self):
        changes_made = False
        for day, sessions in self.study_plan.items():
            st.header(day)
            for session, topics in sessions.items():
                st.subheader(session)
                for topic in topics:
                    checkbox_key = f"{day}_{session}_{topic}"
                    checkbox_placeholder = st.empty()
                    if topic in self.completed_topics:
                        checkbox_placeholder.checkbox(f":green[{topic}]", value=True, disabled=True)
                    else:
                        checkbox = checkbox_placeholder.checkbox(topic, key=checkbox_key)
                        if checkbox:
                            self.completed_topics.append(topic)
                            checkbox_placeholder.checkbox(f":green[{topic}]", value=True, disabled=True)
                            self.update_progress_bar()
                            changes_made = True

        if len(self.completed_topics) == self.total_topics:
            st.success("¡Felicidades! Has completado todos los temas del plan de estudio.")
        return changes_made
