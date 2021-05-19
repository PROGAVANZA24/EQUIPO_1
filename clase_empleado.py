class empleado:
    def __init__(self, id_empleado = 0, nombre = "DEFAULT", direccion = "DEFAULT"):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.direccion = direccion

    def guardar(self):
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\empleado.txt", "a", encoding="utf8")
        f.write(f'id = {self.id_empleado} nombre = {self.nombre} direccion = {self.direccion}+"\n"')
        f.close
    
    def consultar_todo(self):
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\empleado.txt")
        print(f.read())
        f.close

    def consultar_por_id(self, id):
        self.id = str(id)
        f = open("C:\\Users\\McAik\\OneDrive\\Documentos\\FACPYA\\SEGUNDO SEMESTRE\\Programacion Avanzada\\Programa PIA\\empleado.txt")
        for raya in f:
            otracosa = raya.strip().split()
            if otracosa[2] == self.id:
                print(otracosa)
        f.close