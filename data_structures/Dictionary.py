class Dictionary:

    my_dict_length = 6

    def __init__(self):
        self.data = [None] * Dictionary.my_dict_length


    def set(self, key, value):
        """
        Description  create a new entry.  if the key already exists it will be replaced
        Parameters:  'key' : 'value'
        """
        index = self.get_index(key)

        for x in self.data[index] or []:
            if x[0] == key:
                self.data[index].remove(x)

        if self.data[index] is None:
            self.data[index] = list()
        self.data[index].append((key, value))


    def get(self, key, default=None):
        """
        """
        index = self.get_index(key)

        for x in self.data[index]:
            if x[0] == key:
                return x[1]

        # print(self.data[index])


    def contains(self, key):
        """
        """
        # index = self.get_index(key) #gets none some times; i do not know why
        # for x in self.data[index] or []:
        #     if x[0] == key:
        #         return True
        #     else:
        #         return False

        return key in [x[0] for x in (self.data[self.get_index(key)] or [])]


    def get_index(self, key):
        """
        Description:  uses hashes to find where to store the information
        """
        return hash(key) % Dictionary.my_dict_length

    def delete(self, key):
        """
        Description delete a specified key pair in our list
        Parameters: 'key' is the value to search for a delete
        """
        index = self.get_index(key)

        for i, x in enumerate(self.data[index] or []):
            if x[0] == key:
                del self.data[index][i]


    def print_list(self):
        """
        """
        print(self.data)

# my_dict = Dictionary()
# my_dict.set("A", 15)
# my_dict.set("B", 50)
# my_dict.set("C", 105)
# my_dict.set("D", 105)
# my_dict.set("E", 105)
# my_dict.set("F", 105)
# my_dict.delete("A")
# my_dict.delete("B")
# my_dict.delete("C")
# my_dict.delete("D")
# my_dict.delete("E")
# my_dict.delete("F")
# my_dict.print_list()