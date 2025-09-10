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

def obtener_datos():
    eda=int(input("digite la edad del perro:"))
    nom=str(input("digite el nombre del perro:"))
    col=str(input("digite el color del perro:"))
    return eda, nom, col
eda, nom, col = obtener_datos()
mi_perro=Perro(eda, nom, col)


def concentir1():
    print("desea concentir al perro ")
    x=str(input("digite si o no:"))
    if(x=="si"):
        mi_perro.concentir()
    elif(x=="no"):
        print("pienselo")
        while (x!="si"):
            print("desea concentir al perro: ")
            x=str(input("digite si o no:"))
        if(x=="si"):
            mi_perro.concentir()
def alimentar1():
    print("desea alimentar al perro ")
    decision1=str(input("digite si o no:"))
    if(decision1=="si"):
        mi_perro.alimentar()
    elif(decision1=="no"):
        print("pienselo")
        while (decision1!="si"):
            print("desea alimentar al perro: ")
            decision1=str(input("digite si o no:"))
        if(decision1=="si"):
            mi_perro.alimentar()




