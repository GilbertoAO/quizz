import helpers
from model import Quizz, Question


if __name__ == "__main__":
    list_of_questions= helpers.random_question_from_csv()
    questions = [] #list of objects Question 
    for line in list_of_questions:
        all_options = line[1:-1]
    
        right_answer = line[-1]

        question = Question(line[0], right_answer, all_options)
        questions.append(question)
    
    quizz = Quizz(questions)
    quizz.question()
    print(quizz.final_result())