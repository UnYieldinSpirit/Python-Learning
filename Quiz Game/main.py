import question_model
import quiz_brain
import data

question_bank = []

for key in data.question_data:
    new_question = question_model.Question(key["text"], key["answer"])
    question_bank.append(new_question)

quizbrain = quiz_brain.QuizBrain(question_bank)
quizbrain.next_question()