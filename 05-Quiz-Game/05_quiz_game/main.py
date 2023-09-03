from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(data["text"], data["answer"]) for data in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()    