from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
new_quiz = QuizBrain(question_bank)

for i in question_data:
    new_question = Question(i['question'], i['correct_answer'])
    question_bank.append(new_question)

while new_quiz.still_has_questions():
    new_quiz.next_question()
print(f'You\'ve completed the quiz!')
print(f'Your final score was: {new_quiz.score}/{new_quiz.question_number}')
