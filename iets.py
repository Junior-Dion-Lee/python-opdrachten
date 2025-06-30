class Laptop:
    display = "1920x1080"

    def __init__(self, gpu):
        self.gpu = gpu

    def summary(self):
        print(f"Display: {self.display}")
        print(f"GPU: {self.gpu}")

    def info():
        print("Hier wordt info over laptops gegeven")

laptop = Laptop("Nvidia 3070")
laptop.summary()
Laptop.info()

class lokaal:

    def __init__(self, lokaalnaam, richting):
        self.lokaalnaam = lokaalnaam
        self.richting = richting


    def help(self):
        print(f"{self.lokaalnaam} is {self.richting}")       
            
lokaalen = [
    lokaal("c1.13, west"),
    lokaal("c1.04, west"),
    lokaal("c1.06, west")
 ]


for lokaal in lokaalen:
    lokaal.help()
