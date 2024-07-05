import streamlit as st

class StudyPlanDisplay:
    def __init__(self, study_plan, completed_topics):
        self.study_plan = study_plan
        self.completed_topics = completed_topics

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
                            changes_made = True

        if len(self.completed_topics) == sum(len(topics) for sessions in self.study_plan.values() for topics in sessions.values()):
            st.success("¡Felicidades! Has completado todos los temas del plan de estudio.")
        
        return changes_made
