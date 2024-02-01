class Animal():
    def __init__(self, name, herkunft, hauptnahrung, ist_bedroht, ist_vegetarisch):
        self.name = name
        self.herkunft = herkunft
        self.hauptnahrung = hauptnahrung
        self.ist_bedroht = ist_bedroht
        self.ist_vegetarisch = ist_vegetarisch  

    def zeige_info(self):
       print(f"Tiere Name: {self.name}, Herkunft: {self.herkunft}, Hauptnahrung: {self.hauptnahrung}, Ist_bedroht: {self.ist_bedroht}, Ist_vegerarisch: {self.ist_vegetarisch}")
       

class Dog(Animal):
    typ = "Dog"
    def __init__(self, name, herkunft, hauptnahrung, ist_bedroht, ist_vegetarisch, geweindigkeit):
        super().__init__(name, herkunft, hauptnahrung, ist_bedroht, ist_vegetarisch)  # This will call the Animal classes constructor method
        self.geweindigkeit = geweindigkeit

    def zeige_geweindigkeit(self):
     print(f"Maximal Geweindigkeit --> {self.geweindigkeit}")   

dog= Dog("Jimmy", "Deutschland", "Hundfutter", "nein", "ja", 50)
dog.zeige_info()
dog.zeige_geweindigkeit()
animal= Animal("Jimmy", "Deutschland", "Hundfutter", "nein", "ja")