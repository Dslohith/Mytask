# class myobj:
#     def mymeth(self):
#         print("this is defult contractor")
#
#     def mainMetho(self):
#         print("we are doing main method")
#
# obj=myobj()
# obj.mymeth()
# obj.mainMetho()

# inheratance

# single level inhertancee
# class A :
#
#     def methone(self):
#         print("this is level one and class one")
#
# class B(A):
#     def methtwo(self):
#         print("this is level two and class tWo")
#
# Mysingleobjb= B()
# Mysingleobjb.methone()
# Mysingleobjb.methtwo()

# class A :
#     X,Y=2,3
#     def methone(self):
#         print(self.X*self.Y,"hi")
#
# class B(A):
#     A,B=5,7
#     def methtwo(self):
#         print(self.X + self.Y,"hi twwo")
#
# Mysingleobjb= B()
# Mysingleobjb.methone()
# Mysingleobjb.methtwo()

# mullti level inheratance

#
# class A :
#     X,Y=2,3
#     def methone(self):
#         print(self.X*self.Y,"hi")
#
# class B(A):
#     A,B=5,7
#     def methtwo(self):
#         print(self.X + self.Y,"hi twwo")
#
# class C(B):
#     A,B=15,7
#     def meththree(self):
#         print(self.X - self.Y,"hi three")
#
# Mysingleobjb= C()
# Mysingleobjb.methone()
# Mysingleobjb.methtwo()
# Mysingleobjb.meththree()

# HIRARACYCAL inheratance
# class A :
#     X,Y=2,3
#     def methone(self):
#         print(self.X*self.Y,"hi")
#
# class B(A):
#     A,B=5,7
#     def methtwo(self):
#         print(self.X + self.Y,"hi twwo")
#
# class C(A):
#     A,B=15,7
#     def meththree(self):
#         print(self.X - self.Y,"hi three")
#
# Mysingleobjb= C()
# Mysingleobjb.methone()
# Mysingleobjb.meththree()
#
# MysingleobjI= B()
# MysingleobjI.methone()
# MysingleobjI.methtwo()

# variable overriding

# class pararnt:
#     name="Lohith"
#
#
# class child(pararnt):
#     name = "lohi"#im creating same variable in the child class and its overrding the vaorable value and giving the latest vale
#
# mybo=child()
# print(mybo.name)

# methodoverridng#
# class mainbank:
#     def rateOfIntrest(self):
#         print("sbi rate of intrrst is 10 %")

# class Xbank(mainbank):
#     def rateOfIntrest(self):
#         print("sbi rate of intrrst is 112 %")
#
# class Ybank(mainbank):
#     def rateOfIntrest(self):
#         print("sbi rate of intrrst is 134 %")
#
# bankobjX=Xbank()
# bankobjX.rateOfIntrest()
#
# bankobjY=Ybank()
# bankobjY.rateOfIntrest()

# method overloading can only achive my using inheratance

# overloading python is not support fully polyimorphism but we can achive somehow
class myage:
    def agevali(self,name=None):
        if name == None:
            print(f"u have not entered any name : {name} ")
        else:
            print(f"u have entered any name : {name} ")

myobk=myage()
myobk.agevali("lohith")
myobk.agevali()
# it shows differnt behaviour based on calling like now im passong variable it print f"u have not entered any name : {name} and if i entered name and this print another statment