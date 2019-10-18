import random2


def bubble_sort_asc(myList):
    """
    Description:  BubbleSort in ascending order
    Item:  "list" the list which we wold like to sort
    """

    for i in range(len(myList) - 1):
        for j in range(len(myList) - 1 - i):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]

    return myList


def bubble_sort_dec(myList):
    """
    Description:  BubbleSort in descending order
    Item:  "list" the list which we wold like to sort
    """

    for i in range(len(myList) - 1):
        for j in range(1, len(myList) - i):
            if myList[j-1] < myList[j]:
                myList[j - 1], myList[j] = myList[j], myList[j - 1]

    return myList


def insert_sort(myList):
    """
    """

    for i in range(1, len(myList)):
        for j in range(0, i):


    return myList


# print(bubble_sort_asc([3, 1, 67, 2, 1]))
# print(bubble_sort_asc([3, 1, 67, 2, 1]))

print(insert_sort([5, 6, 2, 10, 1, 5, 2, 7]))






