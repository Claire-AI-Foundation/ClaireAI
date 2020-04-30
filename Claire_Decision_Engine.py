from knowledge_corpus import *
import ast
import json


# output of Claire's D.E:
inference = {"questions": [], "comments": [], "answers": []}


def symptoms_scorer(symptoms_dict):
    """

    :param symptoms_dict: dict.
    :return: claire's symptom score.
    """
    stage1_score = 0
    stage1_symptoms_total = len(stage1_symptoms)
    stage2_score = 0
    stage2_symptoms_total = len(stage2_symptoms)

    for symptom in symptoms_dict.keys():
        if symptoms_dict[symptom] == "yes":
            if symptom in stage1_symptoms:
                stage1_score += 1
            elif symptom in stage2_symptoms:
                stage2_score += 1

        elif symptoms_dict[symptom] == "no":
            continue

    stage1_symptom_score = stage1_score / stage1_symptoms_total
    stage2_symptom_score = stage2_score / stage2_symptoms_total

    output = {"stage1": stage1_symptom_score, "stage2": stage2_symptom_score}

    return output


pre_recorded_texts = {
                          "care 1": "self isolate",
                          "care 2": "come back if there are more symptoms",
                          "care 3": "pay a visit to a hospital",
                          "care 4": "where have you been in the past 14 days",
                          "care 5": "Alert NCDC",
                          "care 6": "self isolate until an infection in confirmed",
                          "care 7": "play video clip on health guidelines for Covid 19.",
                          "care 8": "place location marker (amber) on the patient.",
                          "care 9": "place location marker (red) on the patient.",
                          "care 10": "place location marker (green) on the patient",
                          "care 11": "please provide your location history for the past 14 days",

                      }


class Claire(object):
    """

    """
    def __init__(self):
        """
        Claire's general performance software.
        """

    @staticmethod
    def recommend(this_):
        """
        # recommend certain measures.
        :return:
        """
        inference["comments"].append(this_)

    @staticmethod
    def alert(this_):
        """
        # alert NCDC
        :return:
        """
        inference["comments"].append(this_)

    @staticmethod
    def play(this_):
        """
        # play guide video
        :return:
        """
        inference["comments"].append(this_)

    @staticmethod
    def place(this_):
        """
        """
        inference["comments"].append(this_)

    @staticmethod
    def question(this_):
        """

        :param this_:
        :return:
        """
        inference["questions"].append(this_)

    @staticmethod
    def answer(this_):
        """

        :param this_:
        :return:
        """
        inference["answers"].append(this_)

    @staticmethod
    def comment(this_):
        """

        :param this_:
        :return:
        """
        inference["comments"].append(this_)


def decision_engine(symptoms_score):
    """
    :param symptoms_score:
    :return:
    """
    stage1_symptom_score = symptoms_score["stage1"]
    stage2_symptom_score = symptoms_score["stage2"]

    if stage1_symptom_score == 1/3 and stage2_symptom_score == 0/3:
        Claire.recommend(pre_recorded_texts["care 1"])
        Claire.recommend(pre_recorded_texts["care 2"])
        Claire.play(pre_recorded_texts["care 7"])

    if stage1_symptom_score >= 2/3 and stage2_symptom_score == 0/3:
        Claire.question(pre_recorded_texts["care 11"])
        Claire.recommend(pre_recorded_texts["care 3"])
        Claire.recommend(pre_recorded_texts["care 6"])
        Claire.recommend(pre_recorded_texts["care 8"])

    if stage2_symptom_score >= 1/3:
        Claire.recommend(pre_recorded_texts["care 3"])
        Claire.recommend(pre_recorded_texts["care 1"])
        Claire.alert("Alert NCDC")
        Claire.play(pre_recorded_texts["care 7"])
        Claire.place(pre_recorded_texts["care 8"])
        Claire.question(pre_recorded_texts["care 11"])

    if stage1_symptom_score == 0/3 and stage2_symptom_score == 0/3:
        Claire.recommend(pre_recorded_texts["care 2"])
        Claire.recommend(pre_recorded_texts["care 10"])


def main_func(user_input):
    """

    :param user_input: json input from the user via mobile/ web client.
    :return:
    """
    user_input = str(user_input)
    if type(user_input) == str:
        user_input = ast.literal_eval(user_input)
    else:
        pass
    score = symptoms_scorer(user_input)
    decision_engine(score)
    json_output = json.dumps(inference)

    return json_output

# ---------------------------------------------------------------------------------
# Guide: Uncomment the code snippet below and
# run this program file to understand how main_func(user_input) works.
# Alternatively read the pdf file "Claire.ai documentation in the project directory
# ---------------------------------------------------------------------------------
# # sample user response.
# user_input_ = {
#                  "Fever": "Yes/No",
#                  "Cough": "Yes/No",
#                  "Shortness of breath": "Yes/No",
#                  "Trouble breathing": "Yes/No",
#                  "New confusion or inability to arouse": "Yes/No",
#                  "Bluish lips or face": "Yes/No"
#                  }
#
#
# print(main_func(user_input_))
