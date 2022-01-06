class Add:
    def read(self):
        print("father")
class Sub(Add):
    def write(self):
            print("mother")
ob=Sub()

ob.read()
ob.write()