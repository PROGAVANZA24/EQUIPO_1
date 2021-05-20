video de clase :
    def  __init__ ( self , id_video  =  0 , nombre  =  "DEFAULT" , url  =  "DEFAULT.com" , fecha_publicacion  =  "DEFAULT" ):
        yo . id_video  =  id_video
        yo . nombre  =  nombre
        yo . url  =  url
        yo . fecha_publicacion  =  fecha_publicacion
        
    def  guardar ( yo ):
        f  =  open ( "C: \\ Users \\ GBetaGlo \\ OneDrive \\ Documentos \\ FACPYA \\ SEGUNDO SEMESTRE \\ Programacion Avanzada \\ Programa PIA \\ video.txt" , encoding = "utf8" )
        f . write ( f'id_video = { self . id_video } nombre = { self . nombre } url = { self . url } fecha_publicacion = { self . fecha_publicacion } ' )
        f . cerca
    
    def  consultar_todo ( yo ):
        f  =  open ( "C: \\ Usuarios \\ GBetaGlo \\ OneDrive \\ Documentos \\ FACPYA \\ SEGUNDO SEMESTRE \\ Programacion Avanzada \\ Programa PIA \\ video.txt" )
        imprimir ( f . leer ())
        f . cerca
    
    def  consultar_por_id ( self , id ):
        yo . id  =  str ( id )
        f  =  open ( "C: \\ Usuarios \\ GBetaGlo \\ OneDrive \\ Documentos \\ FACPYA \\ SEGUNDO SEMESTRE \\ Programacion Avanzada \\ Programa PIA \\ video.txt" )
        para  sentencia  en  f :
            recorrido  =  sentencia . tira (). dividir ()
            if  recorrido [ 2 ] ==  self . id :
                imprimir ( recorrido )
        f . cerca       