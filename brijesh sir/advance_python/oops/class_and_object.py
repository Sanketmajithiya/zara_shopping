class Auth: # class 
    class Register:
        # data memeber
        username = "brijesh07"
        password = "1234"
        confirm_password = "1234"

        #  member function
        def display(self):
            return "hello"

        # def check_password():
        #     if password:
        #         return True
    
aut1 = Auth()
obj1 = aut1.Register()
print(obj1.confirm_password)
print(obj1.password)
print(obj1.username)
print(obj1.display())

aut2 = Auth()
obj2 = aut2.Register()
print(obj2.confirm_password)
print(obj2.password)
print(obj2.username)
print(obj2.display())