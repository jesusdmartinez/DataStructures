class Stack:
    def __init__(self):
        self._data = list()

    def push(self, item):
        self._data.append(item)  # adds an item to the list

    def pop(self):
        if len(self._data) == 0:
            raise Exception

        else:
            item = self._data[len(self._data) - 1]
            del self._data[len(self._data) - 1]    # deletes the last item in the list
            return item

    def peek(self):
        return self._data[len(self._data) - 1]    # returns the last item in the list
        
    def __len__(self):
        return len(self._data)    # returns the length of the list

