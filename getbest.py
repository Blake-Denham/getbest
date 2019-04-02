#!/usr/bin/python3
#edited
import sys
import os


def getCols(f):
    """ Finds which columns the marks and student number is in """
    headings = f.readline().strip().split(",")
    i=0
    for head in headings:
        if head == "Student Number": num_col=i
        elif head == "Mark" : mark_col =i
        i = i+1
    return (num_col, mark_col)

def findTop(f,num_col, mark_col):
    """ finds the top student in the class """
    best = best_idx =  0
    for line in f:
        data = line.strip().split(",")[1:] 
        print(data)
        mark = int(data[mark_col])
        if mark > best:
            best=mark
    return best_idx, best


f = open(os.path.join(os.path.dirname(__file__), "bestdat0.csv"))
num_col, mark_col = getCols(f)
best_idx, best = findTop(f,num_col,mark_col)
print("The top student was student %s with %d"%(best_idx,best))
