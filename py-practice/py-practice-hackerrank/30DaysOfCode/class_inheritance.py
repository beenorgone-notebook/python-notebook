# https://www.hackerrank.com/challenges/30-inheritance
# http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/


class Person:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def print_person(self):
        print("Name: {}, {}".format(self.lastName, self.firstName))
        print("ID:", self.idNumber)


class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        a = sum(self.scores) / len(self.scores)
        if a < 40:
            return 'T'
        elif a < 55:
            return 'D'
        elif a < 70:
            return 'P'
        elif a < 80:
            return 'A'
        elif a < 90:
            return 'E'
        elif a <= 100:
            return 'O'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade: {}".format(s.calculate()))
