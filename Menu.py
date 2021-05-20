from clase_empleado import empleado
from clase_curso import curso
from clase_curso_tema import curso_tema
from clase_curso_tema_video import curso_tema_video
from clase_video import video
from clase_tema import tema


menuprincipal = int(input("Menu principal: \n 1- Administrar empleados \n 2.- Administrar cursos \n 3- Administrar temas \n 4- Administrar videos \n 5-Administrar los temas asignados al curso \n 6- Administrar los videos asignados a los temas del curso \n"))
while menuprincipal != 0:
    if menuprincipal == 1:
        menu_administrar_empleados = True
    elif menuprincipal == 2:
        pass
    elif menuprincipal == 3:
        pass
    elif menuprincipal == 4:
        pass
    elif menuprincipal == 5:
        pass
    elif menuprincipal == 6:
        pass
    else:
        print("Opcion no valida")
    menuprincipal = int(input("Menu principal: \n 1- agregar empleados \n 2.- Administrar cursos \n 3- Administrar temas \n 4- Administrar videos \n 5-Administrar los temas asignados al curso \n 6- Administrar los videos asignados a los temas del curso \n"))
    while menu_administrar_empleados == True:
        opciones_menu_empleados = int(input("Menu de administracion de empleados: \n 1-Crear nuevo empleado \n 2- Consultar todos los empleados \n 3- Consultar a detalle \n"))
        if opciones_menu_empleados == 1:
            print("creando")
        elif opciones_menu_empleados == 2:
            print("creando")
        elif opciones_menu_empleados == 3:
            print("creando")
        elif opciones_menu_empleados == 0:
            menu_administrar_empleados = False
        elif opciones_menu_empleados >= 4:
            menu_administrar_empleados = False