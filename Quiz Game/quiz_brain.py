# TODO - checking if the answer was correct
# TODO - checking if we're at the end of the quiz

class QuizBrain():
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list

    def next_question(self):
        print(f"Q.{self.question_number + 1}: {self.questions_list[self.question_number].text} (True/False)?")

    def answer