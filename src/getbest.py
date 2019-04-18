#!/usr/bin/python3

import os


def getCols(f):
    """ Finds which columns the marks and student number is in """
    headings = f.readline().strip().split(",")
    i = 0  # was 1
    for head in headings:
        if head == "Student Number":
            num_col = i
        elif head == "Mark":
            mark_col = i
        i = i + 1  # wasn't here
    return (num_col, mark_col)


# assumes getCols was called first
def findTop(f, num_col, mark_col, headings_removed=True):
    """ finds the top student in the class """
    best = best_idx = 0

    # removes the headings of the table
    if not headings_removed:
        f.readline()

    for line in f:
        data = line.strip().split(",")
        mark = int(data[mark_col])  # was 50
        if mark > best:
            best_idx = data[num_col]  # wasn't here
            best = mark
    return best_idx, best


# put in main so testing doesn't do this (only runs if the file is run not imported)
if __name__ == '__main__':
    f = open(os.path.join('..', 'data', "bestdat0.csv"))
    print(f)
    num_col, mark_col = getCols(f)
    best_idx, best = findTop(f, num_col, mark_col)
    print("The top student was student %s with %d" % (best_idx, best))
    f.close()
