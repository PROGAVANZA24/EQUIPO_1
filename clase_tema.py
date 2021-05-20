class tema:
    def __init__(self, id_tema = 0, nombre = "DEFAULT"):
        self.id_tema = id_tema
        self.nombre = nombre
    
    def guardar(self):
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\tema.txt", encoding="utf8")
        f.write(f'id_tema = {self.id_tema} nombre = {self.nombre}')
        f.close
    
    def consultar_todo(self):
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\tema.txt")
        print(f.read())
        f.close
    
    def consultar_por_id(self, id):
        self.id = str(id)
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\tema.txt")
        for sentencia in f:
            recorrido = sentencia.strip().split()
            if recorrido[2] == self.id:
                print(recorrido)
        f.close      