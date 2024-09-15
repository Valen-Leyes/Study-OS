# study_plan.py
import json


def define_study_plan(subject):
    """
    Load the study plan for the specified subject.
    """
    with open(f"components/study_plan/assignments/{subject}.json", "r") as file:
        study_plan = json.load(file)

    return study_plan
