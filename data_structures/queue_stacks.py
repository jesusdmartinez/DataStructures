from data_structures.queue import Queue
from data_structures.stack import Stack


class Queue_Stacks:

    def __init__(self):
        self.stack_one = Stack()
        self.stack_two = Stack()

    def enqueue(self, item):
        """
        Size:  O(1)
        Description:  Add an item to the stack
        Parameters:  item: the item you will add
        """
        self.stack_one.push(item)

    def dequeue(self):
        """
        Size:  O(n)
        Description:  Take something away from the queue
        Parameters:  item: the item you will add
        """
        while len(self.stack_one) > 0:
            temp = self.stack_one.pop()
            self.stack_two.push(temp)
        result = self.stack_two.pop()
        while len(self.stack_two) > 0:
            revert_temp = self.stack_two.pop()
            self.stack_one.push(revert_temp)
        return result

# class Queue_Stacks:
#
#     def __init__(self):
#         self.stack_one = Stack()
#         self.stack_two = Stack()
#
#     def enqueue(self, item):
#         if len(self.stack_two) == 0:
#             self.stack_one.push(item)
#         else:
#             while len(self.stack_two) > 0:
#                 revert_temp = self.stack_two.pop()
#                 self.stack_one.push(revert_temp)
#             self.stack_one.push(item)
#
#     def dequeue(self):
#         if len(self.stack_one) == 0:
#             return self.stack_two.pop()
#         else:
#             while len(self.stack_two) > 0:
#                 revert_temp = self.stack_two.pop()
#                 self.stack_one.push(revert_temp)
#
#             while len(self.stack_one) > 0:
#                 temp = self.stack_one.pop()
#                 self.stack_two.push(temp)
#                 result = self.stack_two.pop()
#         return result


# from stack import Stack
#
#
# class QueueStack:
#
#     def __init__(self):
#         self._stack1 = Stack()
#         self._stack2 = Stack()
#
#     def enqueue(self, item):
#         """Add item to the enqueue stack.
#
#         Parameters:
#         item: item to add to the queue
#         """
#         while len(self._stack1) > 0:
#             self._stack2.push(self._stack1.pop())
#         self._stack2.push(item)
#
#     def dequeue(self):
#         """Remove item from the queue.
#
#         Returns:
#         item: First item in queue
#         """
#         while len(self._stack2) > 0:
#             self._stack1.push(self._stack2.pop())
#         return self._stack1.pop()
#
#
# myqueue = QueueStack()
# myqueue.enqueue("Hooray1")
# myqueue.enqueue("Hooray2")
# print(myqueue.dequeue())