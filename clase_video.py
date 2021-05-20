class video:
    def __init__(self, id_video = 0, nombre = "DEFAULT", url = "DEFAULT.com", fecha_publicacion = "DEFAULT"):
        self.id_video = id_video
        self.nombre = nombre
        self.url = url
        self.fecha_publicacion = fecha_publicacion
        
    def guardar(self):
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\video.txt", encoding="utf8")
        f.write(f'id_video = {self.id_video} nombre = {self.nombre} url = {self.url} fecha_publicacion = {self.fecha_publicacion}')
        f.close
    
    def consultar_todo(self):
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\video.txt")
        print(f.read())
        f.close
    
    def consultar_por_id(self, id):
        self.id = str(id)
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\video.txt")
        for sentencia in f:
            recorrido = sentencia.strip().split()
            if recorrido[2] == self.id:
                print(recorrido)
        f.close       