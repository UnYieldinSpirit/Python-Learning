import question_model
import quiz_brain
import data

question_bank = []

for key in data.question_data:
    new_question = question_model.Question(key["text"], key["answer"])
    question_bank.append(new_question)

brain = quiz_brain.QuizBrain(question_bank)

while brain.quiz_end_check() != True:
    brain.next_question()

print("You completed the quiz")
print(f"Here is your final score: {brain.number_correct}/{brain.question_number}")