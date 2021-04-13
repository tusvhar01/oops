class programmer:
    comany="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def information(self):
        print(f"the name of programmer of {self.comany} is {self.name} and product is {self.product}")


harry=programmer("harry","skype")
tushar=programmer("harry","github")
harry.information()
tushar.information()
 
