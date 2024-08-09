class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def __str__(self):
        return "Question: " + self.text + "  answer: " + self.answer
# new_q = Question("Is it true?", "True")
# print(new_q.text)
