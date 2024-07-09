# study_plan_display.py
import streamlit as st
import webbrowser

class StudyPlanDisplay:
    def __init__(self, study_plan, completed_topics, selected_day):
        self.study_plan = study_plan
        self.completed_topics = completed_topics
        self.selected_day = selected_day
        # Create an empty container for the progress bar
        self.progress_bar_container = st.empty()
        # Calculate the total topics
        self.total_topics = sum(len(topics) for day, day_sessions in self.study_plan.items() for session, topics in day_sessions["Sesiones"].items())
        # Display the initial progress bar
        self.update_progress_bar()

    def update_progress_bar(self):
        # Calculate the progress
        progress = len(self.completed_topics) / self.total_topics
        # Ensure the progress value is between 0.0 and 1.0
        progress = min(progress, 1.0)
        # Update the progress bar
        self.progress_bar_container.progress(progress)


    # Display the study plan and buttons to open the resources
    def display(self):
        changes_made = False
        for day, day_sessions in self.study_plan.items():
            st.header(day)
            for session, topics in day_sessions["Sesiones"].items():
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

            st.subheader("Recursos")
            for resource in day_sessions["Recursos"]:
                # Display the resource name as a button
                resource_name = resource.split("/")[-1]
                resource_button = st.button(resource_name, key=f"{day}_{resource_name}")
                if resource_button:
                    # Open the resource URL in a new tab
                    webbrowser.open_new_tab(resource)

        if len(self.completed_topics) == self.total_topics and self.selected_day == "Todos":
            st.success("¡Felicidades! Has completado todos los temas y recursos del plan de estudio.")
        return changes_made
