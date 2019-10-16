from data_structures.queue import Queue
from data_structures.stack import Stack


# class Queue_Stacks:
#
#     def __init__(self):
#         self.stack_one = Stack()
#         self.stack_two = Stack()
#
#     def enqueue(self, item):
#         self.stack_one.push(item)
#
#     def dequeue(self):
#         while len(self.stack_one) > 0:
#             temp = self.stack_one.pop()
#             self.stack_two.push(temp)
#         result = self.stack_two.pop()
#         while len(self.stack_two) > 0:
#             revert_temp = self.stack_two.pop()
#             self.stack_one.push(revert_temp)
#         return result

class Queue_Stacks:

    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()

    def enqueue(self, item):
        self.stack_one.push(item)

    def dequeue(self):
        while len(self.stack_one) > 0:
            temp = self.stack_one.pop()
            self.stack_two.push(temp)
        result = self.stack_two.pop()
        while len(self.stack_two) > 0:
            revert_temp = self.stack_two.pop()
            self.stack_one.push(revert_temp)
        return result