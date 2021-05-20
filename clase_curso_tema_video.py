class curso_tema_video:
    def __init__(self, id_CTV = 0, id_CT = 0, id_video = 0):
        self.id_CTV = id_CTV
        self.id_CT = id_CT
        self.id_video = id_video
    
    def guardar(self):
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\curso_tema_video.txt")
        f.write(f'id_CTV = {self.id_CTV} id_CT = {self.id_CT} id_video = {self.id_video}')
        f.close

    def consultar_todo(self):
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\curso_tema_video.txt")
        print(f.read())
        f.close
    
    def consultar_por_id(self, id):
        self.id = str(id)
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\curso_tema_video.txt")
        for sentencia in f:
            recorrido = sentencia.strip().split()
            if recorrido[2] == self.id:
                print(recorrido)
        f.close