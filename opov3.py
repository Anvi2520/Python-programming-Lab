#3. Write a program that overloads the + operator so that it can add two objects of class Function.
def GCD(num,deno):
    if(deno==0):
        return num
    else:
        return GCD(deno, num%deno)
class Function:
    def __init__(self):
        self.num=0
        self.deno=1
    def get(self):
        self.num=int(input("Enter the numerator: "))
        self.deno=int(input("Enter the denominator: "))
    def simplify(self):
        common_divisor=GCD(self.num,self.deno)
        self.num//=common_divisor
        self.deno//=common_divisor
    def __add__(self,F):
        temp=Function()
        temp.num=(self.num*F.deno)+ (F.num*self.deno)
        temp.deno=self.deno*F.deno
        return temp
    def display(self):
        self.simplify()
        print(self.num,"/",self.deno)
F1=Function()
F1.get()
F2=Function()
F2.get()
F3=F1+F2
print("Result: ")
F3.display()
