"""
Problem:
we need to write a program to find the position of a given number in a list of numbers arranged in decreasing order.we also need to minimize the number of times we access elements from the list.
"""
from jovian.pythondsa import evaluate_test_cases
def loacte_card(cards,query):
    position =0
    while position < len(cards):
        if cards[position] == query:
            return position
        position+=1
        
        if position==len(cards):
            return -1
    return -1


test_cases = [
    {'input':{'cards':[13,14,67,89,16,23], 'query':16},'output':4},
    {'input':{'cards':[13,14,67,89,16,23], 'query':90},'output':-1},
    {'input':{'cards':[13,14,67,89,16,23], 'query':13},'output':0},
    {'input':{'cards':[13,14,67,89,16,23], 'query':23},'output':5},
    {'input':{'cards':[], 'query':16},'output':-1},
    {'input':{'cards':[1], 'query':1},'output':0},
    {'input':{'cards':[1], 'query':2},'output':-1},
    {'input':{'cards':[1,2,3,4,5], 'query':3},'output':2},
    {'input':{'cards':[1,2,3,4,5], 'query':6},'output':-1},
]
evaluate_test_cases(loacte_card,test_cases)


