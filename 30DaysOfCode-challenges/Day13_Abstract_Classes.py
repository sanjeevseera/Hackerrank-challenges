"""
Today, we're taking what we learned yesterday about Inheritance and extending it to Abstract Classes.
Because this is a very specific Object-Oriented concept, submissions are limited to the few languages that use this construct.
Check out the Tutorial tab for learning materials and an instructional video!
"""

from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display():
        pass


# Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price

    def display(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Price: {}".format(self.price))


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()