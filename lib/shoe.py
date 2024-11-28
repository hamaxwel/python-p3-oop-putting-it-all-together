class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str) and value:
            self._brand = value
        else:
            raise ValueError("Brand must be a non-empty string.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")  

    def cobble(self):
        print("Your shoe is as good as new!") 
