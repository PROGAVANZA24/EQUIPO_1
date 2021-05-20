class curso_tema:
    def __init__(self, id_CT = 0, id_curso = 0, id_tema = 0):
        self.id_CT = id_CT
        self.id_curso = id_curso
        self.id_tema = id_tema
    
    def guardar(self):
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\curso_tema.txt")
        f.write(f'id_CT = {self.id_CT} id_curso = {self.id_curso} id_tema = {self.id_tema}')
        f.close
    
    def consultar_todo(self):
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\curso_tema.txt")
        print(f.read())
        f.close

    def consultar_por_id(self, id):
        self.id = str(id)
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\curso_tema.txt")
        for sentencia in f:
            recorrido = sentencia.strip().split()
            if recorrido[2] == self.id:
                print(recorrido)
        f.close