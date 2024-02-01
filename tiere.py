class Tiere():
    typ = "Säugetiere"
    def __init__(self, name, herkunft, hauptnahrung, ist_bedroht, ist_vegetarisch):
        self.name = name
        self.herkunft = herkunft
        self.hauptnahrung = hauptnahrung
        self.ist_bedroht = ist_bedroht
        self.ist_vegetarisch = ist_vegetarisch 

    def zeige_info(self):
        print(f"Tiere Name: {self.name}, Herkunft: {self.herkunft}, Hauptnahrung: {self.hauptnahrung}, Ist_bedroht: {self.ist_bedroht}, Ist_vegerarisch: {self.ist_vegetarisch}")

my_auto = Tiere("Löwe", "Afrikas südlich", "Fleischfresser (carnivor)", "Gefährdet", "nein")
my_auto.zeige_info()
        
            