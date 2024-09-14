# study_plan.py
import json


def define_study_plan():
    # Load the study plan JSON file
    with open("components/study_plan/study_plan.json", "r") as file:
        study_plan = json.load(file)

    return study_plan
