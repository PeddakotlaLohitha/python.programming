from typing import override
class sub:
    def add(self):
        print("it is super class")
class child(sub):
    @override
    def add(self):
        print("child class:")
    def sum(self):
        print("it is child class method:")
n=child()
n.add()
n.add()
n.sum()
