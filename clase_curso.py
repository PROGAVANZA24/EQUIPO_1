from clase_empleado import empleado


class curso:
    def __init__(self, id_curso = 0, descripcion = "DEFAULT", id_empleado = 0):
        self.id_curso = id_curso
        self.descripcion = descripcion
        self.id_empleado = id_empleado

    def guardar(self):
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\curso.txt")
        f.write(f'id_curso = {self.id_curso} descripcion = {self.descripcion} id_empleado = {self.id_empleado}')
        f.close

    def consultar_todo(self):
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\curso.txt")
        print(f.read())
        f.close
    
    def consultar_por_id(self, id):
        self.id = str(id)
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\curso.txt")
        for sentencia in f:
            recorrido = sentencia.strip().split()
            if recorrido[2] == self.id:
                print(recorrido)
        f.close