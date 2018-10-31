class Test:
    def __init__(self, x=5):    # constructor
        self.x = x;

    def mult (self, b):
        return self.x * b;

    def __eq__ (self, other): # == operator overload
        return self.x == other.x

a= Test()
print a.mult(10)
print Test() == Test()
print Test(2) == Test(3)
