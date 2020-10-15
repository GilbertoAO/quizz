import csv
import os
import random

caminho = os.path.dirname(os.path.dirname(__file__)) + '/data'
arquivo = os.path.join(caminho, 'questions.csv')


question = list()

def list_of_ten_random():
    list_10 = []
    while len(list_10)<11:
        n = random.randint(1,42)
        if n not in list_10:
            list_10.append(n)
    return list_10
        

def random_question_from_csv():
    list_10 = list_of_ten_random()
    questions = []
    with open(arquivo, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter =';')
        next(csv_reader)
      
        for line in csv_reader:
            if int(line[0]) in list_10:
                list_10.remove(int(line[0]))
                questions.append(line[1:])
    
    return questions

    
