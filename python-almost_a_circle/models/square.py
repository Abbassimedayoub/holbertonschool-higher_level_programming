#!/usr/bin/python3
class Square(Base):
    """A class representing a square, inheriting from Base"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.
        """
        super().__init__(id)  # Call the superclass constructor
        self.size = size  # Set the size attribute
        self.x = x  # Set the x-coordinate attribute
        self.y = y  # Set the y-coordinate attribute

    @property
    def size(self):
        """Getter method for the size attribute"""
        return self.width  # Since width and height are the same for a square

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Size must be a positive integer")
        self.width = value  # Set both width and height to the same value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args):
        """
        Updates the attributes of the square using positional arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
