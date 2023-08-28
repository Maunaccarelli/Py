import wikipedia

class TesisSoftware:
    def __init__(self, titulo, autor, contenido):
        self.titulo = titulo
        self.autor = autor
        self.contenido = contenido
        self.citas = []
    
    def agregar_cita(self, cita):
        self.citas.append(cita)
    
    def buscar_informacion(self, termino):
        try:
            informacion = wikipedia.summary(termino, sentences=2)
            print("Información encontrada:")
            print(informacion)
        except wikipedia.exceptions.PageError:
            print("No se encontró información para el término:", termino)
    
    def mostrar_informacion(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Contenido:", self.contenido)
        
        if self.citas:
            print("Citas:")
            for i, cita in enumerate(self.citas, start=1):
                print(f"{i}. {cita}")
    
    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("Título: " + self.titulo + "\n")
            archivo.write("Autor: " + self.autor + "\n")
            archivo.write("Contenido:\n" + self.contenido + "\n")
            
            if self.citas:
                archivo.write("Citas:\n")
                for i, cita in enumerate(self.citas, start=1):
                    archivo.write(f"{i}. {cita}\n")
        print("Tesis guardada en", nombre_archivo)

# Ejemplo de uso
titulo_tesis = input("Ingrese el título de la tesis: ")
autor_tesis = input("Ingrese el autor de la tesis: ")
contenido_tesis = input("Ingrese el contenido de la tesis: ")

tesis = TesisSoftware(titulo_tesis, autor_tesis, contenido_tesis)

while True:
    opcion = input("¿Desea agregar una cita? (Sí/No): ").lower()
    if opcion == "no":
        break
    elif opcion == "sí" or opcion == "si":
        cita = input("Ingrese la cita: ")
        tesis.agregar_cita(cita)
    else:
        print("Opción no válida. Por favor, responda 'Sí' o 'No'.")

termino_busqueda = input("Ingrese un término para buscar información en línea: ")
tesis.buscar_informacion(termino_busqueda)

tesis.mostrar_informacion()

nombre_archivo = input("Ingrese el nombre del archivo para guardar la tesis: ")
tesis.guardar_en_archivo(nombre_archivo)