class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display(self):
        print(f"Title:{self.title} , Author: {self.author}")
        
b = Book("data science","pavan")
b.display()

f = Person("pavan",23)
print(f.name)