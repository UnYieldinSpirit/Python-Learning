# TODO - checking if the answer was correct
# TODO - checking if we're at the end of the quiz

class QuizBrain():
    def __init__(self, questions_list):
        self.question_number = 0
        self.number_correct = 0
        self.questions_list = questions_list

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").title()
        while user_answer != "True" and user_answer != "False":
            print("Invalid Input!")
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").title()
        self.answer_check(user_answer, current_question.answer)

    def answer_check(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("CORRECT!")
            self.number_correct += 1
        else:
            print("INCORRECT")
                
        print(f"Your current score is: {self.number_correct}/{self.question_number}")
        print("\n")

    def quiz_end_check(self):
        return self.question_number == len(self.questions_list)