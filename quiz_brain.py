class QuizBrain:

    def __init__(self, question_list):
        self.number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.number]
        self.number += 1
        choice = input(f"Q. {self.number}: {current_question.text} (True/False)?: ")
        self.check_answer(choice, current_question.answer)

    def still_questions(self):
        return self.number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You answered correctly!!")
        else:
            print("Incorrect answer")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is {self.score}/{len(self.question_list) - 1}\n")







