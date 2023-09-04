class QuizBrain:
    """Quiz Brain"""
    
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_ques = self.question_list[self.question_number].ques
        current_ans = self.question_list[self.question_number].ans
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_ques}: (True/False)?")
        if self.check_answer(user_ans, current_ans):
            self.score += 1
            print("Your answer is coreect.")
            print(f"Your current score is {self.score}")
        else:
            print("Your answer is incorrect.")
            print(f"Your current score is {self.score}")

    def still_have_questions(self) -> bool:
        if self.question_number < len(self.question_list):
            return True
        else:
            print("Quiz Finished!!!")
            return False

    def check_answer(self, user_ans, ans) -> bool:
        return ans.lower() == user_ans.lower()


    