class Array:
    def __init__(self, length=10):
        self.length = length
        self.array = [None] * length

    def get_length(self):
        return self.length

    def set_value(self, index, value):
        if index < self.length:
            self.array[index] = value
        else:
            print("Index out of bounds")

    def get_value(self, index):
        if index < self.length:
            return self.array[index]
        else:
            print("Index out of bounds")
            return None

    def display(self):
        print(self.array)
