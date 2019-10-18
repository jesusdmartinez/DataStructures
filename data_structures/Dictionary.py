class Dictionary:

    my_dict_length = 3

    def __init__(self):
        self.data = [None] * Dictionary.my_dict_length


    def set(self, key, value):
        """
        Description  create a new entry.  if the key already exists it will be replaced by the latest entry.
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
        Description:  delete a specified key pair in our list
        Parameters: 'key' is the value to search for and delete
        """
        # index = self.get_index(key)
        #
        # for i in self.data[index] or []:
        #     if i[0] == key:
        #         self.data[index].remove(i)

        index = self.get_index(key)

        for i, x in enumerate(self.data[index] or []):
            if x[0] == key:
                del self.data[index][i]

    def increase_array(self):
        """
        copy list to somewhere
        """
        # for list in self.data:
        temp_list = []

        for list in self.data:
            temp_list.append(list)

        self.data = [None] * 100

        for list in temp_list:
            self.data.set(list[0], list[1])


    def print_list(self):
        """
        """
        print(self.data)

my_dict = Dictionary()
my_dict.set("A", 15)
my_dict.set("B", 100)
my_dict.increase_array()
# my_dict.print_list()