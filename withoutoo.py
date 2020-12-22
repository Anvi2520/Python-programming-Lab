class Complex:
    def __init__(self):
        self.real=0
        self.imag=0
    def setValue(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,c):
        temp=Complex()
        temp.real=self.real+c.real
        temp.imag=self.imag+c.imag
        return temp
    def display(self):
        print("(",self.real,"+",self.imag,"i)")
c1=Complex()
c1.setValue(1,2)
c2=Complex()
c2.setValue(3,4)
c3=Complex()
c3=c1+c2
c3.display()
