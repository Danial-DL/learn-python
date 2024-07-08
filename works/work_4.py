class Triangle:
    def __init__(self):
        self.first = int(input("Enter the first side : "))
        self.second = int(input("Enter the second side : "))
        self.third = int(input("Enter the third side : "))
    def Proof(self):
        if self.first + self.second > self.third and self.first + self.third > self.second and self.second + self.third > self.first :
            print("The condition of being a triangle is fulfilled")
            print(f"That is, a triangle can be formed with sides {self.first} , {self.second} , and {self.third}")
            print(True)
        else :
            print("The condition of being a triangle is not fulfilled !! ")
            print(f"That is, a triangle can not be formed with sides {self.first} , {self.second} , and {self.third} !!")
            print(False)
analyze = Triangle()
analyze.Proof()