# class Computer:
    
#     className = "Computer_class"

#     def __init__(self,m1,m2,m3):
#             self.m1=m1
#             self.m2=m2
#             self.m3=m3

#   #instance method as using self
#     def printValue(self):
#         print(self.m1+""+self.m2+""+self.m3)

#     def config(self):
#          print("config-function")
    
#     @classmethod
#     def getSchool(cls):
#         print(cls.className)

#     @staticmethod
#     def info():
#         print("this is the static method")
    

# com = Computer(1,2,3)

# # Computer.config(com)

# Computer.getSchool()

# Computer.info()



#INNERCLASS





# class Student:
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno= rollno
#         self.lp = self.Laptop()
    
#     def show(self):
#         print(self.name,self.rollno)
    
    
#     class Laptop:

#         def __init__(self) :
#             self.brand = "HP"
#             self.cpu = "i5"
#             self.ram = 2500
#         def show(self):
#             print(self.brand)
#             print(self.cpu)
#             print(self.ram)

# s1 = Student("ak",23)
# s2 = Student("pk",24)

# # lap1 = s1.lp()
# # lap2 = s2.lp()

# # print((s1.lp.brand))
# # print((s2.lp.cpu))

# print(s2.lp.show())




#INHERITENCE


# class A:   

#     def __init__(self):
#         print("Class A")

#     def feature1(self):
#         print("Feature 1 working")
    
#     def feature2(self):
#         print("Feature 2 working")


# class B(): # B(A) Single Inheritance          # B(A)  ->  C(B)  MutliLevel Inheritance
    
#     def __init__(self):
#         print("class B")


#     def feature3(self):
#         print("Feature 3 working ")
    
#     def feature4(self):
       
#         print("Feature 4 working")


# class C(B,A): #Multiple Inhertance         It depends on order of Inhertence Classes Names
     
#       def __init__(self):
#           print("Class C")

#       def feature5(self):
#            super().__init__()
#            super().feature3()  # this is to call features of inherited class  only that is first inherited C(B,A) as it accessible only B's Features
#            print("feature 5 working")


# c = C()
# c.feature5()
# # you  can all features of A and B and C

# # b = B()
# # print(b.feature1())




