class Queue:
    
    def __init__(self):
        self._data = list()
    
    def enqueue(self, item):
        """
         Size:  O(n)
         Description:  Add item to the queue
         Parameter:  "item" identify the item to add
        """
        self._data.insert(0, item)
            
    def dequeue(self):
        """
        Size:  O(1)
        Description:  Remove item from the queue
        """
        item = self._data[0]
        del self._data[0]
        return item

    def __len__(self):
        """
        Size:  O(n)
        Description:  returns the length of the queue
        """
        return len(self._data)