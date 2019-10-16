import unittest
from data_structures.queue import Queue


class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        # Arrange
        my_queue = Queue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)

        # Act
        enqueue1 = my_queue.dequeue()
        enqueue2 = my_queue.dequeue()

        # Assert
        self.assertEqual(2, enqueue1, "first enqueue did not match")
        self.assertEqual(1, enqueue2, "second enqueue did not match")


    def test_len(self):
        # Arrange
        my_queue = Queue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)

        # Act
        len1 = len(my_queue)

        # Assert
        self.assertEqual(2, len1, "your lengths do not match yo :(")


unittest.main(argv=[''], verbosity=2, exit=False)