import question_model
import data

question_bank = []

for key in data.question_data:
    new_question = question_model.Question(key["text"], key["answer"])
    question_bank.append(new_question)
