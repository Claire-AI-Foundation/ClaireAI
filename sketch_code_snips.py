# def conversation_ai():
#     """
#
#     :return:
#     """
#     user_name = input("\nWelcome to Claire, please type in your name: ")
#     print("\n\nHi "+str(user_name)+", which of the following symptoms do you have : ")
#     dict_ = {}
#     count = 1
#     for symptom in stage1_symptoms:
#         status = input(str(count)+". "+str(symptom) + "   (Yes / No) : ").lower()
#         dict_[symptom] = status
#         count += 1
#
#     for symptom in stage2_symptoms:
#         status = input(str(count)+". "+str(symptom) + "   (Yes / No) : ").lower()
#         dict_[symptom] = status
#         count += 1
#
#     print(dict_)
#     print("\n")
#     return dict_
#
#

# sample user response.
sample_user_response = {
                 "Fever": "Yes/No",
                 "Cough": "Yes/No",
                 "Shortness of breath": "Yes/No",
                 "Trouble breathing": "Yes/No",
                 "New confusion or inability to arouse": "Yes/No",
                 "Bluish lips or face": "Yes/No"
                 }

