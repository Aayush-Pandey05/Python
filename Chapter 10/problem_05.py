'''
Question:- Write a Class 'Train' which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways.

'''

from random import randint

class Train:

    def __init__(self, trainno):
        self.trainno = trainno

    def book(self, fro, to):
        print(f"Your train of train number:- {self.trainno} is booked from {fro} to {to}")

    def getStatus(self):
        print(f"your train of train no:- {self.trainno} is on time")

    def getFare(self, fro, to):
        print(f"The fare for the train:- {self.trainno} from {fro} to {to} is {randint(222,5555)}")


a = Train(1445)
a.book("Chandigarh", "delhi")
a.getStatus()
a.getFare("Chandigarh", "delhi")