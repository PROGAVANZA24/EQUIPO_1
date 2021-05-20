from os import truncate
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
        menu_administrar_video = True
        while menu_administrar_video == True:
            opciones_menu_video = (input("Menu de administracion de video: \n 1-Crear nuevo video \n 2- Consultar todos los video \n 3- Consultar a detalle \n"))
            if opciones_menu_video == 1:
                vid = int(input("Ingrese un id al video"))
                vnom = input("ingrese un nombre al video")
                vurl = input("ingrese una url")
                vfecha = input("mencione la fecha de publicacion")
                video1 = video(vid, vnom, vurl, vfecha)
                video1.guardar()
                print("se ha guardado el video")
            elif opciones_menu_video == 2:
                print("videos: ")
                video1 = video()
                video1.consultar_todo()
            elif opciones_menu_video == 3:
                id_vid = input("ingrese id de video a buscar: ")
                video1 = video()
                video1.consultar_por_id(id_vid)
            elif opciones_menu_video == 0:
                menu_administrar_video = False
            elif opciones_menu_video >= 4:
                menu_administrar_video = False
    elif menuprincipal == 5:
        menu_administrar_temasasigna = True
        while menu_administrar_temasasigna == True:
            opciones_menu_temasasigna = (input("Menu de administracion de temas asignados: \n 1-Crear nuevo tema asignado\n 2- Consultar todos los temas asignados \n 3- Consultar a detalle \n"))
            if opciones_menu_temasasigna == 1:
                ctid = int(input("ingrese id de tema"))
                cuid = int(input("ingrese id de curso"))
                temid = int(input("ingrese aid de tema"))
                cu_te = curso_tema(ctid, cuid, temid)
                cu_te.guardar()
                print("se ha guardado el tema")
            elif opciones_menu_temasasigna == 2:
                print("temas asignados: ")
                cu_te = curso_tema()
                cu_te.consultar_todo()
            
            elif opciones_menu_temasasigna == 3:
                id_cu_te = input("ingrese id de curso asignado: ")
                cu_te = curso_tema()
                cu_te.consultar_por_id(id_cu_te)
            elif opciones_menu_temasasigna == 0:
                menu_administrar_temasasigna = False
            elif opciones_menu_temasasigna >= 4:
                menu_administrar_temasasigna = False
    elif menuprincipal == 6:
        menu_administrar_temavideo = True
        while menu_administrar_temavideo == True:
            opciones_menu_temavideo = (input("Menu de administracion de temavideo: \n 1-Crear nuevo temavideo \n 2- Consultar todos los temavideo \n 3- Consultar a detalle \n"))
            if opciones_menu_temavideo == 1:
                ctvid = int(input("ingrese id de temavideo"))
                cuteid = int(input("ingrese id de curso"))
                viide = int(input("Ingrese id de video"))
                cu_te_vi = curso_tema_video()
                cu_te_vi.guardar()
                print("se guardo el cursotemavideo")
            elif opciones_menu_temavideo == 2:
                print("curso temavideo")
                cu_te_vi = curso_tema_video()
                cu_te_vi.consultar_todo()
            elif opciones_menu_temavideo == 3:
                id_cu_te_vi = input("ingrese el id")
                cu_te_vi = curso_tema_video()
                cu_te_vi.consultar_por_id(id_cu_te_vi)
            elif opciones_menu_temavideo == 0:
                menu_administrar_temavideo = False
            elif opciones_menu_temavideo >= 4:
                menu_administrar_temavideos = False
    else:
        print("Opcion no valida")
    menuprincipal = int(input("Menu principal: \n 1- agregar empleados \n 2.- Administrar cursos \n 3- Administrar temas \n 4- Administrar videos \n 5-Administrar los temas asignados al curso \n 6- Administrar los videos asignados a los temas del curso \n"))