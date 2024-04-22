"""
single, multiple, multi level, herarchical, hybrid
"""
# Single inheritance
# class employee:
#     def __init__(self, role, fullname, salary):
#         self.r = role
#         self.f = fullname
#         self.s = salary

#     def info(self):
#         print(f"Name: {self.f}")
#         print(f"Roll: {self.r}")
#         print(f"Total salary: {self.s}")

# class manager(employee):
#     def __init__(self, role, fullname, salary, ta=1000, ma=300):
#         super().__init__(role, fullname, salary)
#         self.ta = ta
#         self.ma = ma
    

#     def info(self):
#         global ta, ma
#         print(f"Name: {self.f}")
#         print(f"Roll: {self.r}")
#         print(f"Total salary: {self.s + self.ta + self.ma}")


# sanket = employee("faculty", "sanket majithiya", 10000)
# sanket.info()

# brijesh = manager("Manager", "brijesh gondaliya", 12000, 2000, 500)
# brijesh.info()

# single inh.
# class A:
#     def a(self):
#         print("I am from class A")

# class B(A):
#     def b(self):
#         print("I amm from class B")

# obj = B()
# print(dir(obj))
# obj.a()
# obj.b()

# multilevel inh.
# class A:
#     def a(self):
#         print("I am from class A")

# class B(A):
#     def b(self):
#         print("I amm from class B")
# class C(B):
#     def c(self):
#         print("I amm from class C")

# obj = C()
# print(dir(obj))
# obj.a()
# obj.b()
# obj.c()

# multiple inh.
# class A:
#     def a(self):
#         print("I am from class A")

# class B:
#     def b(self):
#         print("I amm from class B")
# class C(A, B):
#     def c(self):
#         print("I amm from class C")

# obj = C()
# print(dir(obj))
# obj.a()
# obj.b()
# obj.c()

# herarchical inh.

# class A:
#     def a(self):
#         print("I anf from class A")
# class Al(A):
#     def al(self):
#         print("I anf from class Al")
# class Alr(Al):
#     def alr(self):
#         print("I anf from class Alr")
# class All(Al):
#     def all(self):
#         print("I anf from class All")
# class Ar(A):
#     def ar(self):
#         print("I anf from class Ar")
# class Arr(Ar):
#     def arr(self):
#         print("I anf from class Arr")
# class Arl(Ar):
#     def arl(self):
#         print("I anf from class Arl")

# obj = All()
# # print(dir(obj))
# print(Arr.__mro__)
# print(Arr.mro())