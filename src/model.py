import random

class Question:
    def __init__(self, question, right_answer, all_options):
        self._question = question
        self._right_answer = right_answer
        #self._right_option = None
        self._user_answer = None
        self._all_options =  all_options
        self._organized_options = {}
    
    @property
    def question(self):
        return self._question
    
    @property
    def right_answer(self):
        return self._right_answer
    

    
    

    def user_answer(self, answer):
        self._user_answer = answer.upper()
        for _ in range(3):
            if len(self._user_answer)>1 or len(self._user_answer) == 0 :
                print('Your answer must have a letter, please try again')
                self._user_answer = input().upper()
            elif self._user_answer not in self._organized_options: 
                print(f'your answer is out of the limits {chr(65)}..{chr(65 + len(self._all_options))}, plesase try again')
                self._user_answer = input().upper()
            else:
                break
         


    def shuffle_options(self):
        '''shuffle the options'''
        random.shuffle(self._all_options)
    

    def organizes_options(self):
        ''' Creates a dic with (a,b ... f) with the options '''
        i = 0 
        for option in self._all_options:
            self._organized_options[f'{chr(65+i)}'] =  option
            i+=1
    
    def is_right(self):
        user_option = self._organized_options[self._user_answer]
        if self._right_answer == user_option:
            return True
        else:
            return False
     
    

    def __str__(self):
        self.shuffle_options()
        self.organizes_options()
        text = f'{self.question} \n'
        for key, value in self._organized_options.items():
            text = f'{text} {key} - {value}\n'
        return text    



#question1 =  Question('Which country has won most world cups soccer?', 'Brazil',  ['German', 'Italy', 'Argentina'])

#print(question1)
#answer = input('digite sua resposta \n')
#question1.user_answer(answer)
#print(question1.is_right())


class Quizz:
    def __init__(self, questions, score = 0):
        self._questions = questions
        self._score = score
        self._fails = []
    
    def question(self):
        i=0
        for question in self._questions:
            i+=1
            print(f'{i} - {question}')
            answer = input('Whats is the right option? \n')
            question.user_answer(answer)
            if question.is_right():
                self.scores()
            else:
                print(f'{i} erro')
                self._fails.append(question)
        


    def scores(self):
        self._score+=1

    
    def final_score(self):
        max_score = 100
        qnt_of_questions = len(self._questions)
        value_of_each_question = max_score/qnt_of_questions
        return self._score*value_of_each_question
    
    def final_result(self):
        text = f'Your Score is {self.final_score()}\n'
        print(self._fails)
        if self._fails == []:
            text = f'{text} You did not missed any question'
        else:
            text = f"{text} Questions you've missed"
            for question in self._fails:
             text = f"{text} {question.question} \n your answer was: {question._user_answer}, and the right answer is {question._right_answer}"
        return text
                