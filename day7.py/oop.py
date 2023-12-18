class House:

    def __init__(self, window=1, door=1,color="red",price=250000):
        self.window=window
        self.door=door
        self.color=color
        self.price=price

    def set_color(self,color):
        self.color = color

    def get_color(self):
        return self.color
    
    def __eq__(self, __value: object) -> bool:
        return self.window==__value.window
    
    def __gt__(self,value):
        return self.price==value.price

ram_ko_ghar=House()
shyam_ko_ghar=House(window=12, color="black",price=3000000)
hari_ko_ghar=House(window=12, color="black",price=4000000)
krishna_ko_ghar=House(window=12, color="black",price=5000000)


# ram_ko_ghar.set_color("blue")
print(ram_ko_ghar.get_color())
print(shyam_ko_ghar.get_color())
print(ram_ko_ghar.__eq__(shyam_ko_ghar))
print(shyam_ko_ghar.__gt__(hari_ko_ghar))  # Output : 1
# print(ram_ko_ghar.door)
# print(ram_ko_ghar.window)
