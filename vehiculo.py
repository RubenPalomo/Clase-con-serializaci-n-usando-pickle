import pickle

class Vehiculo:
    modelo = None
    ruedas = None

    def __init__(self, modelo, ruedas):
        self.modelo = modelo
        self.ruedas = ruedas
    
    def __str__(self):
        return f'El vehículo es un {self.modelo} y tiene {self.ruedas} ruedas.'

def main():
    coche = Vehiculo("Coche", 4)
    f = open("ejemplo.txt", "wb")
    pickle.dump(coche, f)
    f.close()

    f = open("ejemplo.txt", "rb")
    el_coche_de_antes = pickle.load(f)
    f.close()
    print(str(el_coche_de_antes))

if (__name__ == "__main__"):
    main()
