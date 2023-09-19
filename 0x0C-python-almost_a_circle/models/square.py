#!/usr/bin/python3
""" models/square.py """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class initializer """
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """ Update the attributes """
        if not args:
            if kwargs.get('id') is not None:
                self.id = kwargs.get('id')
            if kwargs.get('size') is not None:
                self.size = kwargs.get('size')
            if kwargs.get('x') is not None:
                self.x = kwargs.get('x')
            if kwargs.get('y') is not None:
                self.y = kwargs.get('y')
        else:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg

    def to_dictionary(self):
        """self to dict"""
        return dict({
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'size': self.size
        })

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        class_name = self.__class__.__name__
        s_id = self.id
        s_x = self.x
        s_y = self.y
        s_s = self.size
        return f"[{class_name}] ({s_id}) {s_x}/{s_y} - {s_s}"
