class Perro:
    def __init__(self, edad, nombre, color):
        self.edad=edad
        self.nombre=nombre
        self.color=color


    #metodos
    def ladrar(self):
        print("Guau Guau")
   
    def saludar(self):
        print(f"hola el nombre del perro es {self.nombre}, su color es {self.color} y tiene {self.edad}")


    def concentir(self):
        print(f"el usuario esta concintiendo al perro {self.nombre}")
   
    def alimentar(self):
        print(f"el usuario esta alimentando al perro")
    #hacer feliz al perro
    def hacerfeliz(self):
        print(f"el perro {self.nombre} esta feliz porque ya lo alimentaron y lo concintieron")




