import random

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You are wrong")
        print(f"The correct answer was: {correct_answer}")
        print("Your current score is:",self.score, "/", self.question_number)
        print("")

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        question_text = current_question.text
        question_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question_text} (true/false): ")
        self.check_answer(user_answer, question_answer)

    def still_has_question(self):
        return self.question_number == len(self.questions_list)

    def final_score(self):
        print(f"Your final score was: {self.score} / {self.question_number}")