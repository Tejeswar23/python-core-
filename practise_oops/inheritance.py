# Single Inheritance
class Parent:
    def fun(self):
        print("This is parent fun()")
class Child(Parent):
    def fun1(self):
        print("This is child fun1()")

c = Child()
c.fun()

# Multilevel Inheritance
class GrandParent:
    def fun_gp(self):
        print("This is grandparent fun_gp()")
class Parent(GrandParent):
    def fun_p(self):
        print("This is parent fun_p()")
class Child(Parent):
    def fun_c(self):
        print("This is child fun_c()")
        
ch = Child()
ch.fun_gp()
ch.fun_p()

# Multiple Inheritance
class Father:
    def fun_f(self):
        print("This is father fun_f()")
class Mother:
    def fun_m(self):
        print("This is mother fun_m()")
class Child(Father, Mother):
    def fun_c(self):
        print("This is child fun_c()")
        
ch = Child()
ch.fun_f()
ch.fun_m()