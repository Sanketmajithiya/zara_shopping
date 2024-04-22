class Register:
    # constructor
    def __init__(self, username, password, confirm_password):
        self.u = username
        self.p = password
        self.cp = confirm_password

    def display(self):
        print(f"Your username is : {self.u}")
        print(f"Your pwd is : {self.p}")
        print(f"Your c_pwd is : {self.cp}")

brijesh = Register("brijesh07", '1234', '1234')
brijesh.display()


sanket = Register("sanket07", '12345', '12345')
sanket.display()