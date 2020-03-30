from knowledge_corpus import *
import string
import json

# claire symptoms

# output of Claire's Decision Engine:
inference = {
             "questions": [],
             "comments": [],
             "answers": []
             }

# sample user response.
sample_user_response = {
                 "Fever": "Yes/No",
                 "Cough": "Yes/No",
                 "Shortness of breath": "Yes/No",
                 "Trouble breathing": "Yes/No",
                 "New confusion or inability to arouse": "Yes/No",
                 "Bluish lips or face": "Yes/No"
                 }


def symptoms_scorer(checklist):
    """

    :param checklist: dict.
    :return: claire's symptom score.
    """
    stage1_score = 0
    stage1_symptoms_total = len(stage1_symptoms)
    stage2_score = 0
    stage2_symptoms_total = len(stage2_symptoms)

    for symptom in checklist.keys():
        if checklist[symptom] == "yes":
            if symptom in stage1_symptoms:
                stage1_score += 1
            elif symptom in stage2_symptoms:
                stage2_score += 1

        elif checklist[symptom] == "no":
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
        count = 0
        no_of_recommendations = len(this_)
        prev_texts = ""
        for text in this_:
            prev_texts += text
            count += 1
            remaining = no_of_recommendations - count
            if remaining == 1:
                prev_texts += " and "
            else:
                prev_texts += ", "

        print(prev_texts)
        comments = inference["comments"].append(prev_texts)
        return comments

    @staticmethod
    def alert(this_):
        """
        # alert NCDC
        :return:
        """
        print(this_)
        inference["comments"].append(this_)

    @staticmethod
    def play(this_):
        """
        # play guide video
        :return:
        """
        print(this_)
        inference["comments"].append(this_)

    @staticmethod
    def place(this_):
        """
        """
        print(this_)
        inference["comments"].append(this_)

    @staticmethod
    def question(this_):
        """

        :param this_:
        :return:
        """
        print(this_)
        inference["questions"].append(this_)

    @staticmethod
    def answer(this_):
        """

        :param this_:
        :return:
        """
        print(this_)
        inference["answers"].append(this_)

    @staticmethod
    def comment(this_):
        """

        :param this_:
        :return:
        """
        print(this_)
        inference["comments"].append(this_)


def conversation_ai():
    """

    :return:
    """
    user_name = input("\nWelcome to Claire, please type in your name: ")
    print("\n\nHi "+str(user_name)+", which of the following symptoms do you have : ")
    dict_ = {}
    count = 1
    for symptom in stage1_symptoms:
        status = input(str(count)+". "+str(symptom) + "   (Yes / No) : ").lower()
        dict_[symptom] = status
        count += 1

    for symptom in stage2_symptoms:
        status = input(str(count)+". "+str(symptom) + "   (Yes / No) : ").lower()
        dict_[symptom] = status
        count += 1

    print(dict_)
    print("\n")
    return dict_


def decision_engine(symptoms_score):
    """
    :param symptoms_score:
    :return:
    """
    stage1_symptom_score = symptoms_score["stage1"]
    stage2_symptom_score = symptoms_score["stage2"]

    if stage1_symptom_score == 1/3 and stage2_symptom_score == 0/3:
        # recommend self isolation & come back if there are more symptoms.
        Claire.recommend(([pre_recorded_texts["care 1"], pre_recorded_texts["care 2"]]))
        Claire.play(pre_recorded_texts["care 7"])

    if stage1_symptom_score >= 2/3 and stage2_symptom_score == 0/3:
        # recommend hospital visit and self isolation until infection is confirmed.
        Claire.recommend([pre_recorded_texts["care 3"], pre_recorded_texts["care 6"]])
        # place amber location marker on the patient.
        Claire.recommend(pre_recorded_texts["care 8"])
        # if the user has not used Claire for up to 14 days request location history.
        Claire.question(pre_recorded_texts["care 11"])

    if stage2_symptom_score >= 1/3:
        # recommend visit to Hospital and self isolate.
        Claire.recommend([pre_recorded_texts["care 3"], pre_recorded_texts["care 1"]])
        # Alert NCDC ----------------------------------------
        Claire.alert("Alert NCDC")
        # progress to play video clip on guidelines of Covid19.
        Claire.play(pre_recorded_texts["care 7"])
        # place an amber marker on the user's current location.
        Claire.place(pre_recorded_texts["care 8"])
        # if the user has not used Claire for up to 14 days request location history.
        Claire.question(pre_recorded_texts["care 11"])

    if stage1_symptom_score == 0/3 and stage2_symptom_score == 0/3:
        # keep watching for symptoms.
        Claire.recommend(pre_recorded_texts["care 2"])
        # place green marker on Claire's Pandemic map
        Claire.recommend(pre_recorded_texts["care 10"])


# AQC - Answer, Question & Comment:
# Comment - to user, to mobile client.

# claire interaction history.

status_dict = conversation_ai()
score = symptoms_scorer(status_dict)
decision_engine(score)


print(inference)
json_output = json.dumps(inference)



