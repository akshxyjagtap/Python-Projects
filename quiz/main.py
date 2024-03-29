from data import question_data
from quiz_brain import QuizBrain
from question_model import Question


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has():
    quiz.next_question()


print(f"Q. question_bank[0].text")


