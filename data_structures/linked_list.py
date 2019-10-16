class LinkedList:
    
    def __init__(self, _data, next):
        self._data = data
        self.next = None
            
    def insert_front(self, item):
        """
        Insert an item at the front of the queue
        """
        self._data.append(item)  # adds an item to the list
        
    def pop_front(self):
        """
        Remove an item from the front
        """
        item = self._data[0]
        del self._data[0]  # deletes the first item from the list
        return item
        
    def __len__(self):
        """
        Returns the length of the list
        """
        ...