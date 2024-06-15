'''class A:
    def __init__(self):
        self.a=None
        self._b__=None
    def fun1(self):
        print("hello")
    def fun2(self):
        print('mani')
o1=A()
o2=B()
o1.fun1()'''
class A:
    def __init__(self,a,b):
        self.A=a
        self.__B=b
    def print(self):
        print(self.__B)
obj1=A(2,5)
print(obj1.A)
obj1.print()



