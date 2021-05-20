from typing_extensions import ParamSpecKwargs
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
        while menu_administrar_empleados == True:
            opciones_menu_empleados = int(input("Menu de administracion de empleados: \n 1-Crear nuevo empleado \n 2- Consultar todos los empleados \n 3- Consultar a detalle \n"))
            if opciones_menu_empleados == 1:
                eid = int(input("Ingrese el ID del empleado"))
                enom = input("ingrese el nombre ")
                edi = input("Ingrese la direccion del empleado")
                empleado1 = empleado(eid, enom, edi)
                empleado1.guardar()
                print("se ha guardado empleado")
            elif opciones_menu_empleados == 2:
                print("Empleados:")
                empleado1 = empleado()
                empleado1.consultar_todo()
            elif opciones_menu_empleados == 3:
                id_emple = input("ingrese el id de empleado:\n")
                empleado1 = empleado()
                empleado1.consultar_por_id(id_emple)
            elif opciones_menu_empleados == 0:
                menu_administrar_empleados = False
            elif opciones_menu_empleados >= 4:
                menu_administrar_empleados = False
    elif menuprincipal == 2:
        menu_administrar_cursos = True
        while menu_administrar_cursos == True:
            opciones_menu_cursos = int(input("Menu de administracion de cursos: \n 1-Crear nuevo curso \n 2- Consultar todos los curso \n 3- Consultar a detalle \n"))
            if opciones_menu_cursos == 1:
                cid = int(input("Ingrese el id del curso: "))
                cde = input("Ingrese una descripcion: ")
                emid = int(input("ingrese un id al empleado: "))
                curso1 = curso(cid, cde, emid)
                curso1.guardar()
                print("Se guardo curso")
            elif opciones_menu_cursos == 2:
                print("Cursos: ")
                curso1 = curso()
                curso1.consultar_todo()
            elif opciones_menu_cursos == 3:
                id_cur = input("Ingrese id del curso que busca: ")
                curso1 = curso()
                curso1.consultar_por_id(id_cur)
            elif opciones_menu_cursos == 0:
                menu_administrar_cursos = False
            elif opciones_menu_cursos >= 4:
                menu_administrar_cursos = False
    elif menuprincipal == 3:
        menu_administrar_tema = True
        while menu_administrar_tema == True:
            opciones_menu_tema = int(input("Menu de administracion de temas: \n 1-Crear nuevo tema \n 2- Consultar todos los temas \n 3- Consultar a detalle \n"))
            if opciones_menu_tema == 1:
                tid = int(input("Ingrese un id para el tema: "))
                tnom = input("Ingrese un nombre al tema")
                tema1 = tema(tid, tnom)
                tema1.guardar()
                print("Se guardo el tema")
            elif opciones_menu_tema == 2:
                print("Temas: ")
                tema1 = tema()
                tema1.consultar_todo()
            elif opciones_menu_tema == 3:
                id_tem = input("Ingrese el id de tema a buscar: ")
                tema1 = tema()
                tema1.consultar_por_id(id_tem)
            elif opciones_menu_tema == 0:
                menu_administrar_tema = False
            elif opciones_menu_tema >= 4:
                menu_administrar_tema = False
    elif menuprincipal == 4:
        pass
    elif menuprincipal == 5:
        pass
    elif menuprincipal == 6:
        pass
    else:
        print("Opcion no valida")
    menuprincipal = int(input("Menu principal: \n 1- agregar empleados \n 2.- Administrar cursos \n 3- Administrar temas \n 4- Administrar videos \n 5-Administrar los temas asignados al curso \n 6- Administrar los videos asignados a los temas del curso \n"))