from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for n in question_data:
    text = n["text"]
    answer = n["answer"]
    new_q = Question(text, answer)
    question_bank.append(new_q)


quiz = QuizBrain(question_bank)

while not quiz.still_has_question():
    quiz.next_question()

quiz.final_score()




