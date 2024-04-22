class employee:
    def __init__(self, fname, lname, email, password):
        self.f = fname
        self.l = lname
        self.e = email
        self.__p = password

    def info(self):
        print(f"Employee name : {self.f + ' ' + self.l}")
        print(f"Email: {self.e}")

brijesh = employee("brijesh", 'gondaliya', 'brijesh@gmail.com', '1234')
print(brijesh.e)
print(brijesh._employee__p)
brijesh.info()
print(dir(brijesh))